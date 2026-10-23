# /criterio-legal:legal-setup legal/0990054321001-minera-condor

La instalación quedó lista y la corrida registrada. Esto es lo que le mostré a la persona; está igual en `estado-legal/0990054321001-minera-condor/corridas/salida-legal-setup.md`.

Soy Fidel. Proceso lo que tu empresa firmó y te digo qué vence, quién firmó con qué facultad y qué se pagó por fuera de lo pactado.

Fue una sesión de prueba sin interfaz. Nadie contestó preguntas, así que tomé las respuestas de los documentos y de tus instrucciones.

**Inventario** (`legal/0990054321001-minera-condor`)
- Hay 6 contratos en `contratos/` (CTR-401 a CTR-406).
- Están el registro de contratos y la matriz de atribuciones.
- No hay nada fuera de la estructura recomendada ni nada ilegible.

**Respuestas que tomé**
1. **Entidad:** Minera Cóndor, RUC 0990054321001, Ecuador, USD.
2. **Matriz de atribuciones:** la de `00-referencia/`.
3. **Avisos:** 60 días para vencimientos y 30 para preavisos.
4. **Certificado de la contraparte:** 30 días de antigüedad máxima.
5. **Estado:** `estado-legal/0990054321001-minera-condor`, fuera de los documentos.
6. **Festivos:** lista vacía. No inventé los de Ecuador. Si quieres que cuenten, dime las fechas.
7. **Marca `_CRITERIO_LEGAL.txt`:** no la dejé. Es lo único que se escribiría dentro de tus documentos y nadie lo autorizó. Si la quieres, dímelo.

**Términos (versión 1.2)**
Criterio produce borradores de trabajo, no decisiones ni asesoría. Procesa los documentos que usted le indique y dice lo que muestran; no sabe lo que se habló fuera de ellos. Puede equivocarse, y por eso cada dato viene con la cita del documento de donde salió: la verificación es suya. Sus documentos se procesan en la infraestructura de la plataforma de IA, no solo en su equipo. Cada versión se prueba antes de publicarse; garantía y responsabilidad: licencia Apache 2.0. Cada versión se acepta de nuevo y deja un comprobante en Markdown y PDF con su huella SHA-256. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-10-06, según tus instrucciones. El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-0.8.0-2026-10-06.md` (y su `.pdf`).

**Configuración:** `.criterio/legal/0990054321001/config.json`. El motor la validó sin problemas.

**Fichas:** convertí los 29 documentos y escribí 6 fichas en `estado-legal/0990054321001-minera-condor/contratos/`. No hubo `record_issues` y nada quedó sin procesar. Tres decisiones de lectura:
- Las contrapartes firman como «Representante de <empresa>» y así quedó el nombre del firmante.
- El informe final y el acta de liquidación vencen «a la terminación», así que les puse la fecha de terminación. En CTR-402 usé la del otrosí OT-1 (2027-12-31).
- Registré la decisión de renovar CTR-405 porque la toma el acta del comité del 2026-09-18.

**Señales que el motor calculó:** 4 en total.
- Una es de este calendario: un preaviso vencido, que aparece abajo.
- Las otras tres son de otros comandos, y el motor no dice a qué contratos corresponden:
  - 1 firma sin facultad.
  - 1 contrato sin la firma de las dos partes.
  - 1 garantía faltante.
- Se detallan con `/authority-check` y `/contract-execution`.

---

# Vencimientos, preavisos y obligaciones · Minera Cóndor · al 2026-10-06

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.8.0 · **Comando:** `obligations-calendar`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Pasó la fecha límite del preaviso de un contrato con renovación automática sin una decisión registrada (`renewal_notice_missed`) | CTR-401: el preaviso venció el 2026-10-01 sin decisión; el contrato se prorroga en sus términos el 2026-10-31 | — | — | 5 | `contratos/CTR-401-perforaciones-del-sur-s-a/10-contrato/contrato.md` |

## El resultado

| Fecha | Contrato | Qué | Días | Evidencia |
|---|---|---|---|---|
| 2026-09-30 | CTR-401 | obligación OBL-3 · Reporte de operaciones al oficial de cumplimiento | -6 | `contratos/CTR-401-perforaciones-del-sur-s-a/40-ejecucion/OBL-3_reporte-de-operaciones-al-oficial-de-cum.md` |
| 2026-10-01 | CTR-401 | límite del preaviso | -5 | — |
| 2026-10-31 | CTR-401 | terminación | 25 | — |
| 2026-10-31 | CTR-401 | obligación OBL-2 · Informe final y acta de liquidación | 25 | — |
| 2026-11-20 | CTR-405 | terminación | 45 | — |
| 2026-11-20 | CTR-405 | obligación OBL-2 · Informe final y acta de liquidación | 45 | — |
| 2026-12-31 | CTR-403 | terminación | 86 | — |
| 2026-12-31 | CTR-403 | obligación OBL-2 · Informe final y acta de liquidación | 86 | — |

Entre 30 días atrás y 90 adelante. La decisión de renovar o terminar es de una persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `contratos/CTR-401-perforaciones-del-sur-s-a/10-contrato/contrato.md`