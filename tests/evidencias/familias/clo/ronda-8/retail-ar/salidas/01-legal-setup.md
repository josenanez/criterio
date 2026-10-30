# /criterio-legal:legal-setup legal/30714520780-almacenes-del-plata

Terminé la instalación de Fidel para Almacenes del Plata (CUIT 30714520780). Procesé 6 contratos y el cálculo encontró 5 señales.

**Qué hice**
- **Carpeta e inventario:** usé `legal/30714520780-almacenes-del-plata`. Tiene los 6 contratos, el registro y la matriz de atribuciones, y nada fuera de lugar.
- **Configuración:** quedó en `.criterio/legal/30714520780/config.json` y el motor la validó sin problemas. Los datos salen de los contratos: Argentina, ARS, entidad no pública. Los umbrales son los de `config.example.json`: 60 días para vencimientos, 30 para preavisos y 30 de antigüedad máxima del certificado.
- **Términos:** versión 1.3, aceptados a nombre de José Francisco Ñáñez el 2026-10-06. Los comprobantes están en `.criterio/terminos/`.
- **Fichas:** escribí las 6 en `estado-legal/30714520780-almacenes-del-plata/contratos/`. El motor no reportó `record_issues`.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt`. En la prueba nadie autorizó escribir dentro de los documentos.
- **Preguntas a la persona:** ninguna. Tomé las respuestas de los documentos y las dejé dichas en la salida registrada.

**Lo que hay que atender**
- **CTR-2603** (arrendamiento de la sede principal, 42.000.000 ARS) vence el 2026-11-25, en 50 días, y no tiene decisión registrada de renovar o terminar.
- **CTR-2601:** el reporte al oficial de cumplimiento (cláusula 7) estaba fijado para el 2026-09-30. Hay evidencia entregada ese mismo día.
- **CTR-2605:** termina el 2026-11-20 y el acta del comité del 2026-09-18 decidió renovarlo.

Las otras cuatro señales son:
- una firma sin facultad;
- un pago posterior a la terminación;
- una garantía que vence antes de lo exigido;
- una diferencia con el registro.

Este comando solo muestra el calendario, así que no sé a qué contrato corresponde cada una. El detalle lo dan `authority-check`, `contract-execution` y `contract-register`.

**Salida registrada**
- El texto completo, con el calendario que generó el motor, está en `estado-legal/30714520780-almacenes-del-plata/corridas/salida-legal-setup.md`.
- La corrida quedó registrada como `2026-10-06-legal-setup-1`, con 5 hallazgos.