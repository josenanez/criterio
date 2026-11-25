# /criterio-data-governance:governance-setup datos/20605557771-aseguradora-pacifico-sintetica

Soy Custodia. Pongo cada dato del catálogo al lado de quien responde por él, de su clasificación y de su plazo; no asigno dueños ni borro nada.

**Carpeta:** hay una sola candidata: 1. `datos/20605557771-aseguradora-pacifico-sintetica`, con 00-referencia/, 10-catalogo/, 20-informes/ y 30-calidad/. Tomé la respuesta sugerida: sí, esa.

**Inventario:** 11 documentos, todos donde corresponden: 3 en 00-referencia, 2 en 10-catalogo, 1 en 20-informes y 5 en 30-calidad. Ninguno está fuera de lugar y todos se pudieron abrir.

**Las respuestas, tomadas de los documentos:**
- **Entidad:** Aseguradora Pacífico Sintética, RUC 20605557771, Perú (PEN).
- **Periodo:** 2026-11.
- **Publicar en Rostrum:** sí, porque la política de datos no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-datos/20605557771-aseguradora-pacifico-sintetica`.
- **Diferencia permitida entre una cifra y su fuente:** 0.5 %, según `00-referencia/politica_de_datos.pdf`, p. 1.
- **Marcar la carpeta con `_CRITERIO_DATOS.txt`:** sí.

**Términos (versión 1.6, del 2026-11-16):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-data-governance-0.1.0-2026-11-25.md` y en el `.pdf` del mismo nombre.

**Qué quedó listo:**
- La configuración, en `.criterio/gobierno/20605557771/config.json`. Se validó sin problemas.
- La marca `_CRITERIO_DATOS.txt`, en la carpeta de la entidad.

**Primera ficha (2026-11):** registré 2 políticas con su fecha de revisión, 4 plazos de conservación y 4 términos del informe de junta de octubre. El cálculo del periodo encontró 3 señales:
- un conjunto de datos sin dueño;
- una base con datos personales que no está en el registro;
- un dato que pasó su plazo de conservación.

Este reporte muestra solo la primera. Las otras dos las detallan /criterio-data-governance:glossary-check y /criterio-data-governance:retention-check.

# Cada conjunto con su dueño · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `catalog-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-02 · Movimientos: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 3 |

## El resultado

| Conjunto | Dueño | Clasificación | Tipo | Datos personales |
|---|---|---|---|---|
| DS-01 · Clientes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-02 · Movimientos | — | Restringida | Transaccional | no |
| DS-03 · Proveedores | Compras | Interna | Proveedores | sí |
| DS-04 · Candidatos | Gestión humana | Confidencial | Candidatos | sí |
| DS-05 · Indicadores de gestión | Planeación | Interna | Transaccional | no |

El dueño y la clasificación los asigna el área: aquí se dice cuál falta.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-catalogo/catalogo_datos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

**El reloj:** la tarea programada diaria solo se crea si alguien dice que sí expresamente, y en esta prueba nadie lo dijo, así que no la creé. Para correrla a mano: `/criterio-data-governance:governance-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.