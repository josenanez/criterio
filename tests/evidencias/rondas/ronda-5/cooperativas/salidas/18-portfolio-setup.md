# /criterio-portfolio:portfolio-setup documentos/proyectos

Dejé la instalación lista y probé con tres proyectos: PRY-209, PRY-206 y PRY-208. La mayor señal es el verde de PRY-206, que contradice sus propios documentos. Nadie podía responder, así que tomé el valor propuesto en cada decisión y no hice ninguna pregunta.

**Qué configuré**
- **Documentos:** miré 75 documentos en 13 proyectos, de los que 3 pasaron por la prueba. El más reciente es del 2026-10-16.
- **Rol:** PMO del portafolio.
- **Comité:** semanal, con el primero propuesto para el 2026-10-23. El informe llega dos días antes, en presentación.
- **Rutas:** el estado queda en `estado/` y los informes en `reportes/`.
- **Términos:** aceptados a nombre de José Francisco Ñáñez para la versión 0.3.11 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.11-2026-10-16.md` y `.pdf`.
- **Verificación:** `config` pasó sin problemas.

**Lo que encontró el cálculo** (16 señales en total; por error, la nota de la corrida registrada dice 14):

| Proyecto | Declara | Señales |
|---|---|---|
| PRY-206 Pagos con QR | verde, 53 % | 8: los 3 hitos figuran cerrados sin ningún acta; el avance declarado queda 47 puntos por debajo de lo que sostiene el plan; la proyección de costo sube 16,2 % sobre lo aprobado; 2 compromisos vencidos |
| PRY-208 Motor de crédito | rojo, 45 % | 5: 2 hitos cerrados sin acta; el avance declarado queda 30 puntos por debajo del plan; la proyección de costo sube 18,6 %; el cronograma v2 mueve el piloto 38 días mientras la CC-01 sigue pendiente de comité |
| PRY-209 Convenios de libranza | verde, 26 % | 3: 68 días de atraso contra la línea base original (13 %); 1 compromiso vencido |

**Lo que le falta a la carpeta**
- Ninguna acta de constitución dice hasta qué monto decide el gerente ni en qué etapa está el proyecto.
- Hay pocas actas de recibo.
- La CC-01 de PRY-209 dice «autorizada por el comité» sin nombrar cuál.
- Los riesgos no traen dueño, probabilidad ni fecha.

**El portafolio completo.** Quedan 10 proyectos y 65 documentos, que tomarían unos 30 minutos.

**Una salvedad.** Hay una carpeta previa `estado/PRY-211-cobranza-digital` de otra corrida. No la toqué.

Todo quedó en `estado/corridas/`: el resultado completo en `salida-portfolio-setup.md` y la corrida registrada como `2026-10-16-portfolio-setup-1`.