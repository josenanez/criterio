# /criterio-data-governance:governance-setup datos/901555777-banco-cordillera-sintetico

Soy Custodia. Pongo cada dato del catálogo junto a quien responde por él, su clasificación y su plazo. No asigno dueños ni borro nada.

**Carpeta:** solo había una candidata, `datos/901555777-banco-cordillera-sintetico`, que tiene `00-referencia/`, `10-catalogo/`, `20-informes/` y `30-calidad/`, así que la tomé. Procesé sus 12 documentos y todos estaban en su lugar.

**Preguntas** (como nadie podía contestar, tomé la respuesta que sugieren los documentos):
1. **Entidad:** Banco Cordillera Sintético, NIT 901555777, Colombia (COP). Lo saqué del nombre de la carpeta y de la política de datos.
2. **Periodo:** 2026-11.
3. **Publicar en Rostrum:** sí, porque la política de datos no dice lo contrario.
4. **Dónde guardo lo que encuentro:** `estado-datos/901555777-banco-cordillera-sintetico`.
5. **Términos**, tal cual:
   > Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

   Quedan aceptados por José Francisco Ñáñez (términos 1.6) el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-data-governance-0.2.0-2026-11-25.md` y en su versión `.pdf`.
6. **Marca `_CRITERIO_DATOS.txt` en la carpeta:** sí, ya quedó puesta.

**Configuración:** quedó en `.criterio/gobierno/901555777/config.json`. La tolerancia es 0.5 %, la que fija la política de datos.

**Primera ficha (2026-11):** registré 3 políticas con su fecha de revisión, 4 plazos de conservación y 13 términos del informe de junta de octubre. El motor encontró 19 señales:
- 3 conjuntos sin dueño
- 3 conjuntos sin clasificación
- 3 políticas con la revisión vencida
- 3 conjuntos que superaron su plazo de conservación
- 3 bases con datos personales sin registrar
- 4 términos que no están en el glosario

Abajo va el reporte de dueños y clasificación. Los demás salen con `/criterio-data-governance:retention-check` y `/criterio-data-governance:glossary-check`.

# Cada conjunto con su dueño · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `catalog-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-02 · Movimientos: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 3 |
| 2 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-12 · Pagos a proveedores: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 7 |
| 3 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-13 · Campañas de mercadeo: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 8 |
| 4 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-03 · Proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 |
| 5 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-22 · Contratos con proveedores: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 9 |
| 6 | Un conjunto no tiene su clasificación de confidencialidad (`dataset_without_classification`) | DS-23 · Inventario de activos: el catálogo no trae su clasificación de confidencialidad | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 10 |

## El resultado

| Conjunto | Dueño | Clasificación | Tipo | Datos personales |
|---|---|---|---|---|
| DS-01 · Clientes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-02 · Movimientos | — | Restringida | Transaccional | no |
| DS-03 · Proveedores | Compras | — | Proveedores | sí |
| DS-04 · Candidatos | Gestión humana | Confidencial | Candidatos | sí |
| DS-05 · Indicadores de gestión | Planeación | Interna | Transaccional | no |
| DS-12 · Pagos a proveedores | — | Interna | Transaccional | no |
| DS-13 · Campañas de mercadeo | — | Interna | Transaccional | no |
| DS-22 · Contratos con proveedores | Compras | — | Proveedores | no |
| DS-23 · Inventario de activos | Compras | — | Transaccional | no |
| DS-32 · Beneficiarios | Gerencia comercial | Confidencial | Clientes | sí |
| DS-33 · Visitantes de las sedes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-42 · Candidatos a prácticas | Gestión humana | Interna | Candidatos | no |
| DS-43 · Proveedores históricos | Compras | Interna | Proveedores | no |

El dueño y la clasificación los asigna el área: aquí se dice cuál falta.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-catalogo/catalogo_datos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión nadie lo dio. Para revisar a mano lo que toca: `/criterio-data-governance:governance-wake`.

La corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.