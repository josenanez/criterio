# /criterio-legal:contract-register 

Los términos (v1.2) ya estaban vigentes y aceptados, así que seguí sin registrar nada nuevo. Dos contratos no cuadran entre el registro y los documentos.

# Registro de contratos · Cooperativa Sierra Alta · al 2026-10-06

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | El registro reporta vigente un contrato cuya fecha de terminación ya pasó (`contract_expired_active`) | CTR-203: el registro lo reporta vigente y terminó el 2026-08-31 | `10-registro/registro-contratos.csv` fila 4 · `contratos/CTR-203-edificios-del-valle-s-a/10-contrato/contrato.md` |
| 2 | Un contrato de la carpeta no está en el registro (`register_mismatch`) | CTR-207: el contrato está en la carpeta y no en el registro | `contratos/CTR-207-transporte-de-valores-s-a/` |

## El resultado

| Contrato | Contraparte | Estado en el registro | Estado según sus fechas | Diferencias |
|---|---|---|---|---|
| CTR-201 | Sistemas Cooperativos Cía. Ltda. | vigente | vigente | — |
| CTR-202 | Suministros Quito S.A. | vigente | vigente | — |
| CTR-203 | Edificios del Valle S.A. | vigente | terminado | — |
| CTR-204 | Software Andino Cía. Ltda. | vigente | vigente | — |
| CTR-205 | Asesoría Financiera Cía. Ltda. | vigente | vigente | — |
| CTR-206 | Servicios Generales S.A. | terminado | terminado | — |
| CTR-207 | Transporte de Valores S.A. | — | vigente | — |

**Lo que no se pudo procesar:** todo lo que llegó se procesó.
**Preguntas que hizo:** ninguna.

**Fuentes:** `10-registro/registro-contratos.csv`, `contratos/CTR-203-edificios-del-valle-s-a/10-contrato/contrato.md`, `contratos/CTR-207-transporte-de-valores-s-a/`

La salida completa quedó en `estado-legal/1790012345001-cooperativa-sierra-alta/corridas/salida-contract-register.md`. La corrida quedó registrada con el id `2026-10-06-contract-register-1`.