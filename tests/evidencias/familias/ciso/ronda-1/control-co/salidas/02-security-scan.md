# /criterio-security:security-scan 

# Qué cambió en la seguridad · Cooperativa Control Sintética · periodo 2026-10

**Entidad:** Cooperativa Control Sintética (900777888) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Alexis, versión 0.1.0 · **Comando:** `security-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**En la ficha:** 13 evidencias de controles, 4 revisiones de acceso y 3 evaluaciones de terceros.

**Excluidos por omisión:** 3 archivos —credenciales, llaves o respaldos— que el motor no abre: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

- ¿Dejo la marca _CRITERIO_SEGURIDAD.txt en la carpeta de la entidad? → No (prueba sin interfaz; no se autorizó crear archivos en la carpeta)
- ¿Acepta los términos vigentes (versión 1.3)? → Sí, José Francisco Ñáñez

## Fuentes

- Sin documentos citados.

---
Notas de esta corrida, fuera del reporte:
- Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez, así que no registré una aceptación nueva.
- La ficha del periodo ya traía todos los documentos de `10-controles/`, `20-accesos/` y `30-terceros/`. El motor no encontró documentos sin llevar (`record_issues` vacío). No la modifiqué.
- El inventario marca `80-revisiones/INC-CTL-101_revision.md` como fuera de lugar. El motor dice que iría en `70-incidentes/`. No lo moví.
- La corrida quedó registrada como `2026-10-15-security-scan-2`.