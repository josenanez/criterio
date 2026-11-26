# /criterio-risk-appetite:appetite-setup riesgos/901888444-banco-control-de-riesgos-sintetico

Severo quedó instalado para Banco Control de Riesgos Sintético (NIT 901888444) y el primer reporte, del periodo 2026-10, no tiene nada abierto.

- **Configuración:** `.criterio/apetito/901888444/config.json`. Los plazos salen de la declaración de apetito y de la política de riesgo operacional: 10 días para reportar la exposición, revisión de la junta cada 12 meses, 30 días para registrar un evento y 12 meses para contar eventos repetidos. Rostrum queda activado y el estado se guarda en `estado-riesgos/901888444-banco-control-de-riesgos-sintetico`.
- **Términos v1.6:** José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.2.0-2026-11-25.md` y en `.pdf`.
- **Marca:** dejé `_CRITERIO_RIESGOS.txt` en la carpeta de la entidad.
- **Ficha 2026-10:** según la declaración, la junta la revisó por última vez el 2026-02-26. En el acta de su sesión del 2026-11-12, el comité de riesgos aprobó los excesos de L-04, L-06 y L-07. Sobre L-03 solo tomó nota del plan de acción, así que no lo registré como aprobación. Cité el acta como p. 1 porque el texto procesado no marca saltos de página.

---

# Cada exposición contra su límite · Banco Control de Riesgos Sintético · periodo 2026-10

**Entidad:** Banco Control de Riesgos Sintético (901888444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `limit-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Cartera vencida de consumo | máximo 6 % | 5.8 | no | — | Crédito | 2026-11-06 |
| L-02 | Indicador de cobertura de liquidez | mínimo 120 % | 131 | no | — | Tesorería | 2026-11-10 |
| L-03 | Concentración en el mayor deudor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Pérdidas por fraude externo sobre ingresos | máximo 0.5 % | 0.62 | sí | aprobado | Operaciones | 2026-11-07 |
| L-05 | Exposición a contrapartes sin calificación | máximo 15 % | 12 | no | — | Tesorería | 2026-11-09 |
| L-06 | Pérdidas operacionales sobre el patrimonio | máximo 1 % | 1.1 | sí | aprobado | Operaciones | 2026-11-08 |
| L-07 | Exposición al mayor banco corresponsal | máximo 20 % | 23 | sí | aprobado | Tesorería | 2026-11-09 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-10 (families/criterio-cro/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión no había quien lo diera, así que no la creé. Mientras tanto se corre a mano con `/criterio-risk-appetite:appetite-wake`.

La corrida quedó registrada como `2026-11-25-appetite-setup-1`. Lo que se mostró está en `estado-riesgos/901888444-banco-control-de-riesgos-sintetico/corridas/salida-appetite-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.