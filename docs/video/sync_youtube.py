#!/usr/bin/env python3
"""Sube a YouTube el catálogo que genera scripts/youtube.py: el título, la descripción con sus
capítulos y las etiquetas de cada video, en el idioma del video y su traducción al otro: los videos en
español llevan su traducción al inglés, y los que están en inglés, al español.

    python3 docs/video/sync_youtube.py --secreto client_secret.json            muestra qué cambiaría; no sube nada
    python3 docs/video/sync_youtube.py --secreto client_secret.json --aplicar  sube los cambios
    python3 docs/video/sync_youtube.py ... --solo EXM3bMVS09s                  solo ese video

Lo corre el dueño del canal en su equipo. La primera vez abre el navegador para que autorice el acceso
(OAuth 2.0, alcance youtube.force-ssl); el permiso queda en ~/.config/criterio-youtube/token.json, fuera
del repositorio, y `client_secret.json` es el que se descarga de Google Cloud Console para una
«aplicación de escritorio». Ninguno de los dos se versiona.

Sin --aplicar no escribe nada: trae cada video y muestra, campo por campo, lo que está publicado y lo
que quedaría, y cómo quedaría el orden de cada lista de reproducción de `listas` en videos.json. Con --aplicar sube solo los videos que cambian, conservando la categoría, y la traducción
al inglés de los demás idiomas que ya tenga el video. Cada actualización cuesta 50 unidades de la cuota
diaria de la API (10.000 por defecto); cada consulta, una.

    pip install google-api-python-client google-auth-oauthlib
"""
from __future__ import annotations

import argparse
import difflib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CATALOGO = AQUI / "youtube_catalog.json"
TOKEN = Path.home() / ".config" / "criterio-youtube" / "token.json"
ALCANCE = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def credenciales(secreto: Path):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    cred = Credentials.from_authorized_user_file(str(TOKEN), ALCANCE) if TOKEN.exists() else None
    if cred and cred.valid:
        return cred
    renovado = False
    if cred and cred.expired and cred.refresh_token:
        try:
            cred.refresh(Request())
            renovado = True
        except Exception:
            # Una app en modo de prueba de Google vence su permiso a los siete días: se pide de nuevo.
            renovado = False
    if not renovado:
        cred = InstalledAppFlow.from_client_secrets_file(str(secreto), ALCANCE).run_local_server(port=0)
    TOKEN.parent.mkdir(parents=True, exist_ok=True)
    TOKEN.write_text(cred.to_json(), encoding="utf-8")
    TOKEN.chmod(0o600)
    return cred


def deseado(actual: dict, v: dict, idioma: str, otros: list[str]) -> tuple[dict, dict]:
    sn = dict(actual["snippet"])
    for k in ("thumbnails", "localized", "channelTitle", "publishedAt", "channelId", "liveBroadcastContent"):
        sn.pop(k, None)
    sn.update(title=v[idioma]["title"], description=v[idioma]["description"], tags=v["tags"],
              defaultLanguage=idioma, defaultAudioLanguage=idioma)
    loc = dict(actual.get("localizations") or {})
    for l in otros:
        loc[l] = {"title": v[l]["title"], "description": v[l]["description"]}
    return sn, loc


def diferencias(actual: dict, sn: dict, loc: dict) -> list[str]:
    out = []
    a = actual["snippet"]
    for campo in ("title", "description", "tags", "defaultLanguage", "defaultAudioLanguage"):
        antes, despues = a.get(campo), sn.get(campo)
        if antes == despues:
            continue
        if campo == "description":
            d = difflib.unified_diff((antes or "").splitlines(), despues.splitlines(), "publicado", "catálogo", lineterm="", n=1)
            out.append("  description:\n    " + "\n    ".join(d))
        else:
            out.append(f"  {campo}:\n    - {antes!r}\n    + {despues!r}")
    for l, x in loc.items():
        antes = (actual.get("localizations") or {}).get(l)
        if antes != x:
            out.append(f"  localización {l}: {'nueva' if not antes else 'cambia'} · título {x['title']!r}")
    return out


