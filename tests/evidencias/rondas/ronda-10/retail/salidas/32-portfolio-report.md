# /criterio-portfolio:portfolio-report html

# Portafolio — 2026-10-18
13 proyectos, 11 con hallazgos, 63 señales. Cargué las 13 fichas de `estado/records/` con fecha 2026-10-18. No comprobé por separado qué antigüedad tiene cada ficha.

**Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-18), así que no hizo falta registrarlos de nuevo. En corto: Criterio produce borradores de trabajo, no decisiones ni asesoría. Puede equivocarse, y la verificación es de quien lo usa. Nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Informe HTML** (24 páginas, en `/home/claude/banco/ronda-10/retail/espacio/reportes/`):
- `index.html` va a quien debe actuar. Está organizado por campo y trae la cadena de evidencia de cada dato.
- `decisiones.html` va al patrocinador y al comité. Está organizado por decisión.
- Hay además una página por proyecto y una por producto.

**Qué cambió:** nada. La instantánea de comparación es del mismo día, así que el diff da 0 cambios.

**Hallazgos principales** (cifras de `portafolio.py compute`):
- **Verdes contradichos (5):** PRY-200, PRY-201, PRY-202, PRY-204 y PRY-209 se declaran en verde, pero los documentos no lo sustentan.
- **PRY-206 Precios dinámicos:**
  - Va 53 días atrasado frente al plan original (25 %).
  - Tiene un cambio (CC-01) sin línea base.
  - Tiene 6 compromisos vencidos y 2 reprogramados 5 y 6 veces.
  - Un proveedor facturó sin entregar.
- **PRY-201 Fidelización:** el costo proyectado supera lo aprobado en 22,6 %. Se facturaron 107,5 M más de lo aceptado.
- **PRY-208 Domicilios:** el costo proyectado supera lo aprobado en 26,8 %. Declara 37 % de avance con los 5 hitos del plan cumplidos.
- **PRY-205:** el hito «Integración con el ERP» lleva 9 días vencido.
- **Hitos declarados cumplidos sin evidencia:** 21 en total, repartidos en 10 proyectos.
- **Sin señales:** PRY-199 y PRY-210.
- **Proyectos en silencio:** ninguno. El más callado es PRY-203, con 11 días.
- **Vacíos:** ningún proyecto tiene autoridad de aprobación registrada (13 de 13), y 6 no tienen producto asociado.

La confirmación mensual quedó vacía porque la sesión no tiene interfaz.

**Corrida registrada:** `2026-10-18-portfolio-report-1`. Duró 29 segundos y leyó 83 documentos, todos sin cambios y ninguno releído. La salida quedó en `estado/corridas/salida-portfolio-report.md`.

Si quiere, preparo el material de comité para el 2026-10-25 o entro al detalle de PRY-206, PRY-201 y PRY-208.

**Pie:** criterio-portfolio 0.5.0 · fichas del 2026-10-18 · campos inciertos: la autoridad de los 13 proyectos · términos en el enlace de arriba.