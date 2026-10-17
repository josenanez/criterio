# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos

**Miré:** 81 documentos en 13 proyectos. Formatos: .md (36), .pdf (15), .docx (12), .xlsx (9), .csv (7), .json (1), .txt (1). El más reciente es de 2026-10-17.
**Eres:** PMO del portafolio (propuesto, porque hay trece proyectos).
**Te aviso:** dos días antes del comité semanal. Propuse el 2026-10-24 como próximo comité porque los documentos muestran comités semanales y nadie dio fecha. Dime la real y la corrijo.
**En:** presentación, el valor sugerido.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-17 para la versión 0.3.13 (términos 1.1).
- Comprobante: `.criterio/terminos/aceptacion-criterio-portfolio-0.3.13-2026-10-17.md` y `.pdf`.
- SHA-256 de los términos: d31e6b3611041618…

No hice ninguna pregunta: la sesión es sin interfaz y tomé el valor sugerido en cada una. La configuración quedó en `.criterio/portafolio/config.json`, lo que Vera encuentre en `estado/` y los informes irán a `reportes/`.

### Probé con tres proyectos

Tomé los de documentación más reciente: PRY-211, PRY-205 y PRY-209.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-211 Cobranza digital | 5 | Gerente Camilo Beltrán, patrocinador Andrés Lozano, presupuesto 2.400.000.000 COP, cierre comprometido 2026-05-15. Declara **verde, 84 %**. Cinco hitos cerrados en el cronograma; solo «Salida a producción» tiene acta de recibo (2026-10-17). | Facultad del gerente y fase. El alcance es solo «Componente 1, 2, 3». |
| PRY-205 Prevención de lavado de activos | 17 | Gerente Natalia Ospina, patrocinador Rubén Cárdenas, presupuesto 800.000.000 COP. Cierre 2026-06-07 en el cronograma v3 (el acta decía 2026-03-19). Declara **verde, 27 %**. Hay 26 compromisos seguidos en seis comités y dos solicitudes de cambio pendientes (CC-01: +38 días y 76 M; CC-02: +42 días y 84 M). El proyecto publicó `ficha-pm.json`, que quedó aparte, en `pm_record`. | Producto («No aplica»), facultad y fase. Hay cronograma v3 y no hay v2. |
| PRY-209 Nómina electrónica | 8 | Gerente Gustavo Neira, patrocinador Carlos Peña, presupuesto 6.800.000.000 COP, cierre 2027-07-08. Declara **rojo, 29 %**. Contrato CT-258 con Integra Sistemas (cuatro entregables de 750.219.723 COP, uno con acta de recibo) y factura FV-1258 por 1.115.928.705 COP. | Facultad y fase. |

### Lo que levantó el cálculo (33 señales)

**PRY-205: declara verde y el cálculo no lo sostiene**
- `declared_vs_evidence`: verde declarado con seis señales abiertas.
- `variance_time` y `rebaseline_unauthorized`: +80 días (40,2 %) contra la fecha original, y ninguno de esos días está autorizado (las dos solicitudes siguen pendientes).
- `progress_vs_plan`: declara 27 % con 5 de 5 hitos cerrados, 73 puntos de diferencia.
- `milestone_met_without_evidence`: cinco hitos cerrados sin acta que lo pruebe. El más viejo lleva 372 días.
- `commitment_overdue`: 8 compromisos vencidos. El más antiguo es Paula Céspedes, «Actualizar la matriz 6», con 30 días. Sigue Rubén Cárdenas, «Revisar el anexo 3», con 29.
- `commitment_rescheduled`:
  - Sandra Gil, «Enviar el documento 1», 6 veces. Era 2026-09-17 y hoy es 2026-12-08.
  - Carlos Peña, «Cerrar la prueba 2», 5 veces.
  - Ricardo Salas, «Cerrar la prueba 10», 3 veces.
- `commitment_undated`: 2 compromisos sin fecha (Felipe Arango, «Confirmar la fecha 15»; Laura Vélez, ajuste del presupuesto).

**PRY-211: declara verde**
- `declared_vs_evidence`: verde declarado con dos señales abiertas.
- `progress_vs_plan`: 84 % declarado con 5 de 5 hitos cerrados (16 puntos de diferencia).
- `milestone_met_without_evidence`: cuatro hitos cerrados sin acta. El más viejo lleva 378 días.

**PRY-209: declara rojo**
- `variance_cost`: proyección al cierre de 8.198.690.139 COP contra 6.800.000.000 aprobados (+20,6 %).
- `vendor_invoiced_over_accepted`: facturado 1.115.928.705 COP contra 750.219.723 aceptados, una diferencia de 365.708.982 COP.
- `progress_vs_plan`: declara 29 % y el cronograma sostiene entre 40 y 60 %.
- `milestone_met_without_evidence`: «Diseño funcional aprobado» (109 días).
- `commitment_undated`: Javier Hoyos, «Entregar el punto 19».

Ninguno de los tres tiene la facultad del gerente. En PRY-205 y PRY-211 varios campos vienen del acta de hace 14–15 meses, sin confirmación posterior.

Dos hechos de los documentos no salieron como señal del cálculo, así que los dejo como datos y no como hallazgos:
- **Riesgo sin registrar:** en las notas del 2026-10-17 de PRY-205 se comentó que el proveedor podría no llegar con el equipo completo y nadie lo anotó. Lo dejé en los riesgos de la ficha, con esa fuente.
- **Entregas sin acta:** tres compromisos de PRY-205 se dieron por entregados en comité sin acta (anexo 3, fecha 15 y documento 17).

### El portafolio completo
Faltan 10 proyectos y 51 documentos, en dos lotes, uno tras otro. Con lo que tomó este arranque (tres proyectos y 30 documentos, unos 10–12 minutos contando la instalación), calculo entre 30 y 40 minutos. Es una estimación, no una medida.

### Lo que le falta a tu carpeta
- Faltan actas de recibo en casi todos los hitos que los cronogramas dan por cerrados: 10 de 12 en estos tres proyectos. Es lo que más pesa.
- El cronograma v3 de PRY-205 no tiene v2 al lado ni la aprobación del cambio de fecha.
- Las actas de constitución no traen la facultad del gerente y dejan el alcance en «Componente 1, 2, 3».
- Hay un archivo suelto en PRY-205 (`2026-10-17-notas-reunion.txt`) fuera de `30-reuniones/`. Se leyó, pero conviene moverlo.

Ninguno bloquea el análisis.

**Siguiente paso:** puedo correr el portafolio completo. Como uno de los proyectos ya publica su `ficha-pm.json`, también puedo publicar el estándar en una carpeta compartida para que los gerentes usen los mismos criterios.

Este texto está en `estado/corridas/salida-portfolio-setup.md` y la corrida quedó registrada como `2026-10-17-portfolio-setup-1`.