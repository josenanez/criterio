# /criterio-legal:legal-setup legal/899999101-instituto-publico-de-fomento-andino

Dejé a Fidel instalado sobre el Instituto Público de Fomento Andino (NIT 899999101), con las fichas de los 6 contratos hechas y la corrida registrada.

**Carpeta e inventario.** Usé `legal/899999101-instituto-publico-de-fomento-andino`, la que venía en el argumento. Tiene 63 documentos, 6 contratos, el registro de contratos y la matriz de atribuciones. Solo `00-referencia/politica-contratacion.md` está fuera de la estructura recomendada, porque iría en `20-politicas/`. No moví nada.

**Respuestas tomadas de los documentos:**
- **Entidad pública:** sí. La política de contratación dice que contrata bajo la ley de contratación pública y publica en SECOP II. El umbral de garantía no aplica en Colombia y quedó vacío.
- **Avisos y certificado:** 60 días para vencimientos, 30 para preavisos y 30 para la antigüedad máxima del certificado. Los documentos no fijan estos valores, así que tomé los de `config.example.json`.
- **Estado:** `estado-legal/899999101-instituto-publico-de-fomento-andino`, fuera de la carpeta de documentos.
- **Términos v1.3:** los aceptó José Francisco Ñáñez el 2026-10-06. El comprobante quedó en `.criterio/terminos/`.
- **Marca `_CRITERIO_LEGAL.txt`:** no la pregunté ni la escribí, porque la sesión no tiene interfaz.

**Fichas.** Procesé los contratos CTR-1901 a CTR-1906 y no quedó ningún `record_issues`. En CTR-1902 el otrosí OT-1 mueve la terminación a 2027-12-31, y en CTR-1905 el acta del 2026-09-18 decide renovar. CTR-1902 no tiene constancia de publicación, así que su fecha de publicación quedó en `null`.

**Señales.** El cálculo da 5: 2 garantías por debajo de la ley y 3 contratos públicos sin publicar. No las detallé, porque ese detalle lo dan los comandos de revisión y no el calendario.

**Calendario al 2026-10-06** (copiado del reporte del motor):

| Fecha | Contrato | Qué | Días |
|---|---|---|---|
| 2026-09-30 | CTR-1901 | OBL-3, reporte de operaciones al oficial de cumplimiento (con evidencia) | -6 |
| 2026-11-20 | CTR-1905 | terminación, y OBL-2 informe final y acta de liquidación | 45 |
| 2026-12-31 | CTR-1903 | terminación, y OBL-2 informe final y acta de liquidación | 86 |

El calendario no marca nada abierto que atender. La decisión de renovar o terminar es de una persona.

**Archivos** (en `estado-legal/899999101-instituto-publico-de-fomento-andino/`):
- `contratos/CTR-1901.json` a `CTR-1906.json`
- `contratos/reporte-obligations-calendar.md`
- `corridas/salida-legal-setup.md`

La corrida quedó como `2026-10-06-legal-setup-1`, con 5 hallazgos.