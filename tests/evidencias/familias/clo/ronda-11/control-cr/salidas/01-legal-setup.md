# /criterio-legal:legal-setup legal/3101733015-comercial-control-de-costa-rica

Fidel quedó instalado sobre Comercial Control de Costa Rica, y el calendario de vencimientos ya está armado. Antes de confiar en que nada vence mal, hay un hueco: `compute` devolvió 0 señales, y por eso el reporte dice «Nada abierto». Esa corrida no revisó firmas ni pagos, porque `legal-setup` no las revisa. Las facultades quedan para `authority-check` y los pagos para `contract-execution`.

- **Configuración:** cédula jurídica 3101733015, CR, CRC, entidad privada. Va en `.criterio/legal/3101733015/config.json`, con los umbrales del ejemplo (60 días para vencimientos, 30 para preavisos y 30 de antigüedad máxima del certificado). No hice preguntas porque nadie contestaba.
- **Marca de la raíz:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie la autorizó.
- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez el 2026-10-06. Los comprobantes están en `.criterio/terminos/`.
- **Fichas:** convertí 6 contratos y escribí 6 fichas en `estado-legal/3101733015-comercial-control-de-costa-rica/contratos/`. No hubo `record_issues`.
- **Calendario al 2026-10-06:**
  - El reporte de operaciones de CTR-3801 (OBL-3) venció el 2026-09-30 y tiene su evidencia.
  - CTR-3805 termina el 2026-11-20, en 45 días. El acta del comité del 2026-09-18 dice «renovar»; la ficha lo registra tal cual, sin evaluarlo.
  - CTR-3803 termina el 2026-12-31, en 86 días.
- **Corrida:** quedó registrada como `2026-10-06-legal-setup-1`, con la salida en `corridas/salida-legal-setup.md`.

Dos decisiones mías, por si quieres cambiarlas:
- **CTR-3802:** la ficha toma como terminación vigente el 2027-12-31 del otrosí OT-1, que está firmado.
- **Pólizas:** dejé en `null` el monto asegurado y la fecha de entrega, porque las pólizas no los traen.

No verifiqué las cifras del registro de contratos ni de la matriz de atribuciones contra las fichas.