# /criterio-sales:pipeline-scan 

Los términos están vigentes y no hubo que registrar nada nuevo. Los 8 documentos de evidencia y el acta del comité ya estaban en la ficha y coinciden con los originales, así que no agregué nada.

# Qué cambió en el embudo · Comercial Control Andina · periodo 2026-10

**Entidad:** Comercial Control Andina (900000002) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.1.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender
Nada abierto en lo que procesa este comando.

## El resultado
| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/oportunidades-2026-10-01.csv` | 2026-10-01 | generico | 7 |
| `10-crm/oportunidades-2026-10-16.csv` | 2026-10-16 | generico | 7 |
| `10-crm/oportunidades-2026-11-03.csv` | 2026-11-03 | generico | 7 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 3 de fecha de cierre. **Evidencia en la ficha:** 8 documentos.

- **Etapa:** OPP-1303: Negociación → Compromiso
- **Fecha de cierre:** OPP-1304: 2026-12-10 → 2026-12-15; OPP-1306: 2026-10-30 → 2026-10-28; OPP-1307: 2026-11-30 → 2026-12-18

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
- ¿De qué CRM sale la exportación y qué columna trae cada dato? → Un CRM distinto de Salesforce y HubSpot, con cabeceras en español; se registró el mapeo de monto (Valor estimado), cierre (Fecha estimada de cierre) y última actividad (Última gestión).
- ¿Las fechas van día/mes o mes/día? → Día/mes: hay fechas con el día mayor que 12, como 22/10/2026.
- ¿Qué periodo se revisa? → 2026-10: el acta del comité compromete el pronóstico de octubre.
- ¿Cuántos días sin actividad detienen una oportunidad y cuántas veces puede correrse un cierre? → 30 días y 2 veces, los valores por omisión de la configuración de ejemplo; ningún documento dice otros.

## Fuentes
- Sin documentos citados.

La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 0 hallazgos. La salida está en `estado-comercial/900000002-comercial-control-andina/corridas/salida-pipeline-scan.md`. En el texto que muestra el motor, "Sin documentos citados" está en la sección de fuentes aunque la ficha sí tiene citas.