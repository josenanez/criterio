# /criterio-legal:legal-setup legal/1760001230001-empresa-publica-sierra-norte-ep

Fidel quedó instalado sobre Empresa Pública Sierra Norte EP (RUC 1760001230001, Ecuador, USD): seis contratos procesados, y el motor encontró dos garantías por debajo de lo que pide la ley.

**Instalación**
- **Documentos:** hay 6 contratos, el registro y la matriz de atribuciones. `00-referencia/politica-contratacion.md` iría en `20-politicas/`; no la moví.
- **Configuración:** quedó en `.criterio/legal/1760001230001/config.json` y el motor la validó sin problemas. El estado va en `estado-legal/1760001230001-empresa-publica-sierra-norte-ep`.
- **Preguntas:** las tomé de los documentos o de `config.example.json`. Entidad pública, con umbral de garantía de 100,000.00 USD según la política de contratación. Avisos de 60 días para vencimientos y 30 para preavisos, y certificado de 30 días como máximo.
- **Términos:** los mostré tal cual (versión 1.3) y registré la aceptación de José Francisco Ñáñez el 2026-10-06. Los comprobantes están en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie autorizó escribir dentro de los documentos.
- **Festivos:** dejé solo el 2026-10-12 del ejemplo. Los documentos no traen el calendario de Ecuador.

**Fichas y señales**
- Convertí 35 documentos y escribí las 6 fichas en `contratos/`. No quedaron `record_issues`.
- **CTR-2001:** la garantía de cumplimiento es de 9,600.00 y la ley pide al menos el 5 % del valor, 16,000.00.
- **CTR-2003:** la garantía es de 7,200.00 y la ley pide al menos 12,000.00.

**Calendario al 2026-10-06**
- **CTR-2001, OBL-3:** el reporte al oficial de cumplimiento vencía el 2026-09-30 y tiene evidencia entregada ese día.
- **CTR-2005:** termina el 2026-11-20, en 45 días. El acta del 2026-09-18 decidió renovarlo.
- **CTR-2003:** termina el 2026-12-31, en 86 días. Las dos terminaciones traen su informe final y acta de liquidación sin evidencia todavía.

El motor no marcó nada abierto en el calendario. La decisión de renovar o terminar es de una persona.

Registré la corrida como `2026-10-06-legal-setup-1`. El reporte completo está en `estado-legal/1760001230001-empresa-publica-sierra-norte-ep/contratos/reporte-obligations-calendar.md`, y lo que te mostré en `estado-legal/1760001230001-empresa-publica-sierra-norte-ep/corridas/salida-legal-setup.md`.