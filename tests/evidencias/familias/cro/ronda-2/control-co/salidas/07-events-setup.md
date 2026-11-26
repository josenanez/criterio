# /criterio-risk-events:events-setup riesgos/901888444-banco-control-de-riesgos-sintetico

Casandra quedó lista para el Banco Control de Riesgos Sintético (NIT 901888444). En el periodo 2026-10, ningún indicador clave está en alerta sin una acción registrada.

**Respuestas que tomé.** Nadie respondía en esta prueba, así que tomé cada respuesta de los documentos:
- **Entidad, país y moneda:** salen de la configuración que ya había dejado Severo, el agente de apetito por riesgo: Colombia y pesos colombianos.
- **Periodo:** 2026-10, el de `valores_indicadores_2026-10.xlsx`.
- **Plazos:** 30 días para registrar un evento y una ventana de 12 meses para los repetidos. Los dos están en `00-marco/politica_de_riesgo_operacional.pdf`.
- **Rostrum:** se publica, porque el marco no dice otra cosa.
- **Dónde guardo lo que encuentro:** en `estado-riesgos/901888444-banco-control-de-riesgos-sintetico`.
- **Marca:** la carpeta ya tenía `_CRITERIO_RIESGOS.txt`, así que no la volví a poner.

**Términos.** Mostré la versión 1.6 y quedó registrado que los acepta José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-events-0.2.0-2026-11-25.md` y su `.pdf`.

**Configuración.** Quedó en `.criterio/eventos/901888444/config.json`.

**Ficha del periodo.** En el acta del comité de octubre encontré dos acciones sobre indicadores y las llevé a la ficha, citando la página 1:
- KRI-01: el comité aprueba el bloqueo preventivo de los BIN comprometidos.
- KRI-06: el comité aprueba la conciliación diaria automática de las cuentas puente.

Este es el reporte, tal como lo escribió el motor:

---

# Cada indicador contra su umbral · Banco Control de Riesgos Sintético · periodo 2026-10

**Entidad:** Banco Control de Riesgos Sintético (901888444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `kri-check`

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
| KRI-06 · Partidas sin conciliar a fin de mes | mayor es peor | 5 | 10 | 7 | alerta | sí |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

**Para revisar en el motor:** las «Fuentes» del reporte dicen «Sin documentos citados», aunque la ficha cita el acta.

**Reloj:** no creé ninguna tarea programada, porque nadie dio un sí explícito. Para correrlo a mano: `/criterio-risk-events:events-wake`. Cuándo vuelvo: sin reloj.

La salida quedó en `estado-riesgos/901888444-banco-control-de-riesgos-sintetico/corridas/salida-events-setup.md`, y la corrida se registró como `2026-11-25-events-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.