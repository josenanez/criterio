# /criterio-legal:legal-setup legal/88612904-4-distribuidora-del-ybytyruzu-sintetica

Fidel quedó instalado para Distribuidora del Ybytyruzú Sintética (RUC 88612904-4, Paraguay, PYG). Procesé 29 documentos de 6 contratos y armé una ficha por contrato; el motor no reportó problemas en ninguna.

- **Configuración:** está en `.criterio/legal/88612904-4/config.json` y el motor la validó. El estado se guarda en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica`.
- **Respuestas que tomé de los documentos:**
  - La matriz de atribuciones ya existía en `00-referencia/`.
  - Avisos con 60 días antes de un vencimiento y 30 antes de un preaviso.
  - El certificado de la contraparte puede tener hasta 30 días.
  - No es entidad pública.
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez el 2026-10-06 (términos 1.5). El comprobante está en `.criterio/terminos/`.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt` en la raíz porque nadie lo autorizó.
- **Señales del motor:** encontró 5. El calendario de abajo muestra solo el vencimiento. Las otras cuatro se ven con `/criterio-legal:authority-check`, `/criterio-legal:contract-execution` y `/criterio-legal:contract-register`:
  - 1 firma sin facultad
  - 1 pago después de la terminación
  - 1 garantía que vence antes de lo que exige el contrato
  - 1 diferencia con el registro
- **Pregunta para ti:** los certificados de CTR-4502 (Empaques de Luque) y CTR-4503 (Centro Comercial del Sur) traen el mismo RUC, 88450003-9. ¿Es correcto?
- **Desviación del procedimiento:** una vez usé `cd` y `cat` para procesar los contratos, cuando el comando pide no hacerlo. Las llamadas siguientes las hice con rutas absolutas.

# Vencimientos, preavisos y obligaciones · Distribuidora del Ybytyruzú Sintética · al 2026-10-06

**Entidad:** Distribuidora del Ybytyruzú Sintética (88612904-4) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.6.3 · **Comando:** `obligations-calendar`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un contrato vence dentro de los días configurados y no tiene una decisión registrada de renovar o terminar (`contract_expiring`) | CTR-4503: vence el 2026-11-25, en 50 días, sin decisión de renovar o terminar | 1.980.000.000,00 | — | 50 | `contratos/CTR-4503-centro-comercial-del-sur-sintetica-s-a/10-contrato/contrato.md` |

## El resultado

| Fecha | Contrato | Qué | Días | Evidencia |
|---|---|---|---|---|
| 2026-09-30 | CTR-4501 | obligación OBL-3 · Reporte de operaciones del periodo al oficial de cumplimiento | -6 | `contratos/CTR-4501-logistica-del-chaco-sintetica-s-a/40-ejecucion/OBL-3_reporte-de-operaciones-al-oficial-de-cum.md` |
| 2026-11-20 | CTR-4505 | terminación | 45 | — |
| 2026-11-20 | CTR-4505 | obligación OBL-2 · Informe final y acta de liquidación | 45 | — |
| 2026-11-25 | CTR-4503 | terminación | 50 | — |
| 2026-11-25 | CTR-4503 | obligación OBL-2 · Informe final y acta de liquidación | 50 | — |

Entre 30 días atrás y 90 adelante. La decisión de renovar o terminar es de una persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `contratos/CTR-4503-centro-comercial-del-sur-sintetica-s-a/10-contrato/contrato.md`

---

**Cuándo vuelvo:** no hay revisión automática programada, porque crearla exige un sí explícito y en esta sesión nadie lo dio. Para correr la revisión diaria a mano: `/criterio-legal:legal-wake`.

La corrida quedó registrada como `2026-10-06-legal-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.