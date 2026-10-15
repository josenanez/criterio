# /criterio-portfolio:portfolio-report html

El informe en HTML quedó generado y la corrida registrada. Cargué 13 fichas de `estado/records/`, todas con fecha 2026-10-15. No hay fichas viejas.

Los términos ya estaban vigentes (versión 0.3.9, aceptados por José Francisco Ñáñez el 2026-10-15), así que no volví a registrar la aceptación.

**Qué cambió:** nada. Es la primera instantánea (2026-10-15) y el diff dio 0 cambios.

**Hallazgos:** hay 63 señales en 10 de los 13 proyectos, y 6 proyectos reportados en verde están contradichos por la evidencia. Solo PRY-199, PRY-200 y PRY-207 salen sin hallazgos.

| Proyecto | Señales |
|---|---|
| PRY-203 Despacho automático de flota | 16 |
| PRY-204 Monitoreo de taludes | 11 |
| PRY-202 Planta de tratamiento de agua | 6 |
| PRY-211 Control de polvo en vías | 6 |
| PRY-205, PRY-206 y PRY-209 | 5 cada uno |
| PRY-201 y PRY-208 | 4 cada uno |
| PRY-210 | 1 |

PRY-204 lleva 16 días en silencio y tiene proveedores con facturas sin entrega. Dos proyectos no tienen línea base. Siete proyectos no tienen producto asociado: PRY-201, 202, 205, 206, 209, 210 y 211. Ninguno de los 13 tiene autoridad declarada.

**Dónde quedó:** en `/home/claude/banco/ronda-3/mineria/espacio/reportes/` (23 páginas). No pegué el HTML aquí.
- **`index.html`:** vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- **`decisiones.html`:** vista por decisión, solo lo que excede la facultad de quien gerencia. Es para el patrocinador.
- **PDF:** sale de imprimir el HTML.

**Confirmación mensual:** no hice las cinco preguntas, porque la sesión es de prueba y nadie las responde.

**Corrida:** quedó como `2026-10-15-portfolio-report-1`, con 80 documentos sin cambio y 22 segundos medidos. Lo que te mostré está en `estado/corridas/salida-portfolio-report.md`.

Si hay comité el 2026-10-19, puedo preparar el material de comité o entrar al detalle de PRY-203 y PRY-204.

Criterio Portfolio 0.3.9 · fichas aplicadas: 13, fecha 2026-10-15 · campos inciertos: los contradichos y sin sustento listados en `index.html` · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.9