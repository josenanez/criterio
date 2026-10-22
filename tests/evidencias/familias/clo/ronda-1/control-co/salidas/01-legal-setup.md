# /criterio-legal:legal-setup legal/900000001-distribuidora-control

Fidel quedó instalado sobre Distribuidora Control (NIT 900000001, Colombia). Procesé los 6 contratos y no salió ninguna señal. Con fecha 2026-10-06, el calendario no tiene nada abierto.

- **Inventario:** 6 contratos, y están el registro y la matriz de atribuciones (3 firmantes). No hay nada fuera de la estructura.
- **Respuestas sugeridas, sin interfaz:** avisos de 60 días para vencimientos y 30 para preavisos, y certificado de la contraparte con 30 días de antigüedad máxima. Todo quedó en una línea en la salida de la corrida.
- **Términos:** José Francisco Ñáñez los aceptó (versión 1.2, 2026-10-06). El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-0.7.0-2026-10-06.md` y `.pdf`.
- **Marca `_CRITERIO_LEGAL.txt`:** no la dejé. Es lo único que se escribe dentro de tus documentos y nadie la autorizó en esta prueba. Si quieres la marca, dímelo y la dejo.
- **Fichas:** 6 contratos convertidos (29 documentos), 6 fichas escritas y sin `record_issues`.

Esto muestra el calendario, de 30 días atrás a 90 adelante:

| Fecha | Contrato | Qué | Días |
|---|---|---|---|
| 2026-09-30 | CTR-501 | Reporte de operaciones al oficial de cumplimiento (con evidencia) | -6 |
| 2026-11-20 | CTR-505 | Terminación | 45 |
| 2026-12-31 | CTR-503 | Terminación | 86 |

Todavía no revisé los pagos contra lo pactado. Eso lo hace `contract-execution`, que tiene su propio comando.

Decidí una cosa al armar las fichas: solo CTR-506 lleva la obligación OBL-2 (informe final y acta de liquidación), porque es el único con ese documento. En los otros cinco la cláusula 6 no trae fecha propia, y no quise deducirla.

La configuración quedó en `.criterio/legal/900000001/config.json`. El reporte está en `estado-legal/900000001-distribuidora-control/contratos/reporte-obligations-calendar.md`. La corrida quedó registrada como `2026-10-06-legal-setup-1`, con la salida en `estado-legal/900000001-distribuidora-control/corridas/salida-legal-setup.md`.