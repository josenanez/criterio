# /criterio-finance:close-scan 

El barrido de septiembre de Banco Andino terminó con 8 señales, ninguna nueva respecto de la corrida de `finance-setup`, y la corrida quedó registrada (`2026-10-06-close-scan-1`).

- **Archivos:** 63 nuevos, 0 cambiados, 0 borrados, 0 fuera de lugar. Es la primera vez que close-scan corre en este espacio.
- **Documentos escritos:** convertí 9, que son el correo del cierre, 4 soportes PDF, el PBC y 3 respuestas Word. No extraje nada más a la ficha. Ya traía el estado declarado «en curso», y los requerimientos del auditor vienen en la tabla del PBC, que procesa el motor.
- **Señales (8):** el reporte las lista con su cita.
  - **Cuadre:** la cuenta 5305 no cuadra entre el mayor y el balance, y el balance tiene una diferencia de 5.000,00 entre débitos y créditos.
  - **Checklist:** C-02, «Conciliar cada cuenta bancaria», figura cumplida y no tiene soporte.
  - **Banco andino-1101:** hay un cheque pendiente de 72 días (CH-0450) y una nota débito sin registrar.
  - **Facturación:** la factura SETP99000104 tiene una diferencia de IVA de 1.000,00 entre el XML y los libros.
- **Vacío en el reporte:** el apartado «El resultado» salió vacío del motor y lo dejé tal cual. No agregué cifras.
- **Respuestas tomadas:** las preguntas que hizo el reporte tienen las respuestas sugeridas de `finance-setup`. El marco contable (grupo 1) sigue por confirmar.

Todo está en `estado-finanzas/900123456-banco-andino/`:
- `cierre/2026-09/reporte-close-scan.md`
- `corridas/salida-close-scan.md`