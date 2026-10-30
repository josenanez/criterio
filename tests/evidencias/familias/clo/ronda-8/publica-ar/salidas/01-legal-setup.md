# /criterio-legal:legal-setup legal/30699991011-organismo-publico-del-litoral

Fidel quedó instalado sobre Organismo Público del Litoral (CUIT 30699991011). Los 6 contratos están procesados y el calendario está generado.

- **Inventario:** hay 6 contratos y están el registro y la matriz de atribuciones. `00-referencia/politica-contratacion.md` está fuera de lugar y iría en `20-politicas/`. No moví nada.
- **Respuestas de la prueba:** como nadie contestaba, las tomé de los documentos.
  - **Entidad pública:** la política de contratación dice que publica en COMPR.AR. Quedó país AR, moneda ARS y entidad pública.
  - **Umbral de garantía:** ningún documento lo da, así que no lo registré.
  - **Avisos:** usé los de `config.example.json`: 60 días para vencimientos, 30 para preavisos y 30 de antigüedad máxima del certificado.
  - **Estado:** quedó en `estado-legal/30699991011-organismo-publico-del-litoral`.
- **Marca de la raíz:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie la autorizó.
- **Términos:** la versión 1.3 quedó aceptada por José Francisco Ñáñez el 2026-10-06. El comprobante está en `.criterio/terminos/`.
- **Configuración:** `.criterio/legal/30699991011/config.json`. El motor la validó sin problemas.
- **Fichas:** convertí 35 documentos y escribí las 6 fichas, sin `record_issues`. El motor calculó 5 señales: `public_guarantee_below_law` 2 y `public_guarantee_late` 3. No las detallé, porque pertenecen a otros comandos.
- **Calendario:** no hay nada abierto. Para el 2026-10-06 muestra:

| Fecha | Contrato | Qué | Días |
|---|---|---|---|
| 2026-09-30 | CTR-2801 | OBL-3, reporte al oficial de cumplimiento (con evidencia) | -6 |
| 2026-11-20 | CTR-2805 | terminación e informe final / acta de liquidación | 45 |
| 2026-12-31 | CTR-2803 | terminación e informe final / acta de liquidación | 86 |

Dos puntos quedan para una persona:
- CTR-2801 y CTR-2802 traen el mismo CUIT de la contraparte, 30702800028. Lo registré tal como figura en cada documento.
- Si hay un umbral de garantía vigente para la entidad, hay que dárselo al motor.

La corrida quedó registrada como `2026-10-06-legal-setup-1`. La salida completa está en `estado-legal/30699991011-organismo-publico-del-litoral/corridas/salida-legal-setup.md`, y el reporte del calendario en `estado-legal/30699991011-organismo-publico-del-litoral/contratos/reporte-obligations-calendar.md`.