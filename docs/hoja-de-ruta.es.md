# La hoja de ruta de Criterio

[English](hoja-de-ruta.md)

Todas las familias en un solo documento. Se genera con `scripts/hoja.py` desde la hoja de ruta de cada familia (`families/criterio-<sigla>/hoja-de-ruta.json`), el registro de versiones (`registro/versiones.json`) y las decisiones de alcance (`docs/decisions/`): no se edita a mano.

- **Cada familia lleva su propia versión** (decisión 0017) y sube solo cuando ella cambia.
- **Diez versiones por entero** (decisión 0020): de x.0 a x.9, y después la x+1.0. La 0.10, la 0.11 y la 0.12 son las únicas excepciones: quien está ahí sube a la 1.0.
- **Laboratorio o estable lo dice la evidencia, no el número:** estable, si la corrida más reciente de cada entidad del material tiene el piso del margen del 95 % en 95 % o más, en señales y en datos, y ningún control levanta una señal; si no, laboratorio. Lo calcula `scripts/calidad.py`.
- **Un incremento es una versión con su prueba completa** y su análisis estadístico, con las mismas métricas que las anteriores.

## Dónde está cada familia hoy

| Familia | Agentes | Versión | Calidad | Lo siguiente |
|---|---|---|---|---|
| Criterio PMO · Gobierno de proyectos | Vera, Samuel, Alba | 1.0.0 | Estable | — |
| Criterio CFO · La función financiera | Clara, Tomás, Áurea | 1.0.0 | Laboratorio | — |
| Criterio CLO · Contratos y cumplimiento | Fidel, Constanza | 1.1.0 | Laboratorio | — |
| Criterio EA · Dirección | Ofelia | 1.0.0 | Estable | — |
| Criterio CCO · La función comercial | Augusto, Valeria | 0.3.0 | Estable | — |
| Rostrum · el portal de todas las familias | — | 1.0.0 | — | — |

## Cada familia, incremento por incremento

### Criterio PMO · Gobierno de proyectos

| Versión | Estado | Qué entra | Prueba |
|---|---|---|---|
| 0.6.0 | Liberada | **Material más amplio**<br>· Las correcciones D058 a D060<br>· 20 proyectos por industria en el material de prueba<br>· Las industrias desde una sola fuente | La verifica la prueba de la 0.7.0 |
| 0.7.0 | Liberada | **Cronogramas de Microsoft Project**<br>· El XML de Project como cronograma: tareas, hitos, línea base, avance, predecesoras y recursos; el .mpp donde haya Java y MPXJ<br>· La estructura de carpetas recomendada<br>· El contraste entre la ficha del gerente y la de la PMO como lo define el skill<br>· El análisis estadístico, regenerado con cada prueba<br>· Esta hoja de ruta, desde una sola fuente | 4 industrias, 80 proyectos |
| 0.8.0 | Liberada | **Rostrum para todas las familias, y la CFO y la CLO**<br>· Rostrum, un plugin propio para todas las familias, con un menú por familia y un inicio que dice qué pide atención hoy, WCAG 2.2 AA comprobado con axe-core<br>· La carpeta raíz que cada agente busca y, con permiso, marca<br>· Las familias CFO y CLO, con el motor probado y una primera ronda con el agente | La verifica la prueba de la 0.9.0 |
| 0.9.0 | Liberada | **Construcción e infraestructura, y oil & gas**<br>· Dos industrias nuevas, con sus propios proyectos, documentos y situaciones | 6 industrias |
| 1.0.0 | Liberada | **Telecomunicaciones y logística, y el cronograma en Rostrum**<br>· Dos industrias nuevas: la escala del portafolio y la operación que no se detiene<br>· Rostrum: el Gantt de línea base contra vigente, los hitos y la curva de avance en la página de cada proyecto | La ronda con los agentes en las dos industrias nuevas, con los 38 comandos; las seis anteriores, con su corrida de la ronda 11. El Gantt y la curva, sobre las fichas de las 8 industrias |

### Criterio CFO · La función financiera

