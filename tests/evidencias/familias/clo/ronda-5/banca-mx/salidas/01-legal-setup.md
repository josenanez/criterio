# /criterio-legal:legal-setup legal/BVA150301K21-banco-valle-de-anahuac

Fidel quedó instalado sobre Banco Valle de Anáhuac (BVA150301K21). Procesó los 6 contratos y el motor no devolvió `record_issues`.

- **Inventario:** hay 6 contratos, el registro, los pagos y la matriz de atribuciones, con 3 firmantes. No hay nada fuera de la estructura.
- **Marca de la raíz:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie podía autorizarlo en esta prueba. No toqué nada dentro de los documentos.
- **Configuración:** `.criterio/legal/BVA150301K21/config.json`, validada sin problemas. Tomé de `config.example.json` los avisos de 60 días para vencimientos y 30 para preavisos, y 30 días como antigüedad máxima del certificado. El estado quedó en `estado-legal/BVA150301K21-banco-valle-de-anahuac`.
- **Términos 1.2:** quedaron aceptados a nombre de José Francisco Ñáñez el 2026-10-06. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Señales (5):**
  - Firma sin facultad.
  - Pagos sobre el valor pactado.
  - Una garantía que vence antes de lo exigido.
  - CTR-1303 vence el 2026-11-25, en 50 días, sin decisión de renovar o terminar.
  - CTR-1304 OBL-1, el informe mensual, venció el 2026-09-05 sin evidencia.
- **Detalle pendiente:** el calendario solo muestra las dos últimas. El detalle de las demás sale con `/authority-check`, `/contract-execution` y `/contract-register`, que no corrí en esta sesión.
- **Calendario:** el motor lo escribió en `estado-legal/BVA150301K21-banco-valle-de-anahuac/contratos/reporte-obligations-calendar.md`.
- **Corrida:** quedó registrada como `2026-10-06-legal-setup-1`, con la salida completa en `estado-legal/BVA150301K21-banco-valle-de-anahuac/corridas/salida-legal-setup.md`.

Las fichas las armé con un script que dejé en el directorio temporal de la sesión, no en el proyecto. La decisión de renovar CTR-1305 salió del acta del comité del 2026-09-18.