#!/usr/bin/env python3
"""El camino corto del reloj (decisión 0032): una sola llamada al motor que, si no toca nada, deja la
corrida registrada, y que despierta al agente cuando sí toca.

    python3 tests/reloj_corto.py

Sobre el material de la entidad de Business Central de la CFO, en una carpeta temporal: con Clara
recién configurada toca el barrido; después de registrarlo hoy, no toca nada, y el motor registra la
corrida del reloj sin que el agente dé otro paso.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MOTOR = RAIZ / "plugins" / "criterio-finance" / "scripts" / "finanzas.py"
MATERIAL = RAIZ / "tests" / "criterio-cfo" / "material" / "bc-mx"


def correr(raiz: Path, *args) -> dict:
    r = subprocess.run([sys.executable, str(MOTOR), *args], cwd=raiz, capture_output=True, text=True)
    return json.loads(r.stdout)


def main() -> int:
    clave = json.loads((MATERIAL / "clave.json").read_text(encoding="utf-8"))
    hoy = clave["hoy"]
    fallas = []

    def ok(que, real, esperado):
        if real != esperado:
            fallas.append(que)
        print(f'{"  ok  " if real == esperado else " FALLA"} {que}' + ("" if real == esperado else f": {real!r} ≠ {esperado!r}"))

    with tempfile.TemporaryDirectory() as t:
        raiz = Path(t)
        shutil.copytree(MATERIAL / "finanzas", raiz / "finanzas")
        cfg = raiz / ".criterio" / "finanzas" / clave["config"]["clara"]["entity"]["id"] / "config.json"
        cfg.parent.mkdir(parents=True)
        cfg.write_text(json.dumps(clave["config"]["clara"], ensure_ascii=False), encoding="utf-8")
        correr(raiz, "aceptar", "--config", str(cfg), "--por", "Prueba", "--today", hoy)
        d = correr(raiz, "despertar", "--what", "finance-wake", "--registrar", "--today", hoy)
        ok("sin --config encuentra la configuración del agente en la carpeta", len(d["entidades"]), 1)
        ok("recién configurada, toca algo y el agente sigue", d["callado"], False)
        for que in ("close-scan", "close-status"):
            correr(raiz, "corrida", "--config", str(cfg), "--what", que, "--today", hoy)
        d = correr(raiz, "despertar", "--what", "finance-wake", "--registrar", "--today", hoy)
        e = d["entidades"][0]
        ok("con lo de hoy ya corrido, no toca nada", d["callado"], True)
        ok("y el motor deja la corrida del reloj registrada", e.get("registrado", "").startswith(f"{hoy}-finance-wake"), True)
        ok("con la línea que el agente muestra", bool(d.get("linea")), True)
        estado = raiz / clave["config"]["clara"]["paths"]["state"]
        ok("la corrida queda donde Rostrum la lee", (estado / "corridas" / f'{e["registrado"]}.md').is_file(), True)
    print()
    print(f"{len(fallas)} falla(s)" if fallas else "todo pasa")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
