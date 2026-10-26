# /criterio-finance:finance-setup finanzas/0990054321001-minera-condor

## Listo: Minera Cóndor

**Lo que miré:** 63 archivos, los periodos 2026-01 a 2026-09 y el presupuesto 2026. Ninguno quedó fuera de la estructura.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-0.10.0-2026-10-06.md` y en el `.pdf` del mismo nombre.

**El cierre de 2026-09:** el correo de Sofía León del 2026-10-05 lo declara «en curso». Con evidencia hay un avance del 34.62 %, contra un 46.15 % declarado. El checklist no está aprobado, así que una persona tiene que aprobarlo antes de darlo por bueno. Clara encontró 7 señales en total, pero el reporte de estado del cierre solo muestra 2:
- **C-02, conciliar cada cuenta bancaria:** figura cumplida y no tiene soporte (responsable: Andrés Paz).
- **C-05, registrar provisiones y causaciones:** venció el 2026-10-05 sin evidencia (responsable: Jorge Vela).
- **Las otras 5:**
  - dos bancos sin conciliar;
  - una factura electrónica sin registro en la contabilidad;
  - un requerimiento del auditor sin respuesta;
  - una partida conciliatoria antigua.
  Esas aparecen en los comandos de bancos, facturas y auditoría, no en este reporte.

**Ruta crítica:** C-02 → C-07 → C-08 → C-09. C-07, C-08 y C-09 quedan bloqueadas mientras C-02 y C-05 sigan abiertas.

**Lo que asumí al no haber nadie a quien preguntar** (las 11 respuestas están en la ficha del cierre):
- Ecuador y USD, por el RUC y por el formato de las facturas.
- Cuentas de ventas 4135, compras 5135, 5145 y 5195, e IVA 2408, las que sostienen facturas del periodo.
- Se concilian contra auxiliar 1305 y 2205, y se esperan los bancos andino-4101 y pacifico-4102.
- Aprueba Sofía León, que es la responsable de la tarea C-09.

**Lo que falta para que esto mejore:**
- **Marco contable:** ningún documento dice el grupo, así que quedó como «marco aplicable en Ecuador (F-06)».
- **Festivos:** no los encontré y quedaron vacíos.
- **Soportes:** faltan el de C-02 y el de C-05.
- **Checklist:** hay que aprobarlo.
- **Marca de la carpeta:** no dejé el archivo `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

Guardé todo en estos archivos:
- `.criterio/finanzas/0990054321001/config.json`
- `estado-finanzas/0990054321001-minera-condor/cierre/2026-09/reporte-close-status.md`
- `estado-finanzas/0990054321001-minera-condor/corridas/salida-finance-setup.md`

La corrida quedó registrada con 7 hallazgos. No medí los minutos hasta el primer resultado porque la sesión fue sin interfaz.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.