# /criterio-legal:legal-setup legal/20730000015-minera-puna-alta

Fidel quedó instalado sobre Minera Puna Alta (RUC 20730000015, PE, PEN), con las fichas de los 7 contratos hechas y la corrida registrada. El motor encontró 4 señales.

**Qué se hizo**
- **Carpeta y configuración:** usé `legal/20730000015-minera-puna-alta` y la marqué con `_CRITERIO_LEGAL.txt`. No pregunté nada, como pediste. La configuración quedó en `.criterio/legal/20730000015/config.json` y el motor la validó sin problemas.
- **Términos:** acepté la versión 1.2 a nombre de José Francisco Ñáñez, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-0.10.0-2026-10-06.md`, con su PDF al lado.
- **Fichas:** escribí 7, CTR-801 a CTR-807. El motor no reportó `record_issues`. Los datos salen de los documentos. En CTR-802 la fecha de la obligación OBL-2 (informe final y acta de liquidación) es el 2027-12-31, que es la terminación según el otrosí, no la del contrato original.

**Lo que encontró**
1. **CTR-802:** se pagó 954,000.00 contra 900,000.00 con otrosíes, 54,000.00 de más (filas 6 y 7 de los pagos).
2. **CTR-803:** el registro lo marca vigente, pero terminó el 2026-08-31.
3. **CTR-807:** el contrato está en la carpeta y no en el registro.
4. **CTR-804:** el certificado de la contraparte tenía 75 días cuando se firmó.

**Calendario (30 días atrás a 90 adelante)**
- **CTR-801:** el reporte al oficial de cumplimiento vencía el 2026-09-30 y tiene su evidencia.
- **CTR-805:** termina el 2026-11-20, a 45 días. El informe final y el acta de liquidación vencen ese mismo día y aún no tienen evidencia. El acta del comité del 2026-09-18 decide renovarlo; la decisión es de una persona.

**Dos respuestas que tomé yo, para que las revises**
- **Marca de la raíz:** dije que sí, la respuesta sugerida.
- **Feriados:** dejé la lista vacía, porque los documentos no los traen. Los de Perú se pueden añadir después.

Los archivos están en `estado-legal/20730000015-minera-puna-alta/`:
- `contratos/reporte-obligations-calendar.md` (el reporte completo)
- `corridas/salida-legal-setup.md` (lo mostrado, tal cual)