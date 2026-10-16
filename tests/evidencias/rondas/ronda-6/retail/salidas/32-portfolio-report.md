# /criterio-portfolio:portfolio-report html

Generé el informe HTML del portafolio: 24 páginas en `/home/claude/banco/ronda-6/retail/espacio/reportes`, 13 proyectos, 7 productos. Corrí `informe.py` con la configuración del proyecto, así que el script escribió ahí, que es la carpeta que sirve Rostrum. Abrí en esta carpeta, no abrí las páginas para revisarlas.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16, plugin 0.3.12). No hubo que mostrarlos ni registrarlos de nuevo.
- **Fichas:** cargué 13 de `estado/records`, todas del barrido de hoy, así que ninguna está vieja.
- **Cambios:** el diff dio 0 cambios, porque la instantánea anterior es de hoy. Esto es un punto de partida, no una comparación entre semanas.

**Qué vista va a cada audiencia**
- `index.html` es la vista por campo, con la cadena de evidencia completa. Es para quien va a actuar.
- `decisiones.html` es la vista por decisión, para el patrocinador.
- Cada proyecto tiene su página. El PDF sale de imprimir el HTML.

**Hallazgos (76 señales en 11 de los 13 proyectos)**
- **Verdes contradichos:** 7 proyectos se declaran en verde y la evidencia no los sostiene: PRY-200, 201, 203, 204, 205, 206 y 209.
- **PRY-206 (Precios dinámicos):** declara 21 % de avance con los 5 hitos cumplidos. Tiene 5 compromisos vencidos, 5 sin fecha y 3 reprogramados (hasta 5 veces). Su fecha de fin, 2026-08-31, ya pasó.
- **PRY-209 (Migración del ERP):** lleva 70 días de atraso contra la línea base original. El proveedor facturó COP 275.224.201 sin ningún entregable aceptado.
- **PRY-210 (Etiquetas electrónicas):** 140 días de atraso, de los cuales 27 se replanificaron sin autorización.
- **Hitos vencidos:** PRY-205, 207 y 210.
- **Sin hallazgos:** PRY-199 y PRY-202. En PRY-202 la fecha de fin, 2026-04-24, ya pasó y la ficha no lo señala.
- **Vacíos:** los 13 proyectos no tienen autoridad ni fase, y 6 no tienen producto asociado.

**Errores o puntos a revisar**
- En `salida-portfolio-report.md` dejé las cinco preguntas de confirmación con la respuesta sugerida, porque nadie podía responder. La 3 (evidencia de los hitos de PRY-209) y la 5 (autorización de los 27 días de PRY-210) son sobre todo preguntas para quien escala, no campos de la ficha.
- La corrida quedó registrada como `2026-10-16-portfolio-report-1`, con 47 segundos medidos y 82 documentos sin cambio. El informe en pantalla está en `estado/corridas/salida-portfolio-report.md`, con el pie de versión, fichas, campos inciertos y enlace a los términos.

Siguiente paso sugerido: el material de comité del 2026-10-23, o entrar al detalle de PRY-206, PRY-209 y PRY-210.