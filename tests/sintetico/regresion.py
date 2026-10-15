# -*- coding: utf-8 -*-
"""La prueba de regresión del motor: cinco semanas de una organización, en cada cambio.

    python3 tests/sintetico/regresion.py verificar   # puerta: corre en una carpeta temporal
    python3 tests/sintetico/regresion.py publicar    # deja la corrida en tests/informes/regresion/

**Qué prueba.** El motor que calcula —extracción determinista, aritmética, umbrales y
alertas— sobre la misma organización sintética vista cinco semanas seguidas, escrita
cada semana de una forma distinta (ordenada, plana, revuelta, sin carpetas, ordenada).
Lo esperado se deriva de los hechos y no cambia con la forma de la carpeta: si el motor
coincide con la clave en los cinco cortes y los controles negativos quedan en cero, la
regla se sostiene. No mide al modelo de lenguaje (LLM); eso lo miden las rondas.

**Por qué es puerta.** La primera corrida de cinco cortes se hizo una vez, a mano, el
29 de septiembre. El código cambió después y nadie la volvió a correr: una cifra que no
se vuelve a medir en cada cambio deja de ser evidencia. Ahora corre con cada
verificación, y `publicar` guarda la corrida con su fecha y su commit, sin borrar las
anteriores.
"""
import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SIM = RAIZ / "tests" / "sintetico" / "simulador.py"
FIA = RAIZ / "tests" / "sintetico" / "fiabilidad.py"
DISPOSICIONES = ["referencia", "plana", "revuelta", "sin_carpeta", "referencia"]


def correr(carpeta: Path, salida: Path) -> list:
    org = carpeta / "org"
    cortes = []
    for dia, disp in enumerate(DISPOSICIONES, start=1):
        r = subprocess.run([sys.executable, str(SIM), str(org), "--dia", str(dia),
                            "--disposicion", disp], capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(f"simulador, día {dia}: {r.stderr.strip()[:300]}")
        r = subprocess.run([sys.executable, str(FIA), str(org)], capture_output=True, text=True,
                           env={**os.environ, "CRITERIO_INFORMES": str(salida)})
        clave = json.loads((org / "esperado.json").read_text(encoding="utf-8"))
        nombre = f"dia-{dia}-{clave.get('hoy')}.json"
        informe = json.loads((salida / nombre).read_text(encoding="utf-8"))
        informe["salida_fiabilidad"] = r.returncode
        cortes.append(informe)
    return cortes


def resumen(cortes: list) -> tuple:
    malos = []
    for c in cortes:
        t = c["totales"]
        ruido = {k: v for k, v in (c.get("controles") or {}).items() if v}
        print(f"  corte {c['dia']} · {c['disposicion']:<11} · {c['documentos']['total']:>4} docs · "
              f"{t['aciertos']:>4} aciertos · {t['falsos_positivos']} falsos+ · "
              f"{t['falsos_negativos']} falsos− · controles {'limpios' if not ruido else ruido}")
        if t["falsos_positivos"] or t["falsos_negativos"] or ruido or c.get("errores") \
                or not c.get("controles"):
            malos.append(c["dia"])
    return malos


def main() -> int:
    modo = sys.argv[1] if len(sys.argv) > 1 else "verificar"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        if modo == "publicar":
            commit = subprocess.run(["git", "-C", str(RAIZ), "rev-parse", "--short", "HEAD"],
                                    capture_output=True, text=True).stdout.strip() or "?"
            salida = RAIZ / "tests" / "informes" / "regresion" / f"{dt.date.today().isoformat()}-{commit}"
            salida.mkdir(parents=True, exist_ok=True)
        elif modo == "verificar":
            salida = tmp / "informes"
            salida.mkdir()
        else:
            print(__doc__)
            return 2
        cortes = correr(tmp, salida)
        malos = resumen(cortes)
        if modo == "publicar":
            (salida / "corrida.json").write_text(json.dumps({
                "ejecutada": dt.date.today().isoformat(),
                "commit": cortes[0]["commit"],
                "cortes": len(cortes),
                "coinciden": len(cortes) - len(malos),
            }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"  → {salida.relative_to(RAIZ)}")
    if malos:
        print(f"  FALLA · cortes que no coinciden con la clave: {malos}")
        return 1
    print(f"  OK    {len(cortes)} de {len(cortes)} cortes coinciden con la clave, controles negativos en cero")
    return 0


if __name__ == "__main__":
    sys.exit(main())
