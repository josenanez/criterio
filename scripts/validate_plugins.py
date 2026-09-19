#!/usr/bin/env python3
"""Validate the Criterio marketplace, its plugins, and the consistency of the docs.

Usage:
    python3 scripts/validate_plugins.py
    python3 scripts/validate_plugins.py --json

Standard library only.

Structure checks:
  - marketplace.json: required fields, semver, every listed plugin exists on disk,
    every plugin directory with a manifest is listed
  - plugin.json: required fields, name matches directory, semver, version matches
    the marketplace, licence declared
  - skills: SKILL.md present, front matter with name + description,
    name matches the directory
  - commands: front matter with description + argument-hint
  - a plugin that ships skills or commands also ships a README

Reference checks:
  - a command may reference skills of its OWN plugin only; plugins install
    independently, so a cross-plugin reference breaks

Consistency checks (the docs must not drift from the disk):
  - the plugin README lists every skill and command it ships
  - the terms version quoted in docs/acceptance.md matches TERMS.md

Exit code: 0 when there are no errors, 1 otherwise.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PLUGIN_FIELDS = ["name", "version", "description", "author", "license"]
MARKET_FIELDS = ["name", "version", "description", "owner", "plugins"]
SKILL_FIELDS = ["name", "description"]
COMMAND_FIELDS = ["description", "argument-hint"]

RE_SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
RE_KEBAB = re.compile(r"\*\*([a-z][a-z0-9]*(?:-[a-z0-9]+)+)\*\*")
RE_TERMS_VERSION = re.compile(r"Versi[oó]n\s+(\d+\.\d+)|Version\s+(\d+\.\d+)")


class Findings:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def load_json(path: Path, f: Findings) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        f.error(str(path), "file not found")
    except json.JSONDecodeError as e:
        f.error(str(path), f"invalid JSON: {e}")
    return None


def check_marketplace(root: Path, f: Findings) -> tuple[dict, set[str]]:
    path = root / ".claude-plugin" / "marketplace.json"
    data = load_json(path, f) or {}
    for field in MARKET_FIELDS:
        if field not in data:
            f.error("marketplace.json", f"missing field '{field}'")
    if "version" in data and not RE_SEMVER.match(str(data["version"])):
        f.error("marketplace.json", f"version '{data['version']}' is not semver")

    listed = {}
    for entry in data.get("plugins", []):
        name = entry.get("name")
        if not name:
            f.error("marketplace.json", "a plugin entry has no name")
            continue
        for field in ("description", "source", "category"):
            if field not in entry:
                f.error(f"marketplace.json[{name}]", f"missing field '{field}'")
        src = root / str(entry.get("source", "")).lstrip("./")
        if not src.is_dir():
            f.error(f"marketplace.json[{name}]", f"source '{entry.get('source')}' is not a directory")
        listed[name] = entry

    on_disk = {
        d.name for d in (root / "plugins").iterdir()
        if d.is_dir() and (d / ".claude-plugin" / "plugin.json").exists()
    }
    for missing in sorted(on_disk - set(listed)):
        f.error("marketplace.json", f"plugin '{missing}' exists on disk but is not listed")
    for ghost in sorted(set(listed) - on_disk):
        f.error("marketplace.json", f"plugin '{ghost}' is listed but has no manifest on disk")

    empty = {
        d.name for d in (root / "plugins").iterdir()
        if d.is_dir() and not (d / ".claude-plugin" / "plugin.json").exists()
    }
    for e in sorted(empty):
        f.warn("plugins/", f"directory '{e}' has no plugin.json and is ignored")

    return data, on_disk


def check_plugin(root: Path, name: str, market_version: str, f: Findings) -> dict:
    base = root / "plugins" / name
    manifest = load_json(base / ".claude-plugin" / "plugin.json", f) or {}

    for field in PLUGIN_FIELDS:
        if field not in manifest:
            f.error(f"{name}/plugin.json", f"missing field '{field}'")
    if manifest.get("name") and manifest["name"] != name:
        f.error(f"{name}/plugin.json", f"name '{manifest['name']}' does not match the directory")
    version = str(manifest.get("version", ""))
    if version and not RE_SEMVER.match(version):
        f.error(f"{name}/plugin.json", f"version '{version}' is not semver")
    if version and market_version and version != market_version:
        f.error(f"{name}/plugin.json", f"version {version} differs from the marketplace ({market_version})")

    skills: list[str] = []
    for d in sorted((base / "skills").iterdir()) if (base / "skills").is_dir() else []:
        if not d.is_dir():
            continue
        skill_file = d / "SKILL.md"
        if not skill_file.exists():
            f.error(f"{name}/skills/{d.name}", "missing SKILL.md")
            continue
        fm = front_matter(skill_file.read_text(encoding="utf-8"))
        if not fm:
            f.error(f"{name}/skills/{d.name}", "SKILL.md has no front matter")
            continue
        for field in SKILL_FIELDS:
            if not fm.get(field):
                f.error(f"{name}/skills/{d.name}", f"missing front matter field '{field}'")
        if fm.get("name") and fm["name"] != d.name:
            f.error(f"{name}/skills/{d.name}", f"front matter name '{fm['name']}' does not match the directory")
        if len(fm.get("description", "")) < 60:
            f.warn(f"{name}/skills/{d.name}", "description is short: it is what triggers auto-loading")
        skills.append(d.name)

    commands: list[str] = []
    cmd_dir = base / "commands"
    for c in sorted(cmd_dir.glob("*.md")) if cmd_dir.is_dir() else []:
        text = c.read_text(encoding="utf-8")
        fm = front_matter(text)
        if not fm:
            f.error(f"{name}/commands/{c.name}", "no front matter")
            continue
        for field in COMMAND_FIELDS:
            if not fm.get(field):
                f.error(f"{name}/commands/{c.name}", f"missing front matter field '{field}'")
        commands.append(c.stem)

        for token in set(RE_KEBAB.findall(text)):
            if token in skills or token in commands:
                continue
            if token in ("not-found",):
                continue
            f.warn(f"{name}/commands/{c.name}",
                   f"bold '{token}' looks like a skill reference but no such skill ships in this plugin")

    if (skills or commands) and not (base / "README.md").exists():
        f.error(name, "ships skills or commands but has no README.md")

    return {"name": name, "skills": skills, "commands": commands}


def check_consistency(root: Path, plugins: list[dict], f: Findings) -> None:
    for p in plugins:
        readme = root / "plugins" / p["name"] / "README.md"
        if not readme.exists():
            continue
        text = readme.read_text(encoding="utf-8")
        for skill in p["skills"]:
            if skill not in text:
                f.error(f"{p['name']}/README.md", f"does not list the skill '{skill}'")
        for cmd in p["commands"]:
            if cmd not in text:
                f.error(f"{p['name']}/README.md", f"does not list the command '{cmd}'")

    terms = root / "TERMS.md"
    acceptance = root / "docs" / "acceptance.md"
    if terms.exists() and acceptance.exists():
        m = RE_TERMS_VERSION.search(terms.read_text(encoding="utf-8"))
        version = (m.group(1) or m.group(2)) if m else None
        if not version:
            f.warn("TERMS.md", "no version could be read from the header")
        else:
            body = acceptance.read_text(encoding="utf-8")
            if f'"{version}"' not in body and f"'{version}'" not in body:
                f.error("docs/acceptance.md",
                        f"the gate example does not quote the current terms version ({version})")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Criterio marketplace and its plugins.")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true", help="warnings fail too")
    args = parser.parse_args()

    root = Path(".")
    f = Findings()

    market, on_disk = check_marketplace(root, f)
    market_version = str(market.get("version", ""))
    plugins = [check_plugin(root, name, market_version, f) for name in sorted(on_disk)]
    check_consistency(root, plugins, f)

    if args.json:
        print(json.dumps({
            "plugins": plugins,
            "errors": f.errors,
            "warnings": f.warnings,
        }, ensure_ascii=False, indent=2))
    else:
        print(f"\n=== marketplace '{market.get('name', '?')}' v{market_version} ===")
        for p in plugins:
            print(f"  {p['name']:20} {len(p['skills']):2} skills  {len(p['commands']):2} commands")
        print()
        for e in f.errors:
            print(f"  ERROR  {e}")
        for w in f.warnings:
            print(f"  warn   {w}")
        if not f.errors and not f.warnings:
            print("  clean")
        elif not f.errors:
            print(f"  no errors ({len(f.warnings)} warnings)")

    return 1 if (f.errors or (args.strict and f.warnings)) else 0


if __name__ == "__main__":
    sys.exit(main())
