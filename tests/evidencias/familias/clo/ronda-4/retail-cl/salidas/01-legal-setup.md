# /criterio-legal:legal-setup legal/76083001-1-tiendas-pacifico

Fidel quedó instalado sobre Tiendas Pacífico (RUT 76083001-1) y procesó los 6 contratos sin problemas en las fichas.

**Vence pronto**
- CTR-1003 (arriendo de la sede, Centro Comercial Costanera) termina el 2026-11-25, en 50 días, y no tiene decisión de renovar o terminar. Esa decisión es de una persona.
- CTR-1005 termina el 2026-11-20, en 45 días, pero ya tiene un acta del comité del 2026-09-18 que decide renovarlo.
- CTR-1001: el reporte de operaciones al oficial de cumplimiento vencía el 2026-09-30 y tiene evidencia entregada el mismo día.

**Otras señales (5 en total)**
El motor encontró 5 señales y el calendario solo muestra una. Las otras cuatro no las revisé: son firma sin facultad, pago posterior a la terminación, garantía que vence antes de lo exigido y diferencia con el registro. Las detalla cada comando: `/authority-check`, `/contract-execution` y `/contract-register`.

**Cómo quedó**
- **Configuración:** `.criterio/legal/76083001-1-tiendas-pacifico/config.json`, con país CL y moneda CLP. Sin interfaz, tomé los avisos de 60 y 30 días y el certificado de 30 días de `config.example.json`.
- **Festivos:** dejé solo 2026-10-12, el del ejemplo. No cargué el calendario de Chile.
- **Términos 1.2:** José Francisco Ñáñez los aceptó el 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-0.10.0-2026-10-06.md` y `.pdf`.
- **Marca de la carpeta:** dejé `_CRITERIO_LEGAL.txt` en `legal/76083001-1-tiendas-pacifico`, que es lo único que escribí dentro de los documentos.
- **Estado y corrida:** `estado-legal/76083001-1-tiendas-pacifico`. La salida está en `corridas/salida-legal-setup.md` y la corrida quedó registrada como `2026-10-06-legal-setup-1`.

Todas las fechas son del 2026-10-06, como pediste para la prueba.