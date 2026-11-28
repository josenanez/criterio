# /criterio-assets:vendor-check 

Reporte de proveedores contra su nivel, periodo 2026-11, tal cual lo escribió el motor. La tabla del resultado salió sin filas.

# Cada proveedor contra su nivel · Banco del Istmo Sintético · periodo 2026-11

**Entidad:** Banco del Istmo Sintético (155612345-2-2019) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.2.0 · **Comando:** `vendor-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Proveedor | Métrica | Nivel del contrato | Medido | Crédito pactado | Facturado | Crédito en la factura |
|---|---|---|---|---|---|---|

Qué dice el contrato lo interpreta legal: aquí se dice qué incumplimiento se facturó completo.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-vendor-check-1`, con la salida guardada en `estado-tecnologia/155612345-2-2019-banco-del-istmo-sintetico/corridas/salida-vendor-check.md`.

Dos cosas sobre esta corrida:
- No registré ninguna aceptación de términos. Los términos 1.6 ya estaban vigentes y aceptados (instalada y aceptada 0.2.0), así que el motor no me pidió aceptar de nuevo.
- La tabla vacía no quiere decir que los proveedores cumplan. El reporte no cita ningún documento, así que no hay niveles de servicio cargados en la ficha del periodo. Para llenarla hay que correr `/criterio-assets:assets-scan` con los contratos de `40-proveedores/` en la carpeta.