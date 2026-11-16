#!/usr/bin/env python3
"""El setup en dos llamadas (decisión 0032, palanca 3): `arranque` antes de la primera pregunta y
`dejar-listo` después de la última, en cada agente del núcleo común.

    python3 tests/setup_corto.py

Sobre el primer material de cada familia, en una carpeta temporal: `arranque` encuentra la carpeta
de la entidad, trae su inventario, los términos tal cual —sin esperar a la configuración— y la
configuración de ejemplo; con la configuración de la clave escrita, `dejar-listo` prepara el estado,
la valida, registra la aceptación y deja la marca de la carpeta, todo en una llamada.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MOTOR = {"criterio-finance": "finanzas.py", "criterio-budget": "finanzas.py", "criterio-treasury": "finanzas.py",
         "criterio-legal": "legal.py", "criterio-compliance": "legal.py", "criterio-assistant": "asistente.py",
         "criterio-sales": "ventas.py", "criterio-revenue": "ventas.py", "criterio-security": "seguridad.py",
         "criterio-vulnerability": "seguridad.py", "criterio-resilience": "seguridad.py"}
FAMILIAS = ("cfo", "clo", "cco", "ciso", "ea")


def correr(raiz: Path, motor: Path, *args) -> tuple[int, dict]:
    r = subprocess.run([sys.executable, str(motor), *args], cwd=raiz, capture_output=True, text=True)
    try:
        return r.returncode, json.loads(r.stdout)
    except json.JSONDecodeError:
        return r.returncode, {"_salida": r.stdout[-400:], "_error": r.stderr[-400:]}


def main() -> int:
    agentes = {a["id"]: a for a in json.loads((RAIZ / "plugins/criterio-server/scripts/agentes.json")
                                               .read_text(encoding="utf-8"))["agentes"]}
    fallas = []

    def ok(que, real, esperado):
        if real != esperado:
            fallas.append(que)
        print(f'{"  ok  " if real == esperado else " FALLA"} {que}' + ("" if real == esperado else f": {real!r} ≠ {esperado!r}"))

    for fam in FAMILIAS:
        base = RAIZ / "tests" / f"criterio-{fam}" / "material"
        material = sorted(d for d in base.iterdir() if (d / "clave.json").is_file())[0]
        clave = json.loads((material / "clave.json").read_text(encoding="utf-8"))
        for ag, cfg in (clave.get("config") or {}).items():
            a = agentes[ag]
            motor = RAIZ / "plugins" / a["plugin"] / "scripts" / MOTOR[a["plugin"]]
            with tempfile.TemporaryDirectory() as t:
                raiz = Path(t)
                for d in material.iterdir():
                    if d.is_dir() and not d.name.startswith("estado-"):
                        shutil.copytree(d, raiz / d.name)
                docs = raiz / cfg["paths"]["documents"]
                _, r = correr(raiz, motor, "arranque", "--docs", str(raiz))
                ok(f"{fam} · {ag}: arranque elige la carpeta de la entidad", r.get("elegida"), str(docs.resolve()))
                ok(f"{fam} · {ag}: con su inventario, los términos y la configuración de ejemplo",
                   (bool(r.get("inventario")), bool((r.get("terminos") or {}).get("en_corto")), bool(r.get("ejemplo"))),
                   (True, True, True))
                # La carpeta de la configuración: la identificación de la entidad, o el nombre de su carpeta (la EA).
                ruta = raiz / ".criterio" / a["area"] / (cfg["entity"].get("id") or docs.name) / "config.json"
                ruta.parent.mkdir(parents=True)
                ruta.write_text(json.dumps(cfg, ensure_ascii=False), encoding="utf-8")
                codigo, r = correr(raiz, motor, "dejar-listo", "--config", str(ruta), "--por", "Prueba", "--marcar",
                                   "--entidad", cfg["entity"]["name"], "--today", clave["hoy"])
                ok(f"{fam} · {ag}: dejar-listo valida, acepta los términos y marca la carpeta en una llamada",
                   (codigo, r.get("ok"), bool((r.get("terminos") or {}).get("aceptado")), bool((r.get("marca") or {}).get("ok")),
                    (raiz / cfg["paths"]["state"] / "corridas").is_dir()),
                   (0, True, True, True, True))
    print()
    print(f"{len(fallas)} falla(s)" if fallas else "todo pasa")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