| Versión | Estado | Qué entra | Prueba |
|---|---|---|---|
| 0.8.0 | Liberada | **Construida, con el motor probado y una primera ronda con el agente**<br>· Los comandos de Clara y Tomás, sus skills y el motor de cálculo<br>· La factura electrónica de la DIAN y del SRI, procesada desde su fuente técnica oficial<br>· La carpeta raíz que cada agente busca y, con permiso, marca<br>· La familia en Rostrum, con lo que vence y dónde trabaja cada agente<br>· La primera ronda con el agente: Clara y Tomás sobre banca y el control de Colombia, con los defectos que encontró corregidos | El motor, contra 4 industrias y 2 entidades de control; el agente, sobre banca y el control de Colombia |
| 0.9.0 | Liberada | **La ronda completa con el agente**<br>· Clara y Tomás corren sus comandos sobre el material de las cuatro industrias, como la PMO en cada ronda<br>· Lo que solo traen las actas, los correos y las cartas del auditor, extraído y calificado contra la clave<br>· Con la ronda completa, la familia se declara probada | 4 industrias y 2 entidades de control, con la clave que el agente no ve |
| 0.10.0 | Liberada | **Áurea, Perú y los formatos de un área financiera real**<br>· Áurea, el tercer agente: la caja, los pagos y la deuda contra su política<br>· Perú, con el lector de la factura electrónica de la SUNAT desde su guía oficial<br>· El material de prueba en Excel, Word y PDF, como lo tiene un área financiera, y el extracto bancario en PDF procesado por el motor | La ronda 4, completa: los tres agentes sobre las nueve entidades de Colombia, Ecuador y Perú, con los defectos que encontraron sus rondas corregidos y verificados |
| 0.11.0 | Liberada | **Chile**<br>· El lector de la factura electrónica de Chile, el DTE del SII (F-16), con el RUT y su dígito verificador<br>· El IVA del 19 % (F-17) y las NIIF que adoptó el Colegio de Contadores (F-18)<br>· Material de retail, minería y una entidad de control de Chile | La ronda 5: los tres agentes sobre las tres entidades de Chile, 26 de 26 señales, ninguna de más y 24 de 24 datos |
| 0.12.0 | Liberada | **México**<br>· El lector del CFDI 4.0 del SAT, desde su guía de llenado (F-19), con el RFC<br>· El IVA del 16 % del catálogo de la guía y el marco NIIF o NIF de cada entidad (F-20)<br>· Material de banca, retail y una entidad de control de México | La ronda 6: los tres agentes sobre las tres entidades de México, 27 de 27 señales, ninguna de más y 24 de 24 datos |
| 1.0.0 | Liberada | **Brasil**<br>· Su entrada en el registro de países, el lector de su factura electrónica y sus fuentes verificadas<br>· Los documentos en portugués: el motor los procesa como los de los demás países | La ronda 7 con los tres agentes en Brasil, con los documentos en portugués: 24 de 24 señales, ninguna de más, y 24 de 25 datos; el defecto que encontró, en la clave, con su corrección |

### Criterio CLO · Contratos y cumplimiento

| Versión | Estado | Qué entra | Prueba |
|---|---|---|---|
| 0.8.0 | Liberada | **Construida, con el motor probado y una primera ronda con el agente**<br>· Los catorce comandos de Fidel y Constanza, sus skills y el motor de cálculo<br>· Colombia y Ecuador, sin opinión jurídica: lo que exige una obligación lo define la organización en su matriz<br>· La carpeta raíz que cada agente busca y, con permiso, marca<br>· La familia en Rostrum, con lo que vence y dónde trabaja cada agente<br>· La primera ronda con el agente: Fidel y Constanza sobre banca y el control de Colombia, con los defectos que encontró corregidos | El motor, contra 4 industrias y 2 entidades de control; el agente, sobre banca y el control de Colombia |
| 0.9.0 | Liberada | **La ronda completa con el agente**<br>· Fidel y Constanza corren sus comandos sobre el material de las cuatro industrias, como la PMO en cada ronda<br>· Lo que solo trae cada contrato —partes, valor, fechas, renovación, preaviso, firmantes, otrosíes, garantías y obligaciones—, extraído y calificado contra la clave<br>· Con la ronda completa, la familia se declara probada | 4 industrias y 2 entidades de control, con la clave que el agente no ve |
| 0.11.0 | Liberada | **Perú y Chile**<br>· Material de banca, minería y control de Perú, y de retail, minería y control de Chile, con la identificación fiscal de cada país<br>· Una obligación atada a la terminación vence en la terminación vigente, la del último otrosí (CLO-10) | La ronda 4: Fidel y Constanza sobre las seis entidades de Perú y Chile, 37 de 37 señales, ninguna de más y 812 de 813 datos; el que faltó, corregido y verificado |
| 0.12.0 | Liberada | **México**<br>· Material de banca, retail y control de México, con el RFC de cada contraparte<br>· La fecha de una obligación atada a la terminación es la del último otrosí: lo dice la skill y el motor lo revisa en la ficha (CLO-11) | La ronda 5: Fidel y Constanza sobre las tres entidades de México, 20 de 20 señales, ninguna de más y 395 de 396 datos; el que faltó, corregido y verificado |
| 1.0.0 | Liberada | **Brasil**<br>· Sus fuentes legales verificadas y su material de prueba<br>· Los documentos en portugués: el motor los procesa como los de los demás países | La ronda 6 con los dos agentes en Brasil, con los documentos en portugués: 20 de 20 señales, ninguna de más, y 395 de 396 datos; el defecto que encontró, en el arnés, con su corrección |
| 1.1.0 | Liberada | **Los contratos públicos**<br>· Las reglas de publicación y de garantía de la ley de contratación pública de cada país del registro, cada una con su fuente: el plazo para publicar el contrato en el sistema nacional, el mínimo de la garantía de cumplimiento —su tope, en Brasil— y su entrega a tiempo, en México<br>· Una entidad pública de prueba por país, con sus constancias de publicación y sus pólizas | La ronda 7 con Fidel sobre las seis entidades públicas, una por país: 19 de 19 señales, ninguna de más, y 909 de 912 datos; los dos defectos que encontró, en la clave y en las instrucciones, con su corrección y su verificación |

