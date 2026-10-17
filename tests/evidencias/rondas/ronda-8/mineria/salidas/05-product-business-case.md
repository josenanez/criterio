# /criterio-product:product-business-case 

Armé el caso de negocio de Trazabilidad (PRD-304). Solo una de sus dos cifras tiene fuente, y el costo de construir no está en ningún documento. Por eso, por ahora es una propuesta y no un caso que se pueda evaluar.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17). No hizo falta registrarlos otra vez. Las demás preguntas las dejé en la respuesta sugerida.

- **Cifras:** `volumen_mensual` = 240.425 está declarada. Sale del caso de negocio del 2025-09-15, que es su única fuente, y no dice qué mide ni cómo se calculó. No hay ninguna cifra medida, así que no se pudo contrastar contra una serie.
- **Retorno:** el texto solo dice «Retorno esperado en 24 meses». No tiene valor y pasó a la lista de vacíos.
- **Supuesto de adopción:** el anexo del 2026-09-26 dice «se confirmó», pero cita una medición del piloto que no está en la carpeta. Lo dejé como verificación no sustentada.
- **Costos:** el costo de construir y el de operar no tienen fuente. Es el primer vacío.
- **Qué se construye:** entran los 11 requerimientos aceptados. Los 5 propuestos quedan fuera.
  - Nueve de los 11 aceptados se apoyan en una misma frase genérica de un cliente sin nombre. REQ-4401 y REQ-4414 no tienen evidencia de demanda.
  - REQ-4400 y REQ-4414 no tienen doliente, y ninguno de los aceptados tiene proyecto que lo ejecute.
- **Otros vacíos:** la definición no trae criterio de éxito ni fecha de corte. Tampoco hay qué pasa si no se hace ni alternativas consideradas.
- **Cruce con otros productos:** no hay fichas publicadas para cruzar. Revisé las carpetas de otros productos y ninguna cita 240.425. El cruce con `/product-overlap` queda pendiente.

No proyecté ni calculé ninguna cifra, y no recomiendo aprobar ni rechazar. Ofrezco pasar los tres supuestos al seguimiento con assumption-tracking. Si el caso se aprueba, el paso siguiente es `/product-charter`.

La corrida quedó registrada como `2026-10-17-product-business-case-1`, con 39 segundos medidos. La salida completa está en `estado-producto/PRD-304/corridas/salida-product-business-case.md`.