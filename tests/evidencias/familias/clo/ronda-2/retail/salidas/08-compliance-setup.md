# /criterio-compliance:compliance-setup legal/900765432-almacenes-caribe

Constanza quedó instalada sobre Almacenes Caribe (NIT 900765432). El periodo evaluado es 2026-09, y las 10 obligaciones de la matriz ya están contra su evidencia.

El informe de septiembre declara el periodo **cumplido**, pero el motor encontró 4 señales abiertas:

1. **OB-09, Reporte mensual de quejas (Felipe Arango), está vencida.** Venció el 2026-10-05 y no hay evidencia. Septiembre no trae ningún archivo OB-09.
2. **Lo declarado no cuadra con la evidencia.** El informe dice "cumplido" y hay señales abiertas que ese estado no explica.
3. **OB-13, Reporte de regalos e invitaciones, no cita su fuente.** Tiene evidencia, pero la matriz no dice de qué norma, contrato o política sale.
4. **Hay una revisión de política vencida** (`policy_review_overdue`). El motor la cuenta, pero el reporte no la lista en "Lo que hay que atender". No sé cuál política es: está en `resultados.json` y la dará `/policy-review`.

El avance con evidencia es 72,73 %, ponderado por criticidad. OB-04 y OB-05 están en plazo, sin evidencia todavía.

Tres cosas de la instalación:
- **Configuración:** el motor no la crea, así que la escribí yo en `.criterio/cumplimiento/900765432/config.json`, con el formato de `config.example.json`. Las fichas de Fidel las encontré en `estado-legal/900765432-almacenes-caribe/contratos`.
- **Términos:** los mostré y los registré a nombre de José Francisco Ñáñez, con fecha 2026-10-06.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt`. Nadie podía autorizarlo en esta sesión de prueba.

El reporte completo está en `estado-legal/900765432-almacenes-caribe/cumplimiento/2026-09/reporte-compliance-status.md`. Lo que te mostré quedó en `corridas/salida-compliance-setup.md`, y la corrida se registró como `2026-10-06-compliance-setup-1`.