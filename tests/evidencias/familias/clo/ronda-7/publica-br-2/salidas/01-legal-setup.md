# /criterio-legal:legal-setup legal/45678912000155-empresa-publica-paulista

Fidel quedó instalado sobre Empresa Pública Paulista (CNPJ 45678912000155) y procesó los 6 contratos, sin `record_issues`. El calendario de obligaciones al 2026-10-06 tiene 5 filas, y el motor calculó 4 señales de contratación pública que no están detalladas.

- **Inventario:** están el registro de contratos y la matriz de atribuciones. `00-referencia/politica-contratacao.md` está fuera de la estructura recomendada (iría en `20-politicas/`). No moví nada.
- **Configuración:** quedó en `.criterio/legal/45678912000155/config.json`, con país BR, moneda BRL, entidad pública y umbrales de `config.example.json`. Las respuestas salieron de los documentos, sin preguntar a nadie.
- **Términos:** la versión 1.3 queda aceptada por José Francisco Ñáñez el 2026-10-06. Los comprobantes están en `.criterio/terminos/` (`.md` y `.pdf`).
- **Marca `_CRITERIO_LEGAL.txt`:** no la dejé en la carpeta de documentos, porque ningún documento la autoriza.

**Calendario (al 2026-10-06):**

| Fecha | Contrato | Qué | Días |
|---|---|---|---|
| 2026-09-30 | CTR-2401 | OBL-3, relatório de operações ao responsável de compliance | -6 |
| 2026-11-20 | CTR-2405 | terminación y OBL-2 | 45 |
| 2026-12-31 | CTR-2403 | terminación y OBL-2 | 86 |

La OBL-3 de CTR-2401 aparece con evidencia; las otras no la tienen todavía. Las 4 señales de contratación pública son `public_contract_not_published` (2) y `public_guarantee_over_cap` (2). No las detallé porque salen en los comandos de revisión.

Quedó registrada la corrida `2026-10-06-legal-setup-1`, con 4 hallazgos.

Archivos están en `estado-legal/45678912000155-empresa-publica-paulista/`:
- `contratos/reporte-obligations-calendar.md`
- `corridas/salida-legal-setup.md`