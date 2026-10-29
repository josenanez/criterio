# /criterio-portfolio:portfolio-setup documentos/proyectos

Quedó instalado y probado sobre tres proyectos, sin hacer ninguna pregunta. En las tres fichas, `compute` no devolvió `record_issues` y levantó 21 señales. La salida completa está en `estado/corridas/salida-portfolio-setup.md`, y la corrida quedó registrada como `2026-10-28-portfolio-setup-1`.

**Configuración**
- **Archivos:** la configuración está en `.criterio/portafolio/config.json`. El estado va en `estado/` y los informes en `reportes/`.
- **Valores tomados (los sugeridos):** rol PMO, comité semanal con próxima fecha 2026-10-31 (deducida del comité del 2026-10-24, corrígela si es otra) e informe dos días antes. El formato quedó como `html`.
- **Términos:** aceptados a nombre de José Francisco Ñáñez para la versión 0.12.1 (términos 1.3). El comprobante está en `.criterio/terminos/` en Markdown y PDF.
- **Archivo de marca:** `documentos/proyectos/_CRITERIO_PORTAFOLIO.txt` está puesto. Respondí que sí a la pregunta, que era la sugerida.

**Carpeta:** 74 documentos en 13 proyectos, el más reciente del 2026-10-28.

**Probé con PRY-204, PRY-200 y PRY-206**, los de documentación más reciente. PRY-200 y PRY-206 empataban en fecha con PRY-211, y me quedé con los dos que tienen más documentos.

Lo que más pesa:
- **PRY-206 (declara verde):** la línea base se movió 94 días y ningún documento lo autoriza. La solicitud CC-01 sigue pendiente de comité. Además, el hito de permisos figura cerrado sin acta.
- **PRY-204 (declara verde):** "Enviar el documento 1" lleva 6 reprogramaciones, y otros dos compromisos llevan 5 y 3. Hay 5 compromisos vencidos sin acta de recibo, y el avance declarado (53 %) va por debajo de los hitos cumplidos. Su `ficha-pm.json` quedó aparte en `pm_record` y no generó ninguna contradicción.
- **PRY-200 (declara rojo):** el cambio CC-01 cuadra con los 25 días que se movió el plan. Aun así, el informe muestra comprometido por debajo de ejecutado, y `compute` no lo señaló, así que lo dejé como punto para revisar a mano.

**Antes de correr el resto**
- Quedan 10 proyectos en 2 lotes. Mi estimado, no medido, es de 30 a 40 minutos.
- Cinco cronogramas `.xml` no los lee el script sin instalar algo. Yo los leí como texto, pero un barrido automático los perdería.
- No toqué la carpeta de estado de un agente de proyecto que hay dentro de `estado/PRY-204-…`.

¿Corro el portafolio completo?