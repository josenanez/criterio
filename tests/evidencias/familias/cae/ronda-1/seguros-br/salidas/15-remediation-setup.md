# /criterio-remediation:remediation-setup auditoria/31452078000190-seguradora-atlantica-sintetica

Soy Remedios. Llevo cada hallazgo hasta su cierre, con su evidencia; no cierro nada ni acepto riesgos.

Remedios está instalada para Seguradora Atlântica Sintética (CNPJ 31452078000190). Procesé los 5 documentos de seguimiento y el cálculo de noviembre dio 3 señales.

**Carpeta:** solo había una candidata, `auditoria/31452078000190-seguradora-atlantica-sintetica`. Ya tenía la marca `_CRITERIO_AUDITORIA.txt`, así que no volví a preguntar por ella.

**Respuestas que tomé** (casi todas ya estaban en el setup de Prudencia):
- **Entidad:** Seguradora Atlântica Sintética, CNPJ 31452078000190, Brasil (BRL).
- **Periodo:** 2026-11.
- **Veces que se puede correr la fecha de un plan:** 2. La metodología, en «Seguimiento», dice «hasta dos veces».
- **Quién valida un cierre:** auditoría, con la evidencia de la implementación. Lo dice la misma sección de la metodología.
- **Alta dirección y consejo:** salen de las columnas «Discutido alta dirección» y «Escalado consejo» de `riesgos_aceptados.xlsx`. La configuración no tiene un campo para nombrarlos, así que no inventé ninguno.
- **Publicar en Rostrum:** no.
- **Dónde guardo lo que encuentro:** `estado-auditoria/31452078000190-seguradora-atlantica-sintetica`.

**Términos:** mostré los términos de la versión 1.6 tal cual y quedaron aceptados por José Francisco Ñáñez el 2026-11-24. El comprobante está en `.criterio/terminos/aceptacion-criterio-remediation-0.1.0-2026-11-24.md` y en el `.pdf` del mismo nombre.

**Configuración:** quedó en `.criterio/seguimiento/31452078000190/config.json`.

**Cambios sugeridos en la estructura (no moví nada):**
- `informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/`.
- `riesgos_aceptados.xlsx` iría en `10-plan/`.

**Lo que se llevó a la ficha de 2026-11:**
- La evidencia de H-20, con fecha 2025-09-12.
- La explicación del atraso de H-03, con fecha 2026-10-01.
- El hallazgo RF-01 del informe del revisor fiscal.

**Las 3 señales:**
- Un cierre sin evidencia; el detalle lo da `/criterio-remediation:closure-check`.
- Un riesgo aceptado sin escalar; el detalle lo da `/criterio-remediation:committee-brief`.
- La fecha de H-03 se corrió más veces de las permitidas; está en el reporte de abajo.

# Los planes contra su fecha · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `action-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La fecha de un plan se corrió más veces de las que permite la metodología (`due_date_extended_repeatedly`) | H-03 · Cuentas privilegiadas sin revisión trimestral: su fecha se corrió 3 veces y la metodología permite 2 | — | Gerencia de tecnología | — | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |

## El resultado

**Reprogramaciones que permite la metodología:** 2.

| Hallazgo | Trabajo | Prioridad | Responsable | Fecha | Reprogramaciones | Evidencias |
|---|---|---|---|---|---|---|
| H-01 | TR-01 | Alta | Gerencia de crédito | 2026-12-31 | 0 | 0 |
| H-02 | TR-01 | Media | Gerencia de garantías | 2026-12-15 | 0 | 0 |
| H-03 | TR-02 | Media | Gerencia de tecnología | 2026-09-30 | 3 | 0 |
| RF-01 | — | Media | Gestión humana | 2026-12-31 | 0 | 0 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-seguimiento/registro_hallazgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. La tarea programada necesita que alguien diga que sí, y en esta sesión nadie respondió. Para correrlo a mano: `/criterio-remediation:remediation-wake`.

La corrida quedó registrada como `2026-11-24-remediation-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.