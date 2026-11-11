#!/usr/bin/env python3
"""Una sesión real de Claude Code en una terminal virtual, grabada en asciicast v2, para el video de uso.

    python3 uso/sesion.py <toma> arrancar <carpeta de trabajo>   arranca Claude Code y queda escuchando
    python3 uso/sesion.py <toma> texto "…"                       escribe como una persona (no pulsa Enter)
    python3 uso/sesion.py <toma> tecla enter|down|up|esc|tab|ctrl-c …
    python3 uso/sesion.py <toma> pantalla                        lo que muestra la terminal y cuánto lleva quieta

`<toma>` es la carpeta de la toma (uso/tomas/<familia>-<idioma>/): ahí quedan toma.cast, la carpeta de
configuración de Claude Code de esa sesión (config/, aparte de la de quien graba) y ctl/, por donde se le
dan las órdenes. Nada de eso va al repositorio. Claude Code arranca con un entorno limpio, el de una persona en
su terminal: solo pasan la ruta, el proxy, los certificados y la autenticación.
"""
import json, os, random, sys, threading, time
from pathlib import Path

COLS, ROWS = 120, 36
TECLAS = {"enter": "\r", "down": "\x1b[B", "up": "\x1b[A", "esc": "\x1b", "tab": "\t", "space": " ",
          "ctrl-c": "\x03", "shift-tab": "\x1b[Z", "left": "\x1b[D", "right": "\x1b[C", "bs": "\x7f"}
PASAN = ("PATH", "HOME", "HTTPS_PROXY", "HTTP_PROXY", "https_proxy", "http_proxy", "NO_PROXY", "no_proxy",
         "NODE_EXTRA_CA_CERTS", "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "ANTHROPIC_BASE_URL", "ANTHROPIC_API_KEY",
         "CLAUDE_SESSION_INGRESS_TOKEN_FILE", "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST", "CLAUDE_CODE_PROXY_RESOLVES_HOSTS",
         "GIT_CONFIG_COUNT")


def config_inicial(config: Path, carpeta: str) -> None:
    """La configuración de una persona que ya pasó la bienvenida: sin el asistente de primer uso, que
    pide conectarse a servicios que una grabación no necesita."""
    config.mkdir(parents=True, exist_ok=True)
    p = config / ".claude.json"
    d = json.loads(p.read_text()) if p.is_file() else {}
    d.update(hasCompletedOnboarding=True, theme="dark")
    d.setdefault("projects", {}).setdefault(carpeta, {"hasTrustDialogAccepted": False, "allowedTools": []})
    p.write_text(json.dumps(d))


def arrancar(toma: Path, carpeta: str) -> None:
    import pexpect, pyte
    ctl = toma / "ctl"
    ctl.mkdir(parents=True, exist_ok=True)
    config_inicial(toma / "config", carpeta)
    pantalla, t0, ultimo = pyte.Screen(COLS, ROWS), time.time(), [time.time()]
    flujo = pyte.ByteStream(pantalla)
    env = {k: v for k, v in os.environ.items() if k in PASAN or k.startswith(("GIT_CONFIG_KEY_", "GIT_CONFIG_VALUE_"))}
    env.update(LANG="C.UTF-8", TERM="xterm-256color", COLORTERM="truecolor", DISABLE_AUTOUPDATER="1",
               CLAUDE_CONFIG_DIR=str((toma / "config").resolve()))
    hijo = pexpect.spawn("claude", cwd=carpeta, env=env, dimensions=(ROWS, COLS))
    out = open(toma / "toma.cast", "w", encoding="utf-8")
    out.write(json.dumps({"version": 2, "width": COLS, "height": ROWS, "timestamp": int(t0), "env": {"TERM": "xterm-256color"}}) + "\n")
    candado = threading.Lock()

    def leer():
        while True:
            try:
                b = hijo.read_nonblocking(65536, timeout=0.2)
            except pexpect.TIMEOUT:
                continue
            except pexpect.EOF:
                break
            with candado:
                flujo.feed(b)
                out.write(json.dumps([round(time.time() - t0, 4), "o", b.decode("utf-8", "replace")]) + "\n")
                out.flush()
                ultimo[0] = time.time()
        (ctl / "fin").write_text("eof")

    threading.Thread(target=leer, daemon=True).start()
    while not (ctl / "fin").exists():
        cola = ctl / "cola"
        if cola.exists():
            orden = json.loads(cola.read_text(encoding="utf-8"))
            cola.unlink()
            if orden["tipo"] == "texto":
                for ch in orden["dato"]:
                    hijo.send(ch)
                    time.sleep(random.uniform(0.03, 0.08))
            else:
                hijo.send(TECLAS[orden["dato"]])
        with candado:
            (ctl / "pantalla.txt").write_text("\n".join(l.rstrip() for l in pantalla.display)
                                              + f"\n--- quieta {time.time() - ultimo[0]:.0f} s · {time.time() - t0:.0f} s de sesión", encoding="utf-8")
        time.sleep(0.25)


def ordenar(toma: Path, tipo: str, dato: str) -> None:
    cola = toma / "ctl" / "cola"
    while cola.exists():
        time.sleep(0.1)
    cola.write_text(json.dumps({"tipo": tipo, "dato": dato}), encoding="utf-8")
    while cola.exists():
        time.sleep(0.1)
    time.sleep(0.3 + (len(dato) * 0.06 if tipo == "texto" else 0))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    toma, accion, resto = Path(sys.argv[1]), sys.argv[2], sys.argv[3:]
    if accion == "arrancar":
        arrancar(toma, str(Path(resto[0]).resolve()))
    elif accion == "texto":
        ordenar(toma, "texto", resto[0])
    elif accion == "tecla":
        for k in resto:
            ordenar(toma, "tecla", k)
    elif accion == "pantalla":
        print((toma / "ctl" / "pantalla.txt").read_text(encoding="utf-8"))
    else:
        print(__doc__)
        sys.exit(2)
