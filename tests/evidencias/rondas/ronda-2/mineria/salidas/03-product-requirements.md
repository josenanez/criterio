# /criterio-product:product-requirements 

Corrí `/product-requirements` sobre PRD-300 (Monitoreo de flota) y el registro tiene los cuatro requerimientos aceptados, con vacíos en todos. Registré la corrida con 14 hallazgos en 28 segundos. No pude confirmar las trazas contra fichas de proyecto, porque en este espacio no existe la carpeta de fichas. Aun así, ningún requerimiento declara proyecto.

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-15), así que no los registré de nuevo.

**Registro al 2026-10-15:** 4 requerimientos, todos aceptados. El 75 % tiene evidencia y el 0 % tiene proyecto que lo ejecute.

- **Aceptado sin evidencia:** REQ-2017 (Natalia Ospina) no tiene ninguna cita de quien lo pidió. Va primero porque es lo más grave.
- **Aceptados sin proyecto:** los cuatro. Conviene correr `/product-trace`.
- **Aceptados sin documento de decisión:** el acta del 2026-10-11 dice «Se mantiene el plan», pero no consta quién decidió ni cuándo. La configuración no define quién tiene la facultad de decidir, porque trae `authority: null`.
- **Evidencia de hace 12 meses:** REQ-1000, REQ-1001 y REQ-1002 se sostienen en la misma cita genérica de la entrevista del 2025-09-28. Esa entrevista no nombra ninguno de los tres.
- **Dolientes:** los cuatro tienen una persona, no un área. No hay requerimientos propuestos, así que nada lleva meses sin decidirse.
- **Criterio de aceptación:** los cuatro dicen «se verifica en producción», que no es medible. Es una lectura mía, no una señal calculada.
- **Caso de negocio:** declara 164.808 de volumen mensual y el tablero mide 102.629, un 37,7 % menos (el umbral es 20 %).
- **Supuesto sin verificar:** «El ahorro se sostiene sin inversión adicional» lleva 131 días sin verificarse.

No ofrezco `/product-charter`: ningún requerimiento tiene a la vez evidencia vigente, criterio medible y decisión documentada.

Todo está en `estado-producto/PRD-300/corridas/`:
- `salida-product-requirements.md`
- `2026-10-15-product-requirements-1.md`