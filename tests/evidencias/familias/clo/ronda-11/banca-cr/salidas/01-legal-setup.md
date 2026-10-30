# /criterio-legal:legal-setup legal/3101457812-banco-del-valle-central-sintetico

Fidel quedó instalado sobre Banco del Valle Central Sintético: procesó los 6 contratos y, al corte del 2026-10-06, el calendario trae dos asuntos por atender.

**Qué se instaló**
- **Configuración:** `.criterio/legal/3101457812/config.json`. Pasó la validación sin problemas. Entidad Banco del Valle Central Sintético, Costa Rica, colones, no pública, avisos de 60 y 30 días, certificado de 30 días como máximo.
- **Términos:** versión 1.3, aceptados a nombre de José Francisco Ñáñez el 2026-10-06 para esta prueba. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Fichas:** 6, de CTR-3601 a CTR-3606, en `estado-legal/3101457812-banco-del-valle-central-sintetico/contratos/`. Salieron sin `record_issues`.

**Qué hay que atender**
1. **CTR-3601:** el preaviso de no renovación venció el 2026-10-01 sin una decisión registrada, así que el contrato se prorroga en sus términos el 2026-10-31.
2. **CTR-3604:** el informe mensual de agosto (OBL-1) venció el 2026-09-05 y no hay evidencia en `40-ejecucion/`.

El cálculo marcó además tres señales que este comando no detalla: una firma sin facultad, un pago por encima del valor y una garantía que vence antes de lo exigido. Las revisan authority-check, contract-execution y contract-register. Yo no las revisé.

**Decisiones mías sin confirmar**
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos, porque nadie lo autorizó. Si quieres la marca, dímelo.
- **Valores supuestos:** que la entidad no es pública, los avisos de 60 y 30 días y los 30 días del certificado salen del ejemplo, no de los documentos. Además dejé el festivo 2026-10-12 que traía el ejemplo; no lo ajusté a Costa Rica.

Dejé la salida y el registro de la corrida en `corridas/salida-legal-setup.md`.