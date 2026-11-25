# /criterio-data-governance:catalog-check 

Los cinco conjuntos del catálogo tienen dueño y clasificación, así que no hay nada que atender. Los términos 1.6 ya estaban vigentes y el reporte los muestra aceptados por José Francisco Ñáñez. No volví a registrar la aceptación.

# Cada conjunto con su dueño · Banco Control de Datos Sintético · periodo 2026-11

**Entidad:** Banco Control de Datos Sintético (901666888) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `catalog-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Conjunto | Dueño | Clasificación | Tipo | Datos personales |
|---|---|---|---|---|
| DS-01 · Clientes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-02 · Movimientos | Gerencia de operaciones | Restringida | Transaccional | no |
| DS-03 · Proveedores | Compras | Interna | Proveedores | sí |
| DS-04 · Candidatos | Gestión humana | Confidencial | Candidatos | sí |
| DS-05 · Indicadores de gestión | Planeación | Interna | Transaccional | no |

El dueño y la clasificación los asigna el área: aquí se dice cuál falta.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Entidad, identificación fiscal y país → Banco Control de Datos Sintético, 901666888, CO (respuesta sugerida a partir de la carpeta y la política de datos)
- Periodo → 2026-11 (respuesta sugerida: el mes de la fecha de la prueba)
- ¿Se publica en Rostrum? → Sí (por omisión; la política de datos no dice otra cosa)
- ¿Dónde se guarda el estado? → estado-datos/901666888-banco-control-de-datos-sintetico
- Términos 1.6 → Aceptados por José Francisco Ñáñez
- ¿Se deja la marca _CRITERIO_DATOS.txt? → No: sin un sí explícito no se crea nada en la carpeta de documentos

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

La salida quedó en `estado-datos/901666888-banco-control-de-datos-sintetico/corridas/salida-catalog-check.md`. La corrida quedó registrada como `2026-11-25-catalog-check-1` con 0 hallazgos.