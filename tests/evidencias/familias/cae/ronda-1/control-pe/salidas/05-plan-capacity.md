# /criterio-audit-plan:plan-capacity 

Los términos (v1.6) están vigentes, así que corrí el reporte con `--today 2026-11-24`. No tuve que registrar ninguna aceptación nueva.

# Las horas del plan · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (20602888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.1.0 · **Comando:** `plan-capacity`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Horas del plan:** 2000 · **Horas disponibles del equipo:** 2000.

| Trabajo | Temas | Horas |
|---|---|---|
| TR-01 · Crédito comercial | credito | 500.0 |
| TR-02 · Ciberseguridad de canales | ciberseguridad, ti | 400.0 |
| TR-03 · Prevención de lavado | cumplimiento, sarlaft | 300.0 |
| TR-04 · Pagos a proveedores | fraude, proveedores, terceros | 300.0 |
| TR-06 · Nómina | nomina | 200.0 |
| TR-07 · Gobierno corporativo | gobierno | 300.0 |

Requisitos temáticos de The IIA y desde cuándo rigen: Ciberseguridad, 2026-02-05; Terceros, 2026-09-15; Comportamiento Organizacional, 2026-12-15; Resiliencia Organizacional, 2027-04-30; Anticorrupción, 2027-11-23.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

La corrida quedó registrada con el id `2026-11-24-plan-capacity-1` y 0 hallazgos. Lo que te mostré está guardado en `estado-auditoria/20602888432-cooperativa-control-sintetica/corridas/salida-plan-capacity.md`.

Dos cosas sobre cómo lo hice:
- Guardé en `salida-plan-capacity.md` la salida del motor con una segunda llamada a `reporte`, no la copia del texto que te muestro. Es el mismo reporte.
- Primero creé por error la carpeta `corridas` dentro de `.criterio/plan/…` y la borré. La carpeta correcta es la que está dentro de `estado-auditoria/…`.