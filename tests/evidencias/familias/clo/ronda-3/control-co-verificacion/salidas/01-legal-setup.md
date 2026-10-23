# /criterio-legal:legal-setup legal/900000001-distribuidora-control

Fidel quedó instalado sobre Distribuidora Control (NIT 900000001, Colombia). Las fichas de los 6 contratos están hechas y el calendario sale con fecha de corte 2026-10-06.

**Instalación**
- **Carpeta de documentos:** usé `legal/900000001-distribuidora-control`, la que indicaste. Tiene los 6 contratos (CTR-501 a CTR-506), el registro y la matriz de atribuciones, y nada fuera de la estructura.
- **Configuración:** `.criterio/legal/900000001/config.json`, validada sin problemas. Usé los valores sugeridos: aviso de vencimiento a 60 días, preaviso a 30 y certificado de la contraparte de hasta 30 días. El estado queda en `estado-legal/900000001-distribuidora-control`, fuera de los documentos.
- **Términos:** versión 1.2, aceptados a nombre de José Francisco Ñáñez el 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-0.8.0-2026-10-06.md`, con su PDF.
- **Marca `_CRITERIO_LEGAL.txt`:** no la dejé. Es lo único que se escribe dentro de los documentos y nadie la autorizó en esta sesión.

**Fichas y calendario**
- **Fichas:** convertí 29 documentos, ninguno ilegible, y escribí las 6 fichas en `estado-legal/900000001-distribuidora-control/contratos/`. `compute` no marcó problemas en ninguna.
- **Calendario:** el reporte no marca nada abierto. Muestra tres hechos:
  - CTR-501: el reporte de operaciones al oficial de cumplimiento (OBL-3) vencía el 2026-09-30 y tiene evidencia en la carpeta.
  - CTR-505: termina el 2026-11-20, en 45 días.
  - CTR-503: termina el 2026-12-31, en 86 días.
- **Reporte:** quedó en `estado-legal/900000001-distribuidora-control/contratos/reporte-obligations-calendar.md`. La decisión de renovar o terminar es de una persona.

**Pendiente**
- **Registro y valor de CTR-502:** el registro dice 150.000.000 y el contrato 120.000.000, más 30.000.000 del otrosí OT-1; este comando no los cruza. Eso lo revisa `/contract-register`.
- **Firmas y pagos:** las facultades de firma (`/authority-check`) y los pagos contra lo pactado (`/contract-execution`) tampoco los cubre este comando, así que no sé qué hay en esos dos frentes.

**Corrida:** la dejé registrada como `2026-10-06-legal-setup-1`, con 0 preguntas a la persona. Lo que te mostré está en `estado-legal/900000001-distribuidora-control/corridas/salida-legal-setup.md`.