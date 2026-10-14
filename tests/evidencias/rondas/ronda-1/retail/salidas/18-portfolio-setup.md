# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio retail

**Miré:** 55 documentos en 13 proyectos (.md 23, .docx 11, .pdf 9, .csv 5, .xlsx 5, .json 1, .txt 1). El más reciente es del 2026-10-14.
**Eres:** PMO del portafolio. Tomé la respuesta sugerida porque hay 13 proyectos.
**Te aviso:** dos días antes del comité. No se indicó comité, así que asumí uno semanal.
**En:** presentación (respuesta sugerida).

Dejé aceptados los términos a nombre de José Francisco Ñáñez, fecha 2026-10-14. La configuración está en `.criterio/portafolio/config.json`. El estado está en `estado-portafolio/` y no en `estado/`, porque `estado/` ya guardaba el estado de PRY-211 de otro comando. Los informes irán en `reportes/`.

### Probé con tres proyectos

Tomé los de documentación más reciente: PRY-203, PRY-208 y PRY-211. Escribí y sellé una ficha por cada uno. Las señales de abajo salen de `compute`.

| Proyecto | Qué supe | Qué no está |
|---|---|---|
| PRY-203 Reposición automática | Gerente Natalia Ospina. Declara verde y 56 %. Presupuesto de 800 M COP, con 49,8 % ejecutado. | Producto, autoridad del gerente, fase |
| PRY-208 Domicilios en dos horas | Gerente Carlos Peña. Declara verde y 55 %. Presupuesto de 1.200 M COP, con 33,7 % ejecutado. | Autoridad, fase |
| PRY-211 Pronóstico de demanda | Gerente Camilo Beltrán. Declara verde y 35 %. Presupuesto de 18.000 M COP, con 45,6 % ejecutado. | Producto, autoridad, fase. La ficha del gerente no trae estado ni avance. |

Los tres declaran verde y los tres tienen señales en contra:

- **PRY-203:**
  - Declara 56 %, pero el cronograma sustenta entre 75 % y 100 %.
  - Dos hitos figuran cerrados sin acta: «Diseño de la experiencia aprobado» e «Integración con el ERP».
  - El compromiso de Gustavo Neira, «punto 23», venció hace 16 días.
- **PRY-208:**
  - El hito «Diseño de la experiencia aprobado» figura cerrado sin acta.
  - El compromiso de Laura Vélez, «punto 38», venció hace 19 días.
- **PRY-211:**
  - Declara 35 %, pero el plan sustenta entre 50 % y 75 %.
  - El compromiso de Laura Vélez, «ajuste del presupuesto», quedó sin fecha.
  - La fecha de cierre no coincide: el acta y la ficha del gerente dicen 2027-05-04 y el cronograma dice 2027-03-16.

### El portafolio completo
Faltan 10 proyectos, con 39 documentos por leer, en un solo lote. Calculo entre 15 y 25 minutos, uno tras otro. Es una estimación y no la medí.

### Lo que le falta a tu carpeta
- Ninguna acta de constitución de estos tres declara la autoridad del gerente ni la fase.
- Los hitos cerrados del cronograma casi nunca traen acta de recibo.
- Algunos compromisos de comité no tienen fecha, o tienen una anterior a la reunión donde se anotaron.
- En PRY-203 el patrocinador y el presupuesto salen solo de un acta de hace 14 meses, sin confirmación posterior.

Ninguno bloquea nada: el análisis funciona con lo que hay.

Hice cero preguntas, como se indicó. La corrida quedó registrada como `2026-10-14-portfolio-setup-1`, con la salida completa en `estado-portafolio/corridas/salida-portfolio-setup.md`. ¿Corro el portafolio completo?