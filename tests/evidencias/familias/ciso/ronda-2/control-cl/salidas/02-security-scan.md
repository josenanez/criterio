# /criterio-security:security-scan 

Términos vigentes (versión 1.3, aceptada por José Francisco Ñáñez el 2026-10-15). La ficha del periodo ya traía todos los documentos nuevos de `10-controles/`, `20-accesos/` y `30-terceros/`. Los revisé contra su texto y coinciden, así que no agregué nada. El borrador `A.8.28` sigue anotado como revisado, no como evidencia. Según el inventario, `80-revisiones/INC-ACS-101_revision.md` está fuera de lugar y iría en `70-incidentes/`.

# Qué cambió en la seguridad · Aseguradora Control Sintética · periodo 2026-10

**Entidad:** Aseguradora Control Sintética (966778890) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 0.2.0 · **Comando:** `security-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**En la ficha:** 13 evidencias de controles, 4 revisiones de acceso y 3 evaluaciones de terceros.

**Excluidos por omisión:** 3 archivos (credenciales, llaves o respaldos) que el motor no abre: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz? → seguridad/966778890-aseguradora-control-sintetica (la del argumento)
- ¿Entidad, identificación fiscal, país y moneda? → Aseguradora Control Sintética, 966778890, CL, CLP (tomado del nombre de la carpeta y de la notificación a la Comisión para el Mercado Financiero)
- ¿Qué columnas tiene la declaración de aplicabilidad? → Control, Nombre, Aplicable, Estado, Responsable, Periodicidad, Justificación (cabeceras estándar, sin mapeo)
- ¿Tabla de sistemas, terceros y riesgos? → Cabeceras estándar: sistema;revision_dias;criticidad;responsable / tercero;servicio;critico;evaluacion_dias / riesgo;descripcion;decision;aceptado_por;revision
- ¿Dónde guardo lo que encuentro? → estado-seguridad/966778890-aseguradora-control-sintetica
- ¿Dejo la marca _CRITERIO_SEGURIDAD.txt en la raíz? → Sí (respuesta sugerida), pero marcar-raiz falló con KeyError 'ciso' y la marca no quedó

## Fuentes

- Sin documentos citados.

La corrida quedó registrada como `2026-10-15-security-scan-1`, con 0 hallazgos. Dos cosas para revisar:
- La marca `_CRITERIO_SEGURIDAD.txt` no quedó en la raíz, porque `marcar-raiz` falló con `KeyError 'ciso'`. Es un error del motor, no de los documentos.
- Los tres `.gz` de `50-escaneos/` salieron como ilegibles en el inventario, pero eso es de la parte de vulnerabilidades, no de este comando.