# /criterio-legal:legal-setup legal/155831003-2-2013-comercial-control-del-istmo

Terminé la instalación de Fidel sobre Comercial Control del Istmo y dejé la corrida registrada. Una cosa para corregir: la nota que le puse a esa corrida dice que hay una obligación vencida sin evidencia, y eso es falso. El reporte muestra que el OBL-3 de CTR-3101 venció el 2026-09-30 pero tiene su evidencia entregada. Yo no edité la corrida ya registrada, así que esa nota queda con el error.

**Qué quedó hecho**
- **Carpeta:** usé la que venía en el argumento, `legal/155831003-2-2013-comercial-control-del-istmo`. Tiene 6 contratos, el registro y la matriz de atribuciones, y nada fuera de la estructura recomendada.
- **Configuración:** `.criterio/legal/155831003-2-2013/config.json`, validada sin problemas. Con nadie que respondiera, tomé los datos de los documentos o los valores de `config.example.json`:
  - **Entidad:** Comercial Control del Istmo, RUC 155831003-2-2013, Panamá, USD.
  - **Avisos y certificado:** 60 días para vencimientos, 30 para preavisos y 30 como máximo para el certificado.
  - **Entidad pública:** no. Ningún documento dice que contrate bajo ley de contratación pública.
  - **Feriados:** ninguno. El del ejemplo es de otro país y no lo copié.
- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez, con comprobante en `.criterio/terminos/` en Markdown y PDF.
- **Fichas:** 6 de 6, con 0 `record_issues`, en `estado-legal/155831003-2-2013-comercial-control-del-istmo/contratos/`.
- **Calendario al 2026-10-06:**
  - **CTR-3101:** el reporte de cumplimiento OBL-3 venció el 2026-09-30, hace 6 días, y ya tiene evidencia.
  - **CTR-3105:** termina el 2026-11-20, en 45 días.
  - **CTR-3103:** termina el 2026-12-31, en 86 días.
  - El motor no marcó nada abierto.
- **Registro de la corrida:** `2026-10-06-legal-setup-1`, con la salida guardada en `corridas/salida-legal-setup.md`.

**Lo que conviene que sepas**
- **Fecha de la aceptación:** el comprobante dice 2026-10-30, no 2026-10-06. `aceptar` no recibe `--today` y usó la fecha real del sistema.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt` en los documentos. Nadie autorizó escribir ahí.
- **CTR-3105:** el acta del 2026-09-18 decide renovarlo, pero su cláusula 4 dice que no se prorroga automáticamente. Cómo se formaliza esa renovación es una pregunta para una persona; no la interpreté.