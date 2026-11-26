# /criterio-data-governance:retention-check 

Los términos (v1.6) ya estaban vigentes y aceptados, así que no hizo falta registrar la aceptación. Corrí el reporte con `--today 2026-11-25` y no hay nada abierto en lo que procesa este comando.

# Las políticas y los plazos · Retail Control de Datos Sintético · periodo 2026-11

**Entidad:** Retail Control de Datos Sintético (RCC200101CD2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `retention-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Política | Aprobada | Revisión | Documento |
|---|---|---|---|
| Política de datos | 2024-06-30 | 2026-12-15 | `00-referencia/politica_de_datos.pdf` |
| Política de conservación | 2025-09-01 | 2027-09-01 | `00-referencia/politica_de_conservacion.pdf` |

| Conjunto | Tipo | Plazo | Registro más antiguo | Lo que vence antes del |
|---|---|---|---|---|
| DS-01 | Clientes | 120 meses | 2018-03-01 | 2016-11-25 |
| DS-02 | Transaccional | 120 meses | 2017-01-01 | 2016-11-25 |
| DS-03 | Proveedores | 60 meses | 2023-01-01 | 2021-11-25 |
| DS-04 | Candidatos | 24 meses | 2025-01-01 | 2024-11-25 |
| DS-05 | Transaccional | 120 meses | 2020-01-01 | 2016-11-25 |

Qué se borra o se archiva lo decide el dueño del dato con la política: aquí se dice qué pasó su plazo.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Periodo de la primera ficha? → 2026-11 (mes en curso a la fecha de la prueba), sugerida y tomada sin respuesta de la persona
- ¿Se publica en Rostrum? → Sí, por omisión; la política de datos no dice otra cosa
- ¿Dónde se guarda el estado? → estado-datos/rcc200101cd2-retail-control-de-datos-sintetico
- ¿Se marca la carpeta con _CRITERIO_DATOS.txt? → Sí, respuesta sugerida en la sesión de prueba

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-retention-check-1` con 0 hallazgos. La salida completa está en `estado-datos/rcc200101cd2-retail-control-de-datos-sintetico/corridas/salida-retention-check.md`.