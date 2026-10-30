# /criterio-legal:legal-setup legal/155699101-2-2021-autoridad-publica-del-istmo

Fidel quedó instalado sobre Autoridad Pública del Istmo (RUC 155699101-2-2021). Procesé los 6 contratos y el motor no reportó problemas en ninguna ficha.

**Lo que encontré**
- **Garantía de cumplimiento (2 contratos):** CTR-3201 (200.000 USD) y CTR-3203 (150.000 USD) la exigen en la cláusula 9, pero no hay póliza en `20-garantias/`. Ambos superan los 50.000 USD desde los que la ley exige garantía. El motor lo marcó cuatro veces, dos por cada contrato.
- **Calendario (30 días atrás a 90 adelante):**
  - El reporte al oficial de cumplimiento de CTR-3201 vencía el 2026-09-30 y está entregado ese mismo día.
  - CTR-3205 termina el 2026-11-20. El comité decidió renovarlo en el acta del 2026-09-18.
  - CTR-3203 termina el 2026-12-31 y no se prorroga automáticamente.
  - Ni CTR-3205 ni CTR-3203 tienen todavía el informe final ni el acta de liquidación, que vencen en esas fechas.
- No corrí el chequeo de firmas ni el de pagos. La instalación solo arma el calendario.

**Lo que decidí por mi cuenta**
- **Configuración:** los umbrales son los del ejemplo (60 días para vencimientos, 30 para preavisos, 30 para el certificado) y la moneda es USD, porque Panamá no la trae definida. En Panamá no hay umbral de garantía que registrar.
- **Términos:** versión 1.3, aceptados a nombre de José Francisco Ñáñez el 2026-10-06. El comprobante está en `.criterio/terminos/`.
- **Raíz de documentos:** no la marqué con `_CRITERIO_LEGAL.txt`, porque nadie podía autorizarlo en esta prueba. No moví ni renombré nada en los documentos.
- **Archivo fuera de lugar:** `00-referencia/politica-contratacion.md` iría en `20-politicas/` según la estructura recomendada.

**Dónde quedó**
- Configuración: `.criterio/legal/155699101-2-2021-autoridad-publica-del-istmo/config.json`
- Fichas: `estado-legal/155699101-2-2021-autoridad-publica-del-istmo/contratos/`
- Reporte: `estado-legal/155699101-2-2021-autoridad-publica-del-istmo/contratos/reporte-obligations-calendar.md`
- Corrida registrada: `estado-legal/155699101-2-2021-autoridad-publica-del-istmo/corridas/salida-legal-setup.md`