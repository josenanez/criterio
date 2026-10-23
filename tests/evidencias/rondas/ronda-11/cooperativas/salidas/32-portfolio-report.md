# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-23

Cargué las 13 fichas (PRY-199 a PRY-211), del barrido de hoy. Los términos ya estaban vigentes (versión 0.8.0, aceptados por José Francisco Ñáñez el 2026-10-23), así que no los registré de nuevo.

**Resultado:** 13 proyectos, 11 con hallazgos y 67 señales. La corrida tardó 41 s y leyó 79 documentos sin cambios, así que no releyó ninguno.

- **Qué cambió:** nada. La instantánea anterior es del mismo día y el diff dio 0 cambios.
- **Contradicciones entre fuentes:** ninguna.
- **Hitos vencidos sin evidencia:** ninguno.
- **Dependencias entre proyectos:** no hay ninguna declarada.
- **En silencio:** PRY-207 Microcrédito rural, 16 días desde el 2026-10-07 (el umbral es 15).
- **Siete proyectos en verde contradichos por la evidencia:**
  - PRY-201, PRY-202 y PRY-207 tienen hitos cumplidos sin evidencia o compromisos vencidos, y PRY-207 además está en silencio.
  - PRY-203 lleva 85 días de atraso contra la línea base original.
  - PRY-204 tiene $1.064.377.272 facturados por el proveedor sin entrega.
  - PRY-209 movió la línea base 118 días sin autorización.
  - PRY-211 proyecta un sobrecosto de 25,7 % ($5.280.911.293 contra $4.200.000.000).
- **Otros proyectos con hallazgos:**
  - PRY-206 tiene 4 compromisos vencidos, 5 sin fecha y 4 reprogramados.
  - PRY-210 movió la línea base 28 días sin autorización.
  - PRY-200 y PRY-205 tienen hitos cumplidos sin evidencia.
- **Vacíos de información:** ningún proyecto tiene autoridad registrada (los 13), y 5 proyectos no tienen producto asociado: PRY-202, PRY-205, PRY-208, PRY-209 y PRY-210.
- **Confirmación del mes:** no hay campos para confirmar este mes.

## Dónde quedó el informe
El HTML quedó en `reportes/`, que son 25 páginas:
- **`reportes/index.html`:** vista por campo con la cadena de evidencia completa, para quien va a actuar.
- **`reportes/decisiones.html`:** vista por decisión, para el patrocinador, con solo lo que excede la facultad de quien gerencia.
- **Detalle:** una página por proyecto y páginas por producto.
- **PDF:** sale de imprimir el HTML.

La corrida quedó registrada como `2026-10-23-portfolio-report-1`. Lo que te mostré está guardado en `estado/corridas/salida-portfolio-report.md`.

Si hay un comité próximo, el de 2026-10-30, puedo preparar el material. También puedo entrar al detalle de los proyectos con hallazgos.

*criterio-portfolio 0.8.0 · fichas del 2026-10-23 · ningún campo marcado como ambiguo; falta la autoridad en los 13 proyectos · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.8.0*