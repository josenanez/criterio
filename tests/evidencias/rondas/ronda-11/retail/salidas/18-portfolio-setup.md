# /criterio-portfolio:portfolio-setup documentos/proyectos

Dejé Vera instalada y probada con tres proyectos: PRY-201, PRY-204 y PRY-210. Nadie respondió preguntas, así que tomé el valor sugerido en cada una (0 preguntas hechas). Hay dos supuestos tuyos por corregir y dos fallos del paso final, abajo.

**Qué quedó configurado**
- **Rol y cadencia:** PMO del portafolio, con comité cada dos semanas. Puse el próximo el 2026-11-06 y el aviso dos días antes. Esa fecha es un supuesto mío.
- **Formato del informe:** presentación (`pptx`).
- **Dónde guarda:** documentos en `documentos/proyectos`, estado en `estado` e informes en `reportes`. Todo está en `.criterio/portafolio/config.json`.
- **Términos:** versión 1.2 de los términos, aceptada a nombre de José Francisco Ñáñez el 2026-10-23, según tu instrucción. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-portfolio-0.8.0-2026-10-23.md` y `.pdf`.
- **Marca de carpeta:** no dejé `_CRITERIO_PORTAFOLIO.txt` en tus documentos. Nadie podía autorizarlo y es lo único que un agente escribe ahí.

**Qué encontré en los tres proyectos** (86 documentos, 13 proyectos; 14 señales en total)
- **PRY-201 (9 señales):**
  - **Plazo:** el cierre se movió 82 días, de 2026-12-22 a 2027-03-14.
  - **Avance:** declara 69 %, pero 4 de sus 5 hitos figuran cerrados, un cuadro que respalda 80–100 %.
  - **Hitos sin acta:** Diseño, Ambiente de pruebas y Piloto figuran cerrados sin acta de recibo.
  - **Compromiso vencido:** el punto 36 de Laura Vélez venció el 2026-10-12.
  - **Proveedores:** tres entregables de proveedores atrasados.
  - **Estado:** el informe sigue en amarillo y no menciona ninguna de estas señales.
- **PRY-204 (4 señales):** declara rojo con 48 %, aunque sus 4 hitos están cerrados. Tres de ellos (Diseño, Ambiente de pruebas e Integración con el ERP) no tienen acta de recibo.
- **PRY-210 (1 señal):** la Bolsa de horas del proveedor CT-548 lleva 3 días de atraso.
- **Los tres:** las actas no dicen hasta qué monto puede decidir el gerente sin subir a comité.

**Qué falta en la carpeta**
- `PRY-209-migración-del-erp/10-plan/2026-02-17-cronograma-v1.xml` está en un formato que no leo sin instalar algo.
- PRY-202 tiene una nota de reunión suelta en la raíz del proyecto y un archivo `ficha-pm.json`.
- PRY-203, PRY-206 y PRY-208 solo tienen acta e informe, así que no se les puede medir atraso.

**Dos fallos del paso final**
- La nota de "El portafolio completo" en `estado/corridas/salida-portfolio-setup.md` se contradice. Dice "1 lote" y luego "2 lotes", y el segundo lote incluye a PRY-210, que ya probé. Lo correcto son 2 lotes y 10 proyectos por leer: del 199 al 208 y el 209, más PRY-211. Ya quedó registrada la corrida con esa versión y no la regeneré.
- El tiempo que dije ("unos 20–30 minutos") es una estimación mía, no una medición del script.

Siguiente paso: correr el portafolio completo con el comando `/criterio-portfolio:portfolio-scan`.