def ordenar_listas(yt, listas: dict, videos: dict, aplicar: bool, HttpError) -> int:
    """Cada lista de reproducción, en el orden del catálogo: lo que falta se agrega en su lugar y lo que
    está en otro lugar se mueve. Lo que la lista tiene y el catálogo no —un video viejo— queda al final
    y se nombra; no se quita. Cada movimiento o inserción cuesta 50 unidades de la cuota."""
    fallas = 0
    for idioma, lista in listas.items():
        if not lista.get("id"):
            print(f"\nLista en {idioma}: sin identificador en videos.json (`listas.{idioma}`); no se ordena")
            continue
        items, token = [], None
        while True:
            r = yt.playlistItems().list(playlistId=lista["id"], part="snippet", maxResults=50, pageToken=token).execute()
            items += r.get("items", [])
            token = r.get("nextPageToken")
            if not token:
                break
        actual = [x["snippet"]["resourceId"]["videoId"] for x in items]
        de = {x["snippet"]["resourceId"]["videoId"]: x for x in items}
        deseado = lista["videos"]
        sobran = [v for v in actual if v not in deseado]
        if actual[:len(deseado)] == deseado:
            print(f"\n= Lista en {idioma}: en orden" + (f" · al final, fuera del catálogo: {', '.join(sobran)}" if sobran else ""))
            continue
        print(f"\n~ Lista en {idioma}:")
        for pos, vid in enumerate(deseado):
            nombre = videos.get(vid, {}).get("video", vid)
            if vid in de:
                if actual.index(vid) == pos:
                    continue
                print(f"  {pos + 1:>2}. {nombre} ({vid}): se mueve desde el lugar {actual.index(vid) + 1}")
                cuerpo = {"id": de[vid]["id"], "snippet": {"playlistId": lista["id"], "position": pos,
                                                           "resourceId": {"kind": "youtube#video", "videoId": vid}}}
                hacer = lambda c=cuerpo: yt.playlistItems().update(part="snippet", body=c).execute()  # noqa: E731
            else:
                print(f"  {pos + 1:>2}. {nombre} ({vid}): se agrega")
                cuerpo = {"snippet": {"playlistId": lista["id"], "position": pos, "resourceId": {"kind": "youtube#video", "videoId": vid}}}
                hacer = lambda c=cuerpo: yt.playlistItems().insert(part="snippet", body=c).execute()  # noqa: E731
            actual = [v for v in actual if v != vid]
            actual.insert(pos, vid)
            if aplicar:
                try:
                    r = hacer()
                    de[vid] = r
                except HttpError as e:
                    print(f"     ✗ {e}")
                    fallas += 1
        if sobran:
            print(f"  al final, fuera del catálogo (no se quitan): {', '.join(sobran)}")
    return fallas


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--secreto", type=Path, required=True, help="client_secret.json de la aplicación de escritorio")
    ap.add_argument("--aplicar", action="store_true", help="sube los cambios; sin esto solo los muestra")
    ap.add_argument("--solo", action="append", default=[], help="el identificador de un video (se puede repetir)")
    a = ap.parse_args()

    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError

    cat = json.loads(CATALOGO.read_text(encoding="utf-8"))
    videos = {i: v for i, v in cat["videos"].items() if not a.solo or i in a.solo}
    yt = build("youtube", "v3", credentials=credenciales(a.secreto))
    publicados = {}
    ids = list(videos)
    for k in range(0, len(ids), 50):
        r = yt.videos().list(id=",".join(ids[k:k + 50]), part="snippet,localizations").execute()
        publicados.update({x["id"]: x for x in r.get("items", [])})

    cambian, fallas = 0, 0
    for i, v in videos.items():
        if i not in publicados:
            print(f"✗ {i} ({v['video']}): no está en el canal o la cuenta no es su dueña")
            fallas += 1
            continue
        sn, loc = deseado(publicados[i], v, v["idioma"], v["localizaciones"])
        d = diferencias(publicados[i], sn, loc)
        if not d:
            print(f"= {i} ({v['video']}): al día")
            continue
        cambian += 1
        print(f"~ {i} ({v['video']}):\n" + "\n".join(d))
        if a.aplicar:
            try:
                yt.videos().update(part="snippet,localizations", body={"id": i, "snippet": sn, "localizations": loc}).execute()
                print("  subido")
            except HttpError as e:
                print(f"  ✗ no se subió: {e}")
                fallas += 1
    print(f"\n{cambian} de {len(videos)} cambian" + ("" if a.aplicar else " · nada se subió: agrega --aplicar para subirlos")
          + (f" · {fallas} con error" if fallas else ""))
    if not a.solo:
        fallas += ordenar_listas(yt, cat.get("listas") or {}, cat["videos"], a.aplicar, HttpError)
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
