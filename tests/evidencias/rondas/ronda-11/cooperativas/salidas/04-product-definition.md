# /criterio-product:product-definition 

## Definición — Recaudos (PRD-306) · contrastada al 2026-10-23

Los términos (v1.2) ya estaban aceptados por José Francisco Ñáñez el 2026-10-23, así que no volví a registrarlos. La corrida está registrada como `2026-10-23-product-definition-1`. El informe completo está en `estado-producto/PRD-306/corridas/salida-product-definition.md`.

Analicé 6 afirmaciones del documento del 2026-05-20, el caso de negocio y el anexo de verificación.

- **Contradicciones:** ninguna. Ninguna fuente dice lo contrario de la definición.
- **Cifras que nadie mide:** el `volumen_mensual` de 214.523 no tiene ninguna serie medida. Es el caso más común, no una contradicción. El «retorno esperado en 24 meses» ni siquiera trae una cifra.
- **Lo que no está dicho en ninguna parte:**
  - El criterio de éxito.
  - Qué es la «Propuesta principal»: solo hay ese rótulo.
  - El tamaño del segmento.
  - De dónde sale el 214.523: el caso de negocio se cita a sí mismo.
  - Qué proyecto lo construye.
  - Qué significa «el tiempo pactado» del proveedor.
  - Quién decide: el acta solo registra a Camilo Beltrán, que además escribió todos los documentos.
- **Supuesto:** «El proveedor cumple el tiempo pactado» figura verificado, así que no suma días sin verificar. Pero el anexo se declara a sí mismo la evidencia, y el documento técnico del proveedor del 2026-10-01 no está en la carpeta. Además, el supuesto aparece declarado el 2026-09-29 dentro de una definición fechada el 2026-05-20, o sea que se editó después.
- **Evidencia:** la única es una entrevista del 2025-09-23 a un cliente sin nombre («Lo necesito y hoy no lo tengo»). Es débil: no nombra recaudos, y tiene 13 meses frente a un umbral de 12. De ella dependen el problema y 12 requerimientos.
- **Normativo:** estado «no tengo la norma a la vista». Recaudos mueve dinero y datos personales de terceros, pero la definición no declara el país, así que no puedo nombrar ninguna norma. Esto no equivale a cumplimiento.
- **Para cerrar la definición:** falta el criterio de éxito, así que el producto no se puede cerrar.
- **Fuera de esta definición:** quedan 5 requerimientos aceptados sin criterio de aceptación, 2 propuestos sin decidir hace 142 y 208 días, y 14 aceptados sin proyecto que los ejecute. Eso corresponde a `/product-requirements` y `/product-trace`.

La corrida registró 37 hallazgos en 33 segundos.