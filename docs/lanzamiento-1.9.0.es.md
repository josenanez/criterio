# Criterio · catálogo 1.9.0 · 2 de noviembre de 2026

Paraguay entra a la CFO y a la CLO; la CISO lee las exportaciones de Tenable y de Microsoft Defender
y pasa a estable con su segunda ronda; y Rostrum dice cuándo deja señales fuera por privadas. Código
abierto bajo Apache 2.0.

**El número del catálogo solo ordena las entradas del registro de versiones.** La versión de cada familia es la suya.

## Qué trae

| | |
|---|---|
| **Paraguay en la CFO (1.3.0)** | El lector del documento electrónico de SIFEN por su CDC de cuarenta y cuatro posiciones, con los campos del Manual Técnico 150 de la DNIT (F-40) y el esquema XSD 150 de la SET (F-41). El IVA se toma del documento a cualquiera de sus tasas, la del 10 % y la del 5 % (E734). La factura recibida emitida antes de la vigencia de su timbrado, que SIFEN rechaza (validación 1103), levanta `invoice_outside_authorization`, que ya no es solo de Honduras. El marco contable de cada entidad sale del perfil NIIF de Paraguay (F-42) |
| **Paraguay en la CLO (1.4.0)** | Banca, retail y control, sin entidad pública: la regla de la garantía de la ley de contrataciones públicas de Paraguay no está entre las fuentes verificadas |
| **La CISO, con sus escáneres (0.3.0)** | Guillermo lee la exportación de Tenable Vulnerability Management en CSV (F-08) y la de Microsoft Defender Vulnerability Management en JSON, también comprimida (F-09), cada una desde la documentación de su fabricante. Lo que una exportación de Defender no prueba —la cobertura de los activos— lo dice como no procesado, no como un hallazgo. Con la segunda ronda, la familia pasa a estable |
| **Rostrum (1.0.2)** | La página de una familia ya no dice «Sin señales abiertas» de un agente cuyas señales no se publican: dice que las hay fuera del portal y qué configuración lo abre, sin decir cuántas ni cuáles (Guillermo, `vulnerability.publish`) |
| **Los países probados** | Los README de la CFO y de la CLO traen la tabla de cada país con sus entidades, sus rondas, sus señales y sus datos, y la regla propia del país con su fuente; la escribe el código desde la evidencia de las rondas |

## Cómo se probó

| Ronda | | Señales | Datos |
|---|---|---|---|
| CFO · 13 | Paraguay: banca, retail y control | 28 de 28 | 24 de 24 |
| CLO · 13 | Paraguay: banca, retail y control | 20 de 20 | 396 de 396 |
| CISO · 2 | Energía en Perú con Tenable, aseguradora en Chile con Defender y un control en cada país | 48 de 48 | 32 de 32 |

Ninguna señal de más y ningún defecto nuevo. Con sus dos rondas, la CISO suma 80 datos extraídos y un
piso del 95,4 %. El material es sintético y lo escribe el repositorio; las rondas no reemplazan el
primer uso sobre los documentos de una organización real.

## Las versiones en la 1.9.0

| Familia | Versión | Calidad | Lanzamiento |
|---|---|---|---|
| PMO · Vera, Samuel y Alba | **1.0.2** | Estable | Semana del 19 de octubre |
| CFO · Clara, Tomás y Áurea | **1.3.0** | Estable | Semana del 26 de octubre |
| CLO · Fidel y Constanza | **1.4.0** | Estable | Sin lanzar |
| EA · Ofelia | **1.0.2** | Estable | Semana del 26 de octubre |
| CCO · Augusto y Valeria | **0.3.2** | Estable | Sin lanzar |
| CISO · Alexis, Guillermo y Amparo | **0.3.0** | Estable | Sin lanzar |
| Rostrum | **1.0.2** | — | — |

Todas suben: el registro de países, que lleva cada agente, suma Paraguay. La CFO y la CLO suman Paraguay, la CISO sus escáneres y Rostrum su corrección.

## Para actualizar

```
/plugin marketplace update criterio
```

Cada agente pide aceptar los términos de su versión y deja su comprobante en `.criterio/terminos/`.
