# 0037 · La familia CTO: la tecnología, con dos agentes sobre los cambios y el servicio, y sobre los activos y los proveedores

**Fecha:** 2026-11-26 · **Estado:** aceptada: los nombres y la estructura, por José el 2026-11-26. Cada fuente se verifica una a una (abajo, con la fecha de cada verificación).

## Contexto

José Francisco Ñáñez pidió el 26 de noviembre de 2026 avanzar con la siguiente familia; de las que faltan
—COO, CTO, secretaría de la junta y estrategia—, la CTO va primero.

La CISO ya cubre la seguridad: los controles y su evidencia, las vulnerabilidades y la resiliencia, con los
incidentes de seguridad ([decisión 0023](0023-la-familia-ciso.md)). La CTO toma de la tecnología lo que vive en documentos y
no es seguridad:

- **los cambios y el servicio**: cada cambio en producción con su aprobación, cada incidente mayor con su
  causa y cada servicio contra el nivel que se le prometió al negocio;
- **los activos y los proveedores**: cada activo con su dueño y su soporte, cada licencia contra su uso,
  cada proveedor contra su nivel de servicio y la nube contra su presupuesto.

| Marco | Qué aporta | Estado de la fuente |
|---|---|---|
| ISO/IEC 20000-1:2018 · Gestión del servicio, parte 1 | Los requisitos de un sistema de gestión del servicio: el diseño, la transición, la entrega y la mejora de los servicios | Verificado el 2026-11-26 en iso.org: tercera edición, septiembre de 2018, revisada y confirmada en 2023, con la enmienda 1 de 2024. **Por verificar:** el texto de sus cláusulas de cambios, incidentes y niveles de servicio |
| ISO/IEC 19770-1:2017 · Gestión de activos de TI | Los requisitos de un sistema de gestión de activos de TI, para todo tipo de activo | Verificado el 2026-11-26 en iso.org: tercera edición, diciembre de 2017, revisada y confirmada en 2024 |
| ITIL 4 · La práctica de habilitación del cambio | Maximizar los cambios exitosos: evaluar su riesgo, autorizarlos y llevar el calendario de cambios | Verificado el 2026-11-26 en su descripción, citada por AWS. **Por verificar:** la guía de la práctica, de PeopleCert |
| COBIT 2019 · BAI06 y APO10 | Los cambios de TI gestionados y aceptados; la gestión de los proveedores | Verificado el 2026-11-26 en la comparación de ISACA con COBIT 5. **Por verificar:** el texto de cada objetivo |
| Colombia · Superintendencia Financiera, Circular Externa 005 de 2019 | La nube en una entidad vigilada: el riesgo en el SARO, las cláusulas del contrato, la continuidad y el aviso a la Superintendencia 15 días antes de procesar | Verificado el 2026-11-26 en la copia compilada del normograma de Colpensiones. Agrega el capítulo VI al título I de la parte I de la Circular Básica Jurídica |
| Perú y Brasil | La norma de la SBS sobre la tecnología y la nube y la Resolución CMN 4.893 | **Por verificar** |

## Decisión

**Criterio CTO · La tecnología.** Dos agentes y Rostrum, como en las demás familias:

| Agente | Plugin | Lo que hace |
|---|---|---|
| **Fausto**, del latín *faustus*, el que trae buena fortuna: cada cambio que sale bien | `criterio-changes` | Contrasta cada cambio en producción con su aprobación y cada despliegue con su cambio, cada incidente mayor con su problema y su causa, y cada servicio con el nivel que acordó con el negocio. Señala el cambio sin aprobar, el de emergencia sin su revisión, el despliegue sin cambio, el cambio fallido sin revisión, el incidente mayor sin causa y el servicio por debajo de su nivel. |
| **Domingo**, del latín *dominicus*, el del dueño: cada activo con quien responde por él | `criterio-assets` | Contrasta el inventario de activos con sus dueños y con el soporte del fabricante, las licencias con su uso, las facturas de cada proveedor con su nivel de servicio y la factura de la nube con su presupuesto. Señala el activo sin dueño, el que perdió el soporte, la licencia que falta y la que sobra, el incumplimiento de un proveedor sin su crédito y la nube por encima de su presupuesto. |

### Las señales que calcularía el código

