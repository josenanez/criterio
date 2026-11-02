# /criterio-finance:finance-setup finanzas/88457812-7-banco-del-tebicuary-sintetico

## Listo: Banco del Tebicuary (sintético)

**Lo que miré:** 65 archivos, periodos 2026-01 a 2026-09 y el presupuesto 2026. Ninguno está fuera de la estructura.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.2.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-finance-1.2.0-2026-10-06.md` y `.pdf`.

El cierre de 2026-09 está declarado **en curso** (correo de Sofía León, 2026-10-05). El avance es de **42,31 % con evidencia** y **53,85 % declarado**, ponderado por criticidad. El motor encontró 9 señales en total. El reporte pone en "lo que hay que atender" solo una:

- **C-02, conciliar cada cuenta bancaria (Andrés Paz):** figura cumplida y no hay soporte `C-02*` en `2026-09/40-soportes/`.
- **Ruta crítica:** C-02 → C-07 → C-08 → C-09. C-07, C-08 y C-09 quedan bloqueadas por C-02.
- **Con soporte:** C-01, C-03, C-04 y C-05.
- **En plazo:** C-06.
- **Checklist:** el de la organización, sin aprobación de una persona. Hasta que alguien lo apruebe, el estado se calcula pero no se da por bueno.

Las otras ocho señales (cuadre del mayor contra el balance, bancos sin conciliar, factura sin registro, diferencia de monto en una factura y una partida antigua) están en `resultados.json`.

**Las respuestas que tomé en lugar de preguntar** (sesión sin interfaz):
- Entidad: RUC 88457812-7, Paraguay, PYG. Marco: normas del Banco Central del Paraguay (F-42).
- Periodo 2026-09. Cuentas de facturas: ventas 4135, compras 5135, 5145 y 5195, IVA 2408.
- Conciliación contra auxiliar: 1305 y 2205. Bancos: andino-13101 y pacifico-13102.
- Aprueba Sofía León. No cargué festivos.

**Qué falta para mejorar esto:** el soporte firmado de C-02, la aprobación del checklist por una persona y los festivos del calendario.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

Los archivos quedaron en estos lugares:
- Configuración: `.criterio/finanzas/88457812-7-banco-del-tebicuary-sintetico/config.json`
- Reporte: `estado-finanzas/88457812-7-banco-del-tebicuary-sintetico/cierre/2026-09/reporte-close-status.md`
- Salida registrada: `estado-finanzas/88457812-7-banco-del-tebicuary-sintetico/corridas/salida-finance-setup.md`

No dejé la marca `_CRITERIO_FINANZAS.txt` en la carpeta de documentos. No había nadie que autorizara escribirla.