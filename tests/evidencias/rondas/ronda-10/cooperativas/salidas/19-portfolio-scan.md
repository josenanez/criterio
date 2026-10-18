# /criterio-portfolio:portfolio-scan 

Barrido terminado. Leí 51 de los 75 documentos y escribí y sellé las fichas de 10 proyectos: PRY-199, 200, 203, 204, 205, 206, 207, 209, 210 y 211. La corrida quedó registrada como `2026-10-18-portfolio-scan-1`. PRY-201, 202 y 208 ya tenían ficha y no cambiaron, así que no las abrí. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-18), por lo que no hizo falta volver a registrarlos.

- **Lectura:** los 75 archivos se convirtieron a texto sin error, no hay carpeta `entrada/` y no se movió nada. Todo corrió en esta conversación, sin subagentes.
- **Sin dato en 23 campos:**
  - Autoridad del gerente y fase quedan en `not_found` en los 10 proyectos, porque ningún acta los trae.
  - El producto también falta en PRY-205, 209 y 210, donde el acta dice «No aplica».
- **Hitos cerrados sin acta que los pruebe:** los registré como `met` con la evidencia vacía.
  - PRY-200: 4 hitos.
  - PRY-204: 5 hitos.
  - PRY-209: 3 hitos.
  - PRY-210: 4 hitos.
  - PRY-211: 1 hito.
- **Facturado sobre lo aceptado:** en PRY-200 (FV-1892, 1.002.986.926 COP) y PRY-209 (FV-1102, 3.038.412.141 COP) el contrato declara un solo entregable recibido, sin acta. PRY-204 sí cuadra.
- **PRY-210:** la solicitud de cambio CC-01 (+84 días, +168 millones COP) sigue pendiente del comité. El cronograma v2, del 2026-10-17, ya movió la «Salida a producción» al 2026-09-09 sin citar motivo ni aprobación.
- **Compromisos vencidos al registrarse:** el punto 35 de Natalia Ospina en PRY-206 (para el 2026-10-12) y el punto 33 de Elena Duarte en PRY-207 (para el 2026-10-02).
- **Sin cronograma y con la fecha de cierre del acta ya pasada:** PRY-203 y PRY-205.
- **PRY-201:** el índice reporta 17 fuentes de su `ficha-pm.json` que no resuelven, porque las rutas son relativas a la carpeta del proyecto y no a la raíz de documentación. No toqué esa ficha; hay que avisarle a quien la publica.

Corrí el barrido con la salida y las fichas ya escritas; el registro del script cuenta 65 hallazgos entre los 13 proyectos, con PRY-200 y PRY-209 entre los más cargados.

Puedo generar el informe consolidado con `/criterio-portfolio:portfolio-report`. El texto completo del barrido está en `estado/corridas/salida-portfolio-scan.md`. Términos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.5.0