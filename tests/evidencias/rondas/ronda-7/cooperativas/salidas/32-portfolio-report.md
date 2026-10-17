# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-17

Generé el informe HTML del portafolio: 13 proyectos, 12 con hallazgos y 66 señales. Cargué las 13 fichas de `estado/records`, todas del barrido de hoy. Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrar nada nuevo.

**Qué cambió:** nada que reportar. El único snapshot es el de hoy, así que esta corrida es el punto de partida y no hay comparación con una anterior.

**Lo que hay que mirar:**
- **Verdes contradichos por la evidencia:** PRY-203, PRY-209 y PRY-210.
- **Líneas base movidas sin autorización:** PRY-204 (116 días contra la original) y PRY-208 (59 días).
- **PRY-206 Pagos con QR:** el proveedor facturó sin entrega, y el proyecto tiene desviación de costo y de tiempo.
- **Hitos dados por cumplidos sin evidencia:** 23 en total, repartidos en 8 proyectos.
- **Hitos vencidos:** PRY-207 y PRY-209.
- **Proyecto en silencio:** PRY-205, 20 días sin documentos (umbral: 15).
- **Gobierno:** ningún proyecto tiene patrocinador o autoridad registrada.
- **Producto:** 5 proyectos no están ligados a ningún producto: PRY-202, 205, 208, 209 y 210.

**Dónde quedó:** los archivos están en `espacio/reportes/` (25 páginas).
- `index.html` es la vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- `decisiones.html` es la vista por decisión. Es para el patrocinador y el comité.
- También hay una página por proyecto y por producto.
- Para sacar el PDF, imprima el HTML desde el navegador.

**Problemas en el camino:**
- La primera generación cayó en `estado/reportes` porque mi directorio de trabajo había cambiado. La borré y regeneré el informe en la carpeta de la configuración.
- No hay confirmación mensual de campos: nadie podía responder en esta sesión, así que queda para la próxima corrida.
- En el resumen de la corrida escribí que no hay dependencias en riesgo. Esa afirmación no la comprobé contra la salida de `compute`, así que revísela antes de darla por cierta.

La corrida quedó registrada como `2026-10-17-portfolio-report-1`, con el texto completo en `estado/corridas/salida-portfolio-report.md`.

Criterio Portfolio 0.3.13 · fichas aplicadas: 13, del 2026-10-17 · campos inciertos: la autoridad de los 13 proyectos · Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.13

Si hay comité cerca (el próximo es el 2026-10-24), puedo preparar el material con `/steering-pack`. También puedo entrar al detalle de los proyectos con más señales: PRY-200, PRY-206 y PRY-202.