# /criterio-compliance:compliance-setup legal/155731001-2-2016-banco-istmeno

Constanza quedó instalada sobre Banco Istmeño (155731001-2-2016) y el primer estado del periodo 2026-09 está calculado.

El informe del periodo declara «cumplido», pero la evidencia no lo sostiene del todo. El avance con evidencia es 68.18 % (ponderado por criticidad). El motor levantó 5 señales:

- **Declarado contra evidencia:** el informe del 2026-10-05 dice «cumplido» y hay 4 señales abiertas que ese estado no explica.
- **OB-10 (Luis Quintero):** figura cumplida y no hay ningún archivo de evidencia que empiece por OB-10.
- **OB-11 (Itzel Batista):** la última evidencia es de 2026-07 y el ciclo anterior no tiene.
- **Caso C-003 del canal de denuncias:** recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15.
- **Norma N-2026-04:** aplica y ninguna obligación de la matriz la cita.

El reporte tabula solo las tres primeras. Las dos últimas salen en `resultados.json`; las muestran `reports-cases` y `regulatory-watch`.

- **Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 y quedó el comprobante en Markdown y PDF en `.criterio/terminos/`.
- **Matriz:** revisé las 10 obligaciones. No les completé nada que no estuviera en los documentos.
- **Preguntas:** hice 3, todas con la respuesta sugerida por los documentos:
  - el periodo a evaluar es 2026-09;
  - las fichas de Fidel están en `estado-legal/155731001-2-2016-banco-istmeno/contratos`;
  - los plazos son 15 días para responder denuncias y 30 para evaluar una norma, los valores por defecto.
- **Marca `_CRITERIO_LEGAL.txt`:** no la dejé, porque nadie pudo autorizarla en esta prueba.
- **Glob:** no estaba disponible en esta sesión y usé `find`.
- **Nota de la corrida:** la corrida registrada nombra C-003 y N-2026-04. Las puse antes de comprobarlas y después las confirmé contra `resultados.json`.

Archivos en `<espacio>/`:
- `.criterio/cumplimiento/155731001-2-2016/config.json`
- `estado-legal/155731001-2-2016-banco-istmeno/cumplimiento/2026-09/ficha.json`
- `estado-legal/155731001-2-2016-banco-istmeno/cumplimiento/2026-09/reporte-compliance-status.md`
- `estado-legal/155731001-2-2016-banco-istmeno/corridas/salida-compliance-setup.md`