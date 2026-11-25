# /criterio-data-governance:governance-scan 

El inventario marca todos los documentos como nuevos porque es la primera vez que corre este comando. La ficha del periodo ya tenía las políticas, los plazos de conservación y los términos del informe tal como los dicen los documentos, así que no agregué nada. El motor tampoco devolvió documentos pendientes por llevar a la ficha.

# Qué cambió en el gobierno · Banco Control de Datos Sintético · periodo 2026-11

**Entidad:** Banco Control de Datos Sintético (901666888) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `governance-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Conjuntos en el catálogo:** 5 · **Con datos personales:** 3 · **Políticas en la ficha:** 2 · **Términos de los informes:** 4.

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

---

La corrida quedó registrada como `2026-11-25-governance-scan-1`, con la salida en `estado-datos/901666888-banco-control-de-datos-sintetico/corridas/salida-governance-scan.md`.