| Agente | Señal | Cuándo |
|---|---|---|
| Fausto | `change_without_approval` | Un cambio se implementó sin la aprobación de su autoridad de cambio, o antes de ella |
| Fausto | `emergency_change_without_review` | Un cambio de emergencia no tiene su revisión posterior en el plazo de la política |
| Fausto | `deployment_without_change` | Un despliegue en producción no corresponde a ningún cambio registrado |
| Fausto | `failed_change_without_review` | Un cambio fallido o revertido no tiene su revisión posterior |
| Fausto | `major_incident_without_problem` | Un incidente mayor no tiene un registro de problema con su causa en el plazo de la política |
| Fausto | `service_below_level` | Un servicio quedó por debajo del nivel acordado en el periodo: su disponibilidad o su tiempo de solución |
| Domingo | `asset_without_owner` | Un activo del inventario no tiene dueño |
| Domingo | `asset_out_of_support` | Un activo en producción pasó la fecha de fin de soporte de su fabricante sin una excepción aprobada |
| Domingo | `license_shortfall` | Las instalaciones o los usuarios de un software superan las licencias compradas |
| Domingo | `license_unused` | Las licencias pagadas sin uso superan el umbral de la política |
| Domingo | `vendor_breach_without_credit` | Un proveedor incumplió su nivel de servicio y su factura no trae el crédito que pacta el contrato |
| Domingo | `cloud_over_budget` | La factura de la nube del mes supera su presupuesto más la tolerancia de la política |

**Los plazos, los niveles de servicio, los umbrales y quién aprueba cada cambio los fija la organización**,
en su política. El código calcula y la persona decide.

### Lo que nunca hace

- **Aprobar un cambio, decidir una arquitectura ni elegir un proveedor.** Dice qué no tiene su aprobación, su revisión o su soporte; la decisión es del comité de cambios y del área.
- **Conectarse a una herramienta de gestión del servicio, a la nube ni a un servidor.** Procesa sus exportaciones.
- **Procesar la seguridad.** Las vulnerabilidades, los controles y los incidentes de seguridad son de la CISO.

### Lo que cruza con las otras familias

| Lo que procesa | Con qué familia |
|---|---|
| Los incidentes de seguridad y la continuidad | CISO (Amparo) |
| Los activos que no se escanean | CISO (Guillermo) |
| Los contratos con los proveedores de tecnología y sus cláusulas | CLO (Fidel) |
| Las facturas de tecnología contra el presupuesto y la contabilidad | CFO (Tomás y Clara) |
| Los proyectos que producen los cambios | PMO (Vera) |

### Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| La política de cambios y de niveles de servicio | Word o PDF | Los dos |
| La exportación de cambios de la herramienta de gestión del servicio | Excel o CSV | Fausto |
| Las actas del comité de cambios | PDF o Word | Fausto |
| El registro de despliegues en producción | Excel o CSV | Fausto |
| Las exportaciones de incidentes y de problemas | Excel o CSV | Fausto |
| El catálogo de servicios con su nivel acordado | Excel o PDF | Fausto |
| El inventario de activos con su dueño y su fin de soporte | Excel o CSV | Domingo |
| Las licencias compradas y su uso | Excel o CSV | Domingo |
| Los contratos de nivel de servicio y las facturas de cada proveedor | PDF o Excel | Domingo |
| La factura de la nube y su presupuesto | Excel o CSV | Domingo |

### Cifras de terceros

| Id | Cifra | Fuente |
|---|---|---|
| C-01 | 84 % de las organizaciones dice que gestionar el gasto en la nube es su mayor reto | Flexera, State of the Cloud 2025, más de 750 profesionales y directivos, marzo de 2025 |
| C-02 | 57 % dice que su última caída mayor costó más de 100.000 dólares | Uptime Institute, encuesta anual 2025, más de 800 dueños y operadores de centros de datos, citada en su análisis de caídas de 2026 |
| C-03 | 1 de cada 5 reporta caídas de más de un millón de dólares, por segundo año | Uptime Institute, la misma encuesta |

### La prueba

- **Organizaciones sintéticas** de banca, retail y tecnología, más dos controles. Desde el material de la
  ronda 1, cada defecto se siembra más de una vez, para que la familia pase de 73 señales (decisión 0020).
- **Versiones:** la 0.1.0, construida con su motor probado; la 0.2.0, con la ronda de los dos agentes.

## Lo que queda abierto

1. **Las fuentes por verificar**: las cláusulas de ISO/IEC 20000-1, la guía de ITIL 4, los objetivos de COBIT 2019, la norma de la SBS y la Resolución CMN 4.893.
2. **Las exportaciones de las herramientas**, como ServiceNow, Jira Service Management, Flexera o la facturación de AWS, Azure y Google Cloud, cada una con su fuente o con los encabezados de una exportación real.