### Criterio EA · Dirección

| Versión | Estado | Qué entra | Prueba |
|---|---|---|---|
| 0.12.0 | Liberada | **Ofelia, construida y probada con la ronda completa con la agente**<br>· Los nueve comandos de Ofelia, sus skills y el motor: la agenda .ics con repeticiones y cambio de hora, el correo guardado, las sesiones de los órganos y los compromisos con las reglas de Samuel<br>· Prepara cada decisión con sus opciones y su evidencia, sin ordenarlas ni recomendar<br>· Colombia y Ecuador, en la oficina de una presidencia y de una gerencia general, y dos oficinas de control | La ronda 1: Ofelia sobre las cuatro oficinas, 14 de 14 señales y 76 de 78 datos, con una señal de más en un control; cada defecto que encontró, con su corrección y su verificación |
| 1.0.0 | Liberada | **Los viajes, y las exportaciones de cada proveedor**<br>· Los itinerarios contra la agenda<br>· El .ics que exportan Outlook y Google Calendar y el correo .msg de Outlook, cada uno con su material: lo que de verdad cambia de una oficina a otra, no el país<br>· El material siembra al menos 73 señales, lo que pide un piso del 95 % sin fallas (decisión 0020), y la ronda con la agente vuelve a correr sobre todo él | La ronda 2 con la agente sobre las cuatro oficinas, cada una con su proveedor —Outlook o Google—: 85 de 85 señales y 144 de 146 datos en la primera corrida, ninguna señal en los controles; el defecto que encontró, en el material, con su corrección y su verificación |

### Criterio CCO · La función comercial

| Versión | Estado | Qué entra | Prueba |
|---|---|---|---|
| 0.1.0 | Liberada | **Augusto y Valeria, construidos, con el motor probado**<br>· Los doce comandos, sus skills y el motor, con las nueve señales: el embudo, el pronóstico y la meta de Augusto; el descuento, el contrato, la factura y la comisión de Valeria<br>· Las exportaciones de Salesforce y de HubSpot, y cualquier CSV o Excel con su mapeo de columnas<br>· Lo ganado contra los contratos de Fidel y lo firmado contra las facturas de Clara, por sus fichas<br>· Colombia y México, con entidades de control | El motor contra la clave de todo el material: seis entidades de Colombia y México, con sus controles |
| 0.2.0 | Liberada | **La ronda completa con los agentes**<br>· Augusto y Valeria corren sus comandos sobre todas las entidades del material, con una clave que no ven<br>· El material siembra al menos 73 señales: lo que pide un piso del 95 % sin fallas (decisión 0020)<br>· Cada defecto que encuentre la ronda, con su corrección y su verificación | La ronda 1 con los dos agentes sobre las seis entidades del material: 72 de 80 señales sembradas y 30 de 30 datos en la primera corrida, con dos señales de más en un control, y 80 de 80 sin ninguna de más después de verificar las correcciones; los tres defectos que encontró, con su corrección y su verificación |
| 0.3.0 | Liberada | **Ecuador, Perú y Chile, y Microsoft Dynamics y Zoho**<br>· Los tres países que ya están en el registro de países, con su material y su ronda<br>· Las exportaciones de Microsoft Dynamics y de Zoho, cada una desde su fuente verificada | La ronda 2 con los dos agentes sobre las nueve entidades de Ecuador, Perú y Chile, tres con Dynamics y tres con Zoho: 117 de 117 señales sembradas y 45 de 45 datos en la primera corrida, con una señal de más en un control; el defecto que encontró, en las instrucciones, con su corrección y su verificación |

## Las familias que vienen

Cada una entra con su decisión de alcance: aceptada, se diseña; propuesta, espera su turno, sin fecha.

| Decisión | Familia | Estado |
|---|---|---|
| [0013](decisions/0013-scope-seguridad-ciso.md) | Seguridad de la información (CISO) | Propuesta |
| [0014](decisions/0014-scope-auditoria-cae.md) | Auditoría interna (CAE) | Propuesta |
| [0015](decisions/0015-scope-datos-cdo.md) | Datos (CDO) | Propuesta |
| [0019](decisions/0019-scope-comercial-cso.md) | La función comercial (CSO) | Aceptada |
