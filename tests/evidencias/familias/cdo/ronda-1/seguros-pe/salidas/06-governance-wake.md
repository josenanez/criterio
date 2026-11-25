# /criterio-data-governance:governance-wake 

Hoy solo tocaba la revisión semanal de gobierno (`governance-scan`) de la Aseguradora Pacífico Sintética. Nadie dejó peticiones abiertas y los términos ya estaban aceptados, así que no hubo que registrar nada.

No llegaron documentos nuevos. Revisé la ficha de 2026-11 contra los documentos y coincide con las dos políticas, los plazos de conservación y el informe de junta. Siguen abiertas tres señales; qué hacer con cada una lo deciden el área de datos y el dueño de cada conjunto.

# Qué cambió en el gobierno · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `governance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización (`personal_data_unregistered`) | DS-03 · Proveedores: el catálogo dice que tiene datos personales y no está en el registro de bases de datos personales de la organización | — | Compras | — | `10-catalogo/catalogo_datos.xlsx` fila 4 · `10-catalogo/registro_de_bases_personales.xlsx` |
| 2 | Un conjunto conserva registros más tiempo del que fija la política para su tipo (`retention_exceeded`) | DS-04 · Candidatos: conserva registros desde el 2023-06-01, y la política fija 24 meses para «Candidatos»: todo lo anterior al 2024-11-25 pasó su plazo | — | Gestión humana | 543 | `10-catalogo/catalogo_datos.xlsx` fila 5 · `00-referencia/politica_de_conservacion.pdf` |
| 3 | Un conjunto de datos del catálogo no tiene un dueño de negocio (`dataset_without_owner`) | DS-02 · Movimientos: el catálogo no le asigna un dueño de negocio | — | — | — | `10-catalogo/catalogo_datos.xlsx` fila 3 |

## El resultado

**Conjuntos en el catálogo:** 5 · **Con datos personales:** 3 · **Políticas en la ficha:** 2 · **Términos de los informes:** 4.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/politica_de_conservacion.pdf`
- `10-catalogo/catalogo_datos.xlsx`
- `10-catalogo/registro_de_bases_personales.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

---

Las dos corridas, `governance-scan` y `governance-wake`, quedaron registradas con el caso 2026-11.