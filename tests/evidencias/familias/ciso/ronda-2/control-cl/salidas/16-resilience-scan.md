# /criterio-resilience:resilience-scan 

Los incidentes, la revisión y las pruebas ya estaban en la ficha del periodo y coinciden con los documentos, así que no hubo nada nuevo que llevar. El inventario marca `80-revisiones/INC-ACS-101_revision.md` como fuera de lugar, porque el motor sugiere `70-incidentes/`. Es una observación de orden, no una señal.

# Qué cambió en la respuesta · Aseguradora Control Sintética · periodo 2026-10

**Entidad:** Aseguradora Control Sintética (966778890) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Amparo, versión 0.2.0 · **Comando:** `resilience-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**En la ficha:** 1 incidentes, 1 revisiones posteriores y 5 pruebas.

**Excluidos por omisión:** 3 archivos —credenciales, llaves o respaldos— que el motor no abre: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

- ¿Plazos de contención y de revisión posterior? → Tomados de la política de respuesta a incidentes v2, §5 y §7: crítica 6 h, alta 24 h, media 72 h, baja 168 h; revisión a 15 días. Propuesta aceptada en la prueba sin interfaz.
- ¿Matriz de notificaciones y calendario de continuidad? → Columnas reconocidas tal cual en 00-referencia/ (4 destinatarios; 5 pruebas); sin mapeo en columns.
- ¿Dejo la marca _CRITERIO_SEGURIDAD.txt en la raíz? → Respuesta sugerida: sí. El motor falló (KeyError 'ciso' en raiz.py) y la marca no quedó.
- ¿Acepta los términos 1.3? → Sí: José Francisco Ñáñez, 2026-10-15.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-04 (families/criterio-ciso/FUENTES.es.md)

La salida quedó en `corridas/salida-resilience-scan.md` y la corrida se registró como `2026-10-15-resilience-scan-1`.