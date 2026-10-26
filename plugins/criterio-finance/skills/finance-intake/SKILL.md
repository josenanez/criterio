---
name: finance-intake
description: "Qué documentos procesa la familia CFO, dónde va cada uno, qué procesa el motor directamente y qué extrae el agente a la ficha. Úsalo al recorrer la carpeta de una entidad, al recibir un documento nuevo, al explicar dónde va un archivo o cuando una exportación no trae las columnas esperadas. Finance document intake, folder structure, ERP exports."
---

# Los documentos de la función financiera

## Dos clases de documento, dos formas de procesarlo

**Las tablas y las facturas las procesa el motor directamente.** Balance de comprobación, libro mayor, auxiliares, extractos bancarios, checklist del cierre, índice de requerimientos del auditor, presupuesto y sus versiones, compromisos y proyecciones llegan como exportaciones en `.csv` o `.xlsx`; las facturas electrónicas, como XML de la DIAN o del SRI. Nada de eso se transcribe ni se resume: `finanzas.py` lo lee con su fila de origen, que es la cita.

**Lo que solo trae un documento escrito lo extrae el agente a la ficha.** El estado que alguien declara («septiembre quedó cerrado»), un acta de aprobación o de traslado, un requerimiento del auditor que llegó por correo, lo que un área dice de su presupuesto. Se convierte con `finanzas.py convertir` y se registra en la ficha con su cita. El código no lo inventa ni lo infiere.

## Las columnas de una exportación

El motor reconoce las columnas por su nombre —`cuenta`, `debito`, `credito`, `saldo_final`, `fecha`, `tercero`, `documento`, `comprobante`, `centro_costo`, `valor`— y por sus variantes más comunes (`debe`, `haber`, `nit`, `asiento`…). Cuando una exportación las llama de otra forma, el motor dice cuáles faltan. **No adivines**: pregúntale a la persona cómo se llama la columna en su ERP y regístralo en `columns` de la configuración, por tabla (`trial_balance`, `ledger`, `bank_statement`, `bank_book`, `subledger`, `checklist`, `audit`, `budget`, `budget_map`, `commitments`, `forecast`).

Los números llegan con coma o con punto decimal; las fechas en ISO, `dd/mm/aaaa` o como número de serie de Excel. El motor los normaliza; un valor que no puede leer lo reporta.

## La estructura recomendada

<!-- cfo:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). La contabilidad del periodo tiene un solo lugar, `10-contabilidad/`: Clara la cierra, Tomás saca de ahí la ejecución y Áurea calcula ahí los covenants.

Una carpeta por entidad, con el NIT o el RUC al inicio del nombre: `900123456-nombre-de-la-entidad`. Dentro, lo que la organización entrega una vez, una carpeta por periodo contable y una por año presupuestal.

```
finanzas/
└── <entidad>/
    ├── 00-referencia/
    ├── <AAAA-MM>/
    │   ├── 10-contabilidad/
    │   ├── 20-bancos/
    │   ├── 30-facturacion/
    │   ├── 40-soportes/
    │   ├── 50-auditoria/
    │   └── 60-tesoreria/
    └── presupuesto-<AAAA>/
        ├── 10-aprobado/
        ├── 20-compromisos/
        ├── 30-proyecciones/
        └── 40-actas/
estado-finanzas/
```

**`<entidad>/`** · Lo que la organización entrega una vez

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | El plan de cuentas con la naturaleza de cada cuenta, `checklist-cierre.xlsx` en el modelo definido y el mapeo de cuentas a centros de costo y líneas presupuestales; para Áurea, la política de tesorería, la matriz de firmas, el registro de la deuda y los covenants | Clara, Tomás, Áurea |

**`<AAAA-MM>/`** · Un periodo contable, numerado en el orden en que se trabaja el cierre

| Carpeta | Qué va | Agente |
|---|---|---|
| `10-contabilidad/` | Balance de comprobación y libro mayor exportados del ERP, y `auxiliares/` con un archivo por cuenta; de aquí sale también la ejecución del presupuesto | Clara, Tomás |
| `20-bancos/` | Una carpeta por cuenta, `<banco>-<últimos 4 dígitos>`, con el extracto y el auxiliar de libros | Clara, Áurea |
| `30-facturacion/` | `emitidas/` y `recibidas/`, con el XML de la DIAN (F-01) o del SRI (F-04) | Clara |
| `40-soportes/` | La evidencia de cada tarea del checklist —actas, correos, conciliaciones firmadas—, con el id de la tarea al inicio del nombre | Clara |
| `50-auditoria/` | `requerimientos/` y `respuestas/` del auditor | Clara |
| `60-tesoreria/` | El programa de pagos con quién aprobó cada uno y el flujo de caja proyectado al cierre del periodo | Áurea |

**`presupuesto-<AAAA>/`** · Un año presupuestal

| Carpeta | Qué va | Agente |
|---|---|---|
| `10-aprobado/` | El presupuesto aprobado y cada versión, con su fecha en el nombre | Tomás |
| `20-compromisos/` | Órdenes de compra y compromisos exportados del ERP, con la fecha de corte en el nombre | Tomás |
| `30-proyecciones/` | La proyección de cada área, una por área y fecha | Tomás |
| `40-actas/` | Actas del comité de presupuesto, de aprobación y de traslados | Tomás |

**`estado-finanzas/`** · Lo que escriben Clara, Tomás y Áurea: la configuración, las fichas, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cfo:intake -->

## Lo que nunca se hace

- **Mover, renombrar o crear** algo dentro de los documentos de la organización. La estructura se sugiere; el inventario dice dónde iría cada archivo. La única excepción es la marca de la carpeta raíz, `_CRITERIO_<…>.txt`, que se deja solo con el sí de la persona y que ningún inventario cuenta como documento (ADR 0011).
- **Escribir el estado dentro de la carpeta de documentos.** El estado vive en `estado-finanzas/<entidad>/`.
- **Adivinar el formato** de un archivo que no se pudo procesar: se reporta con lo que le falta.
