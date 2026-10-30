# /criterio-legal:legal-setup legal/61999010-2-servicio-publico-del-maipo

Fidel quedó instalado sobre Servicio Público del Maipo, con los seis contratos procesados y la corrida registrada.

**Carpeta y respuestas**
- La carpeta es `legal/61999010-2-servicio-publico-del-maipo`, que llegó como argumento. Tiene 6 contratos, el registro de contratos y la matriz de atribuciones.
- No moví nada. `00-referencia/politica-contratacion.md` está fuera de la estructura recomendada y iría en `20-politicas/`.
- Nadie respondió preguntas, así que tomé las respuestas de los documentos:
  - La entidad es Servicio Público del Maipo, 61999010-2, Chile, CLP.
  - Es pública, con garantía de cumplimiento exigida desde 62.500.000 CLP, según la política de contratación.
  - Los avisos son de 60 y 30 días, y el certificado puede tener hasta 30 días. Son los valores de `config.example.json`.
- No dejé la marca `_CRITERIO_LEGAL.txt` en la carpeta, porque nadie autorizó escribir dentro de los documentos.

**Términos**
- Registré la aceptación de la versión 1.3 a nombre de José Francisco Ñáñez, con fecha 2026-10-06.
- El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-1.0.0-2026-10-06.md` y `.pdf`.

**Fichas y señales**
- Convertí 35 documentos y armé las 6 fichas, sin `record_issues`.
- El cálculo dejó 3 señales de contratación pública: 2 de garantía de cumplimiento bajo el mínimo de la ley y 1 de contrato público sin publicar.
- El calendario no las detalla. Para ver qué contratos son, hay que correr los comandos de revisión de ejecución y de registro.

**Calendario al 2026-10-06**

| Fecha | Contrato | Qué | Días |
|---|---|---|---|
| 2026-09-30 | CTR-2201 | OBL-3, reporte de operaciones al oficial de cumplimiento (con evidencia) | -6 |
| 2026-11-20 | CTR-2205 | terminación y OBL-2, informe final y acta de liquidación | 45 |
| 2026-12-31 | CTR-2203 | terminación y OBL-2, informe final y acta de liquidación | 86 |

- Nada queda abierto en lo que procesa este comando.
- La decisión de renovar o terminar es de una persona.

**Archivos**
- Configuración: `.criterio/legal/61999010-2/config.json`.
- Fichas y reporte: `estado-legal/61999010-2-servicio-publico-del-maipo/contratos/`.
- Salida completa de la corrida: `estado-legal/61999010-2-servicio-publico-del-maipo/corridas/salida-legal-setup.md`.