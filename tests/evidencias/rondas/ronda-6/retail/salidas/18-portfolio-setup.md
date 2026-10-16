# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos retail

**Miré:** 82 documentos en 13 proyectos (PRY-199 a PRY-211). Hay 32 en .md, 20 en .pdf, 13 en .docx, 8 en .xlsx, 7 en .csv, 1 en .json y 1 en .txt. El más reciente es del 2026-10-16.
**Eres:** PMO del portafolio, porque hay 13 proyectos.
**Te aviso:** dos días antes del comité del 2026-10-23, y cada semana después. Los comités de las carpetas caen en viernes y de ahí deduje la fecha.
**En:** presentación. Es el valor sugerido, porque nadie respondió.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.12 (términos 1.1). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.12-2026-10-16.md` y `.pdf`. El SHA-256 del Markdown empieza por 08da686bb7c9acf4…

La configuración quedó en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes irán a `reportes/`. La verificación de la configuración salió sin problemas.

### Probé con tres proyectos
Tomé PRY-200, PRY-202 y PRY-210, que tienen documentos del 2026-10-16. Las fichas quedaron escritas y selladas en `estado/records/`.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-200 Tienda en línea | 5 | Declara verde y 46 %. Cierre comprometido 2026-12-11. Ejecutado 2.855 M de 6.800 M COP; la proyección es 6.931 M (+1,9 %). | Facultad del gerente y fase. Actas de recibo de 2 de los 3 hitos cerrados. |
| PRY-202 Centro de distribución norte | 2 | Declara verde y 55 %. Ejecutado 1.090 M de 4.200 M COP; la proyección es 3.893 M (−7,3 %). El despliegue se reprogramó por el congelamiento de fin de año. | Cronograma e hitos, producto, facultad del gerente, fase y nueva fecha del despliegue. |
| PRY-210 Etiquetas electrónicas de precio | 6 | Declara amarillo y 57 %. Cierre original 2026-12-04, vigente 2027-04-23. Hay dos solicitudes de cambio: CC-01 pendiente y CC-02 autorizada. | Producto, facultad del gerente y fase. Actas de recibo de los 2 hitos cerrados. |

### Hallazgos (los que levantó el cálculo)
**PRY-200** declara verde y el cálculo lo contradice con tres señales:
- **Avance:** declara 46 %, pero 3 de sus 4 hitos están cerrados en el cronograma, lo que sostiene entre 75 y 100 %.
- **Hitos sin acta:** «Ambiente de pruebas certificado» e «Integración con el ERP» figuran cerrados sin acta que lo pruebe.
- **Compromiso vencido:** Javier Hoyos debía entregar «el punto 29» el 2026-10-02. El comité del 2026-10-11 lo registra sin cumplir (14 días).

**PRY-210** declara amarillo y tiene cinco señales:
- **Atraso:** el cierre se movió 140 días contra la línea base original (64,8 %).
- **Cambio sin autorizar:** solo 113 de esos 140 días están autorizados, por CC-02. Los 27 restantes son de CC-01, que sigue pendiente del comité.
- **Hito vencido:** «Integración con el ERP» venció el 2026-10-11 y sigue abierto.
- **Hitos sin acta:** «Diseño de la experiencia aprobado» y «Ambiente de pruebas certificado» figuran cerrados sin acta.

**PRY-202** no tuvo ninguna señal. Eso no significa que esté sano: sin cronograma el cálculo no tiene contra qué medirlo.

En total son 3 proyectos, 2 con señales, 10 señales y 1 verde contradicho.

### El portafolio completo
Faltan 10 proyectos (PRY-199, 201, 203 a 209 y 211) y 69 documentos, en 2 lotes uno tras otro. Calculo de una hora a hora y media de trabajo continuo; es una estimación, no una medida. PRY-206 trae 27 documentos, incluida una `ficha-pm.json` de su gerente que se lee aparte.

### Lo que le falta a tu carpeta
Ninguno es bloqueante.
- **Facultad del gerente:** ningún acta de los tres la declara, así que no se puede saber si un cambio excede lo que decide solo.
- **Actas de recibo:** en PRY-200 y PRY-210 hay hitos cerrados sin acta.
- **PRY-202 sin cronograma:** su acta fija el cierre en 2026-04-24, y el informe del 2026-10-16 sigue en 55 % sin dar nueva fecha.
- **CC-02:** dice «autorizada por el comité» sin nombrar cuál ni cuándo.
- **Datos viejos:** en PRY-200 y PRY-202 varios campos solo salen del acta de 2025, con más de 12 meses sin confirmación posterior.
- **Nota suelta:** `2026-10-16-notas-reunion.txt` de PRY-206 está fuera de las carpetas de reuniones.

**Preguntas y registro de la corrida:** no hice ninguna pregunta; tomé los valores sugeridos, con el nombre y la fecha de aceptación que indicó la prueba. No medí con precisión los minutos hasta el primer resultado. Dejé la salida completa en `estado/corridas/salida-portfolio-setup.md` y la corrida registrada como `2026-10-16-portfolio-setup-1`.

Puedo correr ahora el portafolio completo. También puedo publicar el estándar en una carpeta compartida para que los gerentes de proyecto usen los mismos criterios, pero el equipo no está definido todavía.