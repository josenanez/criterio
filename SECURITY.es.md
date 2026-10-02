# Seguridad

[English](SECURITY.md)

## Cómo reportar una vulnerabilidad

**No abras un issue público.** Usa el reporte privado de GitHub: pestaña **Security** de
este repositorio → **Report a vulnerability**. Solo el mantenedor lo ve.

Incluye qué versión del plugin (`/plugin` → Installed), qué comando, y cómo reproducirlo.
Recibirás acuse en un plazo razonable; no hay un acuerdo de nivel de servicio.

## Qué se considera vulnerabilidad aquí

- Un comando o un hook que lee, escribe o envía algo fuera de las carpetas que la persona
  configuró.
- Un script que ejecuta contenido de un documento como si fuera una instrucción.
- Cualquier camino por el que datos de un proyecto terminen en un lugar que la persona
  no eligió.

## Lo que Criterio hace en tu equipo

Los plugins instalan *hooks* de Claude Code que corren `scripts/rastro.py` con Python en tu
máquina: registran cada corrida en `.criterio/corridas/` dentro de tu carpeta, y bloquean
el lanzamiento de subagentes cuando la configuración lo pide. No hacen llamadas de red.
Los scripts usan solo la librería estándar de Python. Revísalos antes de instalar: son
texto.
