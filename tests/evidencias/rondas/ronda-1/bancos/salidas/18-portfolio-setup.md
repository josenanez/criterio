# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos

**Miré:** 69 documentos en 13 proyectos. Los formatos son .md 25, .docx 14, .pdf 14, .xlsx 8, .csv 6, .json 1 y .txt 1. El más reciente es del 2026-10-14.
**Eres:** PMO del portafolio, porque hay 13 proyectos.
**Te aviso:** dos días antes del comité semanal. Supuse el primer comité el 2026-10-20, una semana después del último que vi (2026-10-13). El informe llegaría el 2026-10-18.
**En:** presentación. La configuración la guarda como página HTML.
**Términos:** los acepta José Francisco Ñáñez el 2026-10-14 (prueba sin interfaz).
**Dónde queda:** la configuración está en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes irán a `reportes/`.

No hice ninguna pregunta, porque en esta sesión nadie responde. Tomé las respuestas sugeridas y las dije arriba. Pasaron unos 10 minutos hasta el primer resultado.

### Probé con tres proyectos

Elegí PRY-205, PRY-206 y PRY-207, los de documentación más reciente. Escribí sus tres fichas, las sellé y corrí `compute`. Lo que sigue sale de `compute`, que levantó 12 señales.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-205 Prevención de lavado de activos | 6 | Gerente Andrés Lozano, patrocinadora Sandra Gil. Declara amarillo, 56 %. Presupuesto 6.800 M COP. Cierre comprometido 2026-12-24; el cronograma v2 mueve la integración con el core a 2027-02-20 | Facultad del gerente, fase y proveedores. Dependencias dice "ninguna declarada", aunque el informe cita el calendario de liberaciones del core |
| PRY-206 Billetera y QR | 5 | Gerente Carlos Peña, patrocinadora Laura Vélez. Declara amarillo, 32 %. Presupuesto 18.000 M COP. Hay un acta de recibo, la del diseño funcional del 2026-10-09 | Facultad del gerente, fase, proveedores y el acta de recibo del ambiente de pruebas |
| PRY-207 Onboarding PyME | 3 | Gerente Beatriz Cuéllar, patrocinador Jorge Medina. Declara verde, 72 %. Presupuesto 3.300 M COP; proyección al cierre 4.056 M | Facultad del gerente, fase, cronograma, hitos y acta de comité |

**PRY-205**
- Va 101 días (39,3 %) atrasado contra la línea base original.
- La solicitud de cambio CC-01 (+101 días, +202 M COP) sigue pendiente de presentarse al comité, pero el cronograma v2 ya usa la fecha nueva.
- Declara 56 % y el plan sostiene entre 67 y 100 %.
- Dos hitos figuran cerrados sin acta que lo pruebe: Diseño funcional aprobado y Ambiente de pruebas certificado.
- Natalia Ospina tiene un compromiso sin fecha: "Entregar el punto 37", plazo "por definir".

**PRY-206**
- Declara 32 % y el plan sostiene entre 50 y 75 %.
- El hito Ambiente de pruebas certificado figura cerrado sin acta de recibo.
- Diana Molina tiene un compromiso vencido hace 22 días: "Entregar el punto 3", plazo 2026-09-22.

**PRY-207**
- Declara verde, pero la proyección al cierre supera el presupuesto aprobado en 22,9 %.
- La CC-01 (+25 días) figura autorizada por el comité, pero ninguna línea base nueva la recoge.
- Los datos de identidad y de plan se apoyan solo en el acta de 2025-06-02, sin confirmación posterior en 16 meses.

### El portafolio completo
Quedan 10 proyectos y 53 documentos, en dos lotes uno tras otro. Estas tres fichas tomaron pocos minutos, así que calculo entre 20 y 30 minutos para el resto. Es una estimación mía, no una medición.

### Lo que le falta a tu carpeta
Ninguno es bloqueante.
- En los tres proyectos faltan la facultad del gerente (hasta qué monto decide sin subir a comité) y la fase.
- PRY-205 y PRY-206 tienen hitos cerrados sin acta de recibo en la carpeta. No quiere decir que no existan.
- PRY-207 no tiene cronograma ni acta de comité, así que no se puede juzgar su plan.
- Los compromisos de comité llegan con plazo "por definir".
- Las actas traen alcance genérico ("Componente 1, 2, 3") y "Dependencias: ninguna declarada". Con eso no hay de dónde sacar cruces entre proyectos.

### Después
¿Corro el portafolio completo? Si tu equipo tiene gerentes de proyecto, puedo publicar el estándar en una carpeta compartida para que usen los mismos criterios.

La salida quedó en `estado/corridas/salida-portfolio-setup.md`. La corrida quedó registrada como `2026-10-14-portfolio-setup-1`.