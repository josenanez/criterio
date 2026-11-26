# criterio-cro · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada vez,
byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el generador al
sembrar cada defecto; el motor no la ve. Los nombres, las empresas y los documentos son inventados.

## Las entidades

| Carpeta del material | País | Industria | Lengua de los documentos | Señales esperadas |
|---|---|---|---|---:|
| `banca-co` | Colombia | banca | español | 34 |
| `seguros-pe` | Perú | seguros | español | 23 |
| `cooperativa-br` | Brasil | cooperativa de crédito | portugués | 23 |
| `control-co` | Colombia | banca | español | 0 |
| `control-br` | Brasil | cooperativa de crédito | portugués | 0 |

Cada una trae su carpeta de riesgos al 25 de noviembre de 2026, con octubre como el último periodo cerrado:
la declaración de apetito y la política de riesgo operacional en PDF, y la matriz de riesgos, los límites y
los indicadores clave en Excel; la exposición de octubre y los planes de acción en Excel; los valores de los
indicadores y sus acciones en Excel; la base de eventos de pérdida en Excel, y el acta del comité de riesgos
de octubre en PDF. La cooperativa de Brasil y su control traen los nombres de los archivos, las columnas y
los valores en portugués.

## Lo que se siembra, y la señal que tiene que levantar

La lista exacta está en la clave de cada entidad, en `esperado`. Las tres entidades sembradas traen las doce
señales: el banco, cada una tres veces, y la aseguradora y la cooperativa, dos; la declaración de apetito
vencida, una vez, porque cada entidad tiene una sola. Cada repetición va en su propia fila —otro límite, otro
indicador, otro evento—, y la tabla dice la primera.

| Agente | Lo que se siembra | Señal |
|---|---|---|
| Severo | La cartera vencida de consumo en 6,4 % con un límite máximo de 6 %, sin plan ni aprobación | `limit_breached_without_plan` |
| Severo | El límite de liquidez sin dueño | `limit_without_owner` |
| Severo | El límite de liquidez con su revisión del 30 de junio de 2026 | `limit_review_overdue` |
| Severo | Tesorería reporta su exposición el 18 de noviembre, con un plazo hasta el 10 | `exposure_report_late` |
| Severo | La continuidad del negocio, calificada alta, sin límite ni indicador | `risk_without_limit` |
| Severo | La declaración revisada por la junta el 28 de agosto de 2025, con revisión cada 12 meses | `appetite_statement_outdated` |
| Casandra | Las transacciones fraudulentas en 52, con una alerta en 40, y el acta sin acción | `kri_alert_without_action` |
| Casandra | La rotación del personal de crédito sin valor en octubre | `kri_not_reported` |
| Casandra | Un error de liquidación sin causa | `loss_event_incomplete` |
| Casandra | La caída del canal digital registrada 50 días después de descubierta, con un plazo de 30 | `loss_event_registered_late` |
| Casandra | Dos fraudes con tarjeta en canales en los últimos 12 meses | `loss_event_repeated` |
| Casandra | Una multa asociada a un riesgo que no está en la matriz | `loss_event_risk_unmapped` |

Las repeticiones: la cartera vencida de vivienda y la comercial por encima de su límite; la concentración
sectorial y el descalce de plazos sin dueño; la exposición en moneda extranjera y las inversiones de baja
liquidez con la revisión vencida; los cupos de contraparte y las pérdidas por errores operativos reportados
tarde; el riesgo de tasa de interés y el de modelo, altos, sin límite ni indicador; los reclamos y los
incidentes de seguridad en alerta sin acción; dos indicadores sin valor; un evento sin monto y otro sin
proceso; dos registrados a los 45 y a los 60 días; los faltantes de efectivo en sucursales y los errores de
conciliación en tesorería, dos veces cada uno; y dos eventos con un riesgo que no está en la matriz.

## Lo que se parece a un defecto y no lo es

En todas las entidades, y sin nada más en las de control: un límite excedido con su plan de acción, tres
excedidos con el exceso aprobado en el acta del comité, un límite mínimo que la exposición supera por arriba,
un reporte que llega el último día del plazo, un límite que se revisa el mes que viene, un riesgo alto medido
solo por un indicador, un riesgo medio sin límite, dos indicadores en alerta con la acción en el acta, otro en
alerta con la acción en la tabla, otro justo fuera de su alerta en el sentido «menor es peor», un evento
registrado el último día del plazo, el mismo tipo de evento en otro proceso y dos eventos iguales con uno
fuera de la ventana de 12 meses. Ninguno puede levantar una señal.

## Lo que el material no prueba

- **La extracción.** El evaluador escribe la ficha con la extracción correcta, de la clave. Que el agente
  procese la declaración, el acta, los excesos aprobados y las acciones sobre los indicadores, y los
  registre bien, lo prueba la ronda con los agentes, desde la 0.2.0: [las rondas](../evidencias/familias/cro/RONDAS.md).
  Desde la ronda 2, cada aprobación y cada acción se califican por separado, campo por campo.
- **Las exportaciones reales** de las herramientas de gestión de riesgos: el material usa tablas con columnas
  en español y en portugués; el setup mapea las de cualquier exportación.
- **El texto del Capítulo XXXI de la Superintendencia Financiera y COSO ERM**: están por verificar, y no
  sostienen ninguna señal.
- **El juicio del área de riesgos**: si un exceso se aprueba, qué límite o umbral corresponde a un riesgo, y
  cómo se califica.
