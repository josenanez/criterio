# /criterio-remediation:remediation-wake 

Hoy solo tocaba `remediation-scan`, la revisión semanal, y se hizo. No había peticiones abiertas en Rostrum y no tocaba ningún otro reporte. Los términos ya estaban aceptados a nombre de José Francisco Ñáñez con fecha 2026-11-24, así que no hubo que registrarlos de nuevo.

En la revisión no apareció ningún documento nuevo, cambiado ni borrado. La ficha ya tenía las evidencias de H-20 y H-21, la explicación del atraso de H-03 y el hallazgo externo RF-01.

# Qué cambió en el seguimiento · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (20602888432) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.2.2 · **Comando:** `remediation-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Hallazgos en el registro:** 6 · **Abiertos:** 4 · **Evidencias en la ficha:** 2.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

**Corridas registradas:** `2026-11-24-remediation-scan-2` y `2026-11-24-remediation-wake-1`.

**Un fallo mío que se corrigió:** cambié la terminal a la carpeta de estado, y en la siguiente consulta los términos salieron como no vigentes. El motor busca los comprobantes con una ruta relativa a la carpeta desde donde se llama. Los comprobantes estaban en `.criterio/terminos/`. Al volver a la carpeta de trabajo, los términos salieron vigentes y el motor siguió marcando solo `remediation-scan`.