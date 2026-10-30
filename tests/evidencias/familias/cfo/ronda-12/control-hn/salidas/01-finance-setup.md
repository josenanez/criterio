# /criterio-finance:finance-setup finanzas/08010007330150-comercial-control-de-honduras

Terminé la instalación de Clara para Comercial Control de Honduras y la corrida quedó registrada con 0 hallazgos.

## Listo — Comercial Control de Honduras

**Lo que miré:** 66 archivos · periodos 2026-01 a 2026-09 y presupuesto-2026 · 0 fuera de la estructura recomendada, 0 ilegibles.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.1.0 (términos 1.3). El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-1.1.0-2026-10-06.md` y `.pdf`.

**Estado del cierre de 2026-09:** declarado «en curso» (correo de Sofía León, 2026-10-05).
- **Avance:** 53.85 % con evidencia y 53.85 % declarado, ponderados por criticidad.
- **Tareas cumplidas con soporte:** C-01 a C-05.
- **Tareas en plazo:** C-06 y C-07.
- **Tareas bloqueadas:** C-08 y C-09.
- **Ruta crítica:** C-07 → C-08 → C-09.
- **Señales abiertas:** ninguna en lo que procesa `close-status`.

**Respuestas que tomé de los documentos, sin que nadie contestara:**
- **Periodo y entidad:** 2026-09; RTN 08010007330150, Honduras, HNL.
- **Cuentas que cruzan las facturas** (las que salen de las 17 facturas): ventas 4135; compras 5135, 5145 y 5195; ISV 2408.
- **Cuentas a conciliar:** 1305 y 2205, que tienen auxiliar en agosto y septiembre.
- **Bancos esperados:** andino-12701 y pacifico-12702.
- **Aprobador del cierre:** Sofía León.
- **Festivos:** ninguno, porque no me dieron.
- **Archivo `_CRITERIO_FINANZAS.txt`:** no lo dejé en la carpeta, porque la prueba no autorizó escribir en los documentos.

**Qué falta para que esto sea mejor:**
- Una persona debe aprobar el checklist. Ningún documento dice que esté aprobado, así que lo dejé sin aprobar.
- Hay que confirmar si el marco son las NIIF completas o las NIIF para las PYMES. La configuración dice «NIIF» y deja esa duda anotada.
- Faltan por correr `einvoice-check`, `bank-reconcile`, `account-reconcile` y `ledger-check`, que son los comandos que abren señales. Este reporte solo compara lo declarado con el checklist, así que «nada abierto» no significa que todo cuadre.

**Dónde quedó cada cosa:**
- **Configuración:** `.criterio/finanzas/08010007330150-comercial-control-de-honduras/config.json`.
- **Ficha del cierre:** `estado-finanzas/08010007330150-comercial-control-de-honduras/cierre/2026-09/ficha.json`, con las 17 facturas extraídas y la declaración del correo.
- **Reporte del motor:** `reporte-close-status.md`, en la misma carpeta de la ficha.
- **Salida de esta corrida:** `estado-finanzas/08010007330150-comercial-control-de-honduras/corridas/salida-finance-setup.md`.

No medí los minutos hasta el primer resultado, y eso quedó anotado en la corrida.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.