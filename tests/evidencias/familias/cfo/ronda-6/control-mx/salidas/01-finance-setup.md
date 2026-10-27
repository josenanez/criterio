# /criterio-finance:finance-setup finanzas/CCM120615R59-comercial-control-centro

## Listo: Comercial Control Centro

**Lo que miré:** 66 archivos, periodos 2026-01 a 2026-09 y el presupuesto 2026. Ninguno está fuera de la estructura.
**Términos:** José Francisco Ñáñez aceptó la versión 0.11.0 (términos 1.2). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-finance-0.11.0-2026-10-06.md` y `.pdf`.

El cierre de septiembre va en curso, con el 53.85 % de avance. Ese avance es igual con evidencia y declarado, así que no hay brecha entre lo que se afirma y lo que está soportado. El motor no encontró señales abiertas, y el checklist no está aprobado.

# Estado del cierre · Comercial Control Centro · periodo 2026-09

**Entidad:** Comercial Control Centro (CCM120615R59) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.11.0 · **Aprueba:** Contralor · **Comando:** `close-status`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Estado declarado:** en curso (`2026-09/40-soportes/correo-estado-del-cierre.md`, 2026-10-05) · **Avance con evidencia:** 53.85 % · **Avance declarado:** 53.85 % (ponderados por criticidad)

El checklist no está aprobado: el estado se calcula, y una persona tiene que aprobarlo antes de darlo por bueno.

| Id | Tarea | Responsable | Vence | Criticidad | Estado | Evidencia |
|---|---|---|---|---|---|---|
| C-08 | Revisar el cierre y sus soportes | Sofía León | 2026-10-08 | alta | bloqueada por otra (C-07) | — |
| C-09 | Aprobar el cierre del periodo | Sofía León | 2026-10-09 | alta | bloqueada por otra (C-08) | — |
| C-06 | Preparar los papeles de trabajo de impuestos | Elena Cruz | 2026-10-07 | alta | en plazo | — |
| C-07 | Cuadrar el balance de comprobación | Lucía Mora | 2026-10-07 | alta | en plazo | — |
| C-01 | Cerrar los módulos de ventas, compras e inventarios | Lucía Mora | 2026-10-01 | alta | cumplida con evidencia | `2026-09/40-soportes/C-01-soporte.md` |
| C-02 | Conciliar cada cuenta bancaria | Andrés Paz | 2026-10-02 | alta | cumplida con evidencia | `2026-09/40-soportes/C-02-soporte.md` |
| C-03 | Cruzar las facturas emitidas con las ventas | Lucía Mora | 2026-10-02 | alta | cumplida con evidencia | `2026-09/40-soportes/C-03-soporte.md` |
| C-04 | Conciliar cartera contra su auxiliar | Marta Ríos | 2026-10-05 | alta | cumplida con evidencia | `2026-09/40-soportes/C-04-soporte.md` |
| C-05 | Registrar provisiones y causaciones | Jorge Vela | 2026-10-05 | media | cumplida con evidencia | `2026-09/40-soportes/C-05-soporte.pdf` |

**Ruta crítica del cierre:** C-07 → C-08 → C-09

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad/)
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 5135, 5145, 5195; IVA generado y descontable 2408 (las que sostienen las facturas del periodo)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (auxiliar en 2026-08 y 2026-09); bancos andino-1901 y pacifico-1902
- ¿Cuál es el país, la moneda y el marco? → México, MXN, NIF (CINIF); propuesto por el RFC y los CFDI de la carpeta, sin confirmar
- ¿El checklist está aprobado y quién aprueba el cierre? → Se usa 00-referencia/checklist-cierre.xlsx, sin aprobar; aprobador 'Contralor' (sugerido, sin confirmar)
- ¿Hay festivos del calendario? → No se dieron; la lista queda vacía
- ¿Dónde se guarda el estado? → estado-finanzas/CCM120615R59-comercial-control-centro

## Fuentes

- Sin documentos citados.

**Qué falta para que esto sea mejor:**
- El checklist necesita que una persona lo apruebe.
- El marco (NIF) y el aprobador («Contralor») son propuestas mías, sin confirmar.
- El correo del cierre solo dice «en curso», sin fecha de término.

**Cuándo vuelvo:** a diario durante la ventana del cierre; una vez por semana fuera de ella.

**Notas de la corrida:**
- Hice 7 preguntas y tomé la respuesta sugerida de los documentos en cada una.
- No medí los minutos hasta el primer resultado.
- No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie dio el sí. Es lo único que un agente escribe ahí.
- No registré requerimientos del auditor en la ficha (`audit_requests` vacío): `pbc-2026-09.xlsx` es la tabla del auditor y `audit_requests` es solo para los que llegan fuera de ella.
- La corrida quedó registrada como `2026-10-06-finance-setup-1`, y lo mostrado está en `estado-finanzas/CCM120615R59-comercial-control-centro/corridas/salida-finance-setup.md`.