# /criterio-legal:legal-setup legal/48712035-banco-del-altiplano-sintetico

Fidel quedó instalado sobre Banco del Altiplano Sintético (NIT 48712035, GT, GTQ), con 6 contratos procesados y la corrida registrada. Las 5 señales no están todas detalladas: el calendario solo muestra 2.

- **Carpeta:** usé la que venía en el argumento. Tiene 6 contratos, el registro y la matriz de atribuciones, y nada fuera de la estructura.
- **Respuestas tomadas de los documentos:** la entidad no es pública, porque ningún documento indica contratación pública. Los umbrales son los de `config.example.json` (60 días para vencimientos, 30 para preavisos, certificado de máximo 30 días). No dejé la marca `_CRITERIO_LEGAL.txt` porque nadie la autorizó.
- **Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.3. El comprobante, en Markdown y PDF, está en `.criterio/terminos/`.
- **Configuración y fichas:**
  - **Configuración:** `.criterio/legal/48712035-banco-del-altiplano-sintetico/config.json`, validada sin problemas.
  - **Fichas:** `estado-legal/48712035-banco-del-altiplano-sintetico/contratos/`, sin `record_issues`. En todas dejé vacíos el monto asegurado y la fecha de entrega de las pólizas, porque las pólizas no los dicen.
- **Señales:** el cálculo dio 5.
  - **Fechas (las que detalla el calendario):**
    - **CTR-3304:** el informe mensual de ejecución venció el 2026-09-05 sin evidencia, y el preaviso de no renovación vence el 2026-11-01 (en 26 días) sin decisión.
  - **Facultad, pago sobre el valor pactado y garantía faltante:** el cálculo marcó una de cada una. No las detallé en esta corrida; salen con `authority-check`, `contract-execution` y `contract-register`.
- **Calendario:** también muestra la terminación de CTR-3305 el 2026-11-20, la de CTR-3303 y CTR-3304 el 2026-12-31, y el reporte del 2026-09-30 de CTR-3301, que sí tiene evidencia.

El motor escribió el calendario, no yo. Está en `estado-legal/48712035-banco-del-altiplano-sintetico/contratos/reporte-obligations-calendar.md`. La salida de esta sesión quedó en `estado-legal/48712035-banco-del-altiplano-sintetico/corridas/salida-legal-setup.md`.

No hice ninguna valoración jurídica, y la decisión de renovar o terminar es de una persona.

Una desviación de proceso: en un paso encadené `mkdir` con `&&` y escribí la configuración con un `cat` en la misma llamada, contra la regla de una acción por llamada. El resultado fue correcto.