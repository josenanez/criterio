# /criterio-finance:finance-setup finanzas/BVA150301K21-banco-valle-de-anahuac

Terminé la instalación y dejé la corrida registrada. Lo único que me falta es darte el resultado.

## Listo — Banco Valle de Anáhuac

**Lo que miré:** 65 archivos, periodos 2026-01 a 2026-09 y `presupuesto-2026`, 0 fuera de la estructura.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.11.0 (términos 1.2). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-0.11.0-2026-10-06.md` y `.pdf`.

**Estado del cierre de 2026-09:**
- **Estado declarado:** «en curso», según el correo de Sofía León del 2026-10-05.
- **Avance:** 42.31 % con evidencia frente a 53.85 % declarado.
- **Ruta crítica:** C-02 → C-07 → C-08 → C-09.
- **Lo que hay que atender:** C-02, «Conciliar cada cuenta bancaria» (Andrés Paz), figura como cumplida y no hay soporte `C-02*` en `2026-09/40-soportes/`. Por eso quedan bloqueadas C-07, C-08 y C-09.
- **Otras señales:** el motor encontró 9 en total, las otras 8 son:
  - 2 de libro mayor contra balance
  - 1 de balance descuadrado
  - 1 de factura sin registrar
  - 2 de bancos sin conciliar
  - 1 de factura con monto distinto
  - 1 de partida antigua

  El reporte de close-status solo detalla la de C-02. Las demás se abren con `/ledger-check`, `/einvoice-check` y `/bank-reconcile`.

**Lo que decidí yo por defecto, sin que nadie lo confirmara:**
- **Marco contable:** NIF (CINIF). Ningún documento lo dice, hay que confirmarlo.
- **Cuentas de facturas:** ventas 4135; compras 5135, 5145 y 5195; IVA 2408. Salen de las facturas del periodo.
- **Conciliación:** cuentas 1305 y 2205, con los bancos andino-1301 y pacifico-1302.
- **Checklist:** el de la organización, marcado como no aprobado porque nadie confirmó su aprobación.
- **Festivos:** ninguno, no los encontré.
- **Marca `_CRITERIO_FINANZAS.txt`:** no la dejé en la carpeta de documentos, porque la prueba no lo autorizaba.

**Qué falta para mejorar esto:**
- El soporte firmado de C-02.
- Confirmar el marco contable.
- Que una persona apruebe el checklist.
- Los festivos del calendario.

No le hice preguntas a nadie porque la sesión no tiene interfaz: usé 11 respuestas por defecto. No medí los minutos hasta el primer resultado.

**Cuándo vuelvo:** a diario durante la ventana del cierre y una vez por semana fuera de ella.

**Dónde quedó todo:**
- Configuración: `.criterio/finanzas/BVA150301K21/config.json`.
- Reporte: `estado-finanzas/BVA150301K21-banco-valle-de-anahuac/cierre/2026-09/reporte-close-status.md`.
- Salida de esta corrida: `estado-finanzas/BVA150301K21-banco-valle-de-anahuac/corridas/salida-finance-setup.md`, registrada como `2026-10-06-finance-setup-1`.