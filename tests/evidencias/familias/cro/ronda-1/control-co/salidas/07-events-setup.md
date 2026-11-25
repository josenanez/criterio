# /criterio-risk-events:events-setup riesgos/901888444-banco-control-de-riesgos-sintetico

Casandra quedó configurada para Banco Control de Riesgos Sintético (NIT 901888444) y su primera revisión de indicadores clave no encontró nada abierto.

Como la sesión era de prueba, tomé cada respuesta sugerida de los documentos y de la configuración que Severo ya había dejado en esta carpeta:

- **Carpeta:** `riesgos/901888444-banco-control-de-riesgos-sintetico`. Era la única candidata y ya tenía la marca `_CRITERIO_RIESGOS.txt`, así que no la volví a marcar.
- **Periodo:** 2026-10, el de `valores_indicadores_2026-10.xlsx`.
- **Plazos de la política de riesgo operacional:** 30 días para registrar un evento desde que se descubre, y 12 meses de ventana para contar dos eventos como repetidos.
- **Publicar en Rostrum:** sí, porque el marco no dice otra cosa.
- **Estado:** `estado-riesgos/901888444-banco-control-de-riesgos-sintetico`.
- **Configuración:** `.criterio/eventos/901888444/config.json`.
- **Términos v1.6:** aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-events-0.1.0-2026-11-25.md` y `.pdf`.

Procesé el acta del comité de riesgos de octubre y llevé a la ficha de 2026-10 una acción: para KRI-01, «El comité aprueba el bloqueo preventivo de los BIN comprometidos» (`40-actas/acta_comite_riesgos_2026-10.pdf`, p. 1). Los límites L-04 y L-03 que trata la misma acta son de Severo y no van en esta ficha.

# Cada indicador contra su umbral · Banco Control de Riesgos Sintético · periodo 2026-10

**Entidad:** Banco Control de Riesgos Sintético (901888444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transacciones fraudulentas por millón | mayor es peor | 40 | 60 | 52 | alerta | sí |
| KRI-02 · Disponibilidad de los canales digitales | menor es peor | 99.5 | 99 | 99.6 | normal | no |
| KRI-03 · Rotación del personal de crédito | mayor es peor | 8 | 12 | 6.5 | normal | no |
| KRI-04 · Días sin una prueba del plan de continuidad | mayor es peor | 180 | 365 | 64 | normal | no |
| KRI-05 · Concentración de los depósitos en los 20 mayores | mayor es peor | 25 | 30 | 29 | alerta | sí |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión de prueba nadie podía darlo. Para correrlo a mano: `/criterio-risk-events:events-wake`.

La corrida quedó registrada como `2026-11-25-events-setup-1`, y lo que se mostró está en `estado-riesgos/901888444-banco-control-de-riesgos-sintetico/corridas/salida-events-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.