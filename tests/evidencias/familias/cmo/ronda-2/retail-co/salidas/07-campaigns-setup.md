# /criterio-campaigns:campaigns-setup mercadeo/901333555-almacenes-del-valle-sinteticos

Próspero quedó configurado para Almacenes del Valle Sintéticos (NIT 901333555), periodo 2026-10, y ya corrió el primer reporte de presupuestos.

- **Configuración:** está en `.criterio/campanas/901333555/config.json`. La validación salió sin problemas.
- **Términos:** quedó registrada la aceptación de José Francisco Ñáñez con fecha 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-campaigns-0.2.0-2026-11-25.md` y en el `.pdf` del mismo nombre.
- **Preguntas:** no hice ninguna. Saqué las tolerancias (5 % sobre el presupuesto y 2 % entre el resultado y la plataforma) de `00-politica/politica_de_publicidad.pdf`. La entidad, el periodo y la carpeta de estado coinciden con los del setup de Lucía en esta misma carpeta.
- **Marca:** la carpeta ya tenía `_CRITERIO_MERCADEO.txt`, así que no la volví a poner.
- **Ficha 2026-10:** llevé a la ficha 3 resultados del informe, de las campañas C-01, C-03 y C-04, con corte al 2026-10-31.
- **Señales:** el cálculo encontró 15 en total. 9 están en el reporte de abajo; las otras 6 son 3 facturas de pauta sin campaña ni orden y 3 resultados que no coinciden con la plataforma, y salen en otros reportes.

# Cada campaña contra su presupuesto · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.2.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-01 · Temporada de fin de año: la pauta facturada suma 108,000,000 y el presupuesto es 100,000,000; la política tolera un 5 % más | 8.000.000,00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |
| 2 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-33 · Hogar: la pauta facturada suma 54,000,000 y el presupuesto es 50,000,000; la política tolera un 5 % más | 4.000.000,00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 11 |
| 3 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-32 · Día de la familia: la pauta facturada suma 23,000,000 y el presupuesto es 20,000,000; la política tolera un 5 % más | 3.000.000,00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 10 |
| 4 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta facturada hasta el 2026-10-31 (F-104) | 25.000.000,00 | — | 16 | `50-campanas/plan_de_mercadeo.xlsx` fila 4 · `50-campanas/facturas_de_pauta.xlsx` fila 5 |
| 5 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-43 · Feria escolar: terminaba el 2026-10-10 y hay pauta facturada hasta el 2026-10-25 (F-43) | 11.000.000,00 | — | 15 | `50-campanas/plan_de_mercadeo.xlsx` fila 13 · `50-campanas/facturas_de_pauta.xlsx` fila 12 |
| 6 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-42 · Verano: terminaba el 2026-09-30 y hay pauta facturada hasta el 2026-10-20 (F-42) | 9.000.000,00 | — | 20 | `50-campanas/plan_de_mercadeo.xlsx` fila 12 · `50-campanas/facturas_de_pauta.xlsx` fila 11 |
| 7 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-02 · Clientes recurrentes: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 |
| 8 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-22 · Aniversario: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 8 |
| 9 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-23 · Gran venta de noviembre: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 9 |

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 108,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | — | — |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 0 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |
| C-12 · Reactivación | 15,000,000 | 0 | 2026-10-01 | 2026-11-30 | 800 clientes reactivados | Clientes reactivados |
| C-13 · Referidos | 12,000,000 | 0 | 2026-10-01 | 2026-12-15 | 500 referidos | Referidos |
| C-22 · Aniversario | 25,000,000 | 0 | 2026-10-01 | 2026-11-15 | — | — |
| C-23 · Gran venta de noviembre | 35,000,000 | 0 | 2026-10-15 | 2026-11-30 | — | — |
| C-32 · Día de la familia | 20,000,000 | 23,000,000 | 2026-09-01 | 2026-10-31 | 900 ventas | Ventas atribuidas |
| C-33 · Hogar | 50,000,000 | 54,000,000 | 2026-09-01 | 2026-10-31 | 1500 ventas | Ventas atribuidas |
| C-42 · Verano | 18,000,000 | 9,000,000 | 2026-08-01 | 2026-09-30 | 1000 visitas a la tienda | Visitas a la tienda |
| C-43 · Feria escolar | 22,000,000 | 11,000,000 | 2026-09-01 | 2026-10-10 | 1200 visitas a la tienda | Visitas a la tienda |

Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

---

**Reloj:** no creé la tarea programada. Para crearla hace falta un sí explícito de la persona, y en esta prueba nadie podía darlo. Para revisar a mano se corre `/criterio-campaigns:campaigns-wake`.

**Cuándo vuelvo:** sin reloj.

**Registro:** la corrida quedó registrada como `2026-11-25-campaigns-setup-1`. Lo que mostré está en `estado-mercadeo/901333555-almacenes-del-valle-sinteticos/corridas/salida-campaigns-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.