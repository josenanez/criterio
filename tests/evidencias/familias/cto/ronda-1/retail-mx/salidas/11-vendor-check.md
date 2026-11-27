# /criterio-assets:vendor-check 

Los términos (v1.6) ya estaban vigentes, así que no hizo falta registrar la aceptación. Corrí el reporte del periodo 2026-11 con fecha de corte 2026-11-25.

# Cada proveedor contra su nivel · Retail del Golfo Sintético · periodo 2026-11

**Entidad:** Retail del Golfo Sintético (RGS180610QW4) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `vendor-check`

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

La tabla de resultados salió vacía: la ficha del periodo no tiene ningún nivel de servicio de proveedor. Eso no es lo mismo que decir que todos cumplieron. Para llenarla hay que correr `/criterio-assets:assets-scan`, que lleva a la ficha los niveles y los créditos de los contratos de `40-proveedores/`.

La salida quedó en `estado-tecnologia/rgs180610qw4-retail-del-golfo-sintetico/corridas/salida-vendor-check.md`. La corrida quedó registrada como `2026-11-25-vendor-check-1`. El registro reporta 18 hallazgos, que corresponden a otros comandos, no a este.