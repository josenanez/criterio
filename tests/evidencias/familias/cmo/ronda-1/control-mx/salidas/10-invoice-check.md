# /criterio-campaigns:invoice-check 

Los términos están vigentes (versión 1.6), así que el reporte se produjo. Las cinco facturas de pauta del periodo 2026-11 tienen campaña y orden de compra.

# Cada factura con su campaña · Consumo Control de Mercadeo Sintético · periodo 2026-11

**Entidad:** Consumo Control de Mercadeo Sintético (CCM220101ZZ9) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `invoice-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Factura | Proveedor | Campaña | Orden de compra | Valor | En el plan |
|---|---|---|---|---|---|
| F-101 | Televisora Sintética | C-01 | OC-301 | 60,000,000 | sí |
| F-102 | Televisora Sintética | C-01 | OC-301 | 44,000,000 | sí |
| F-103 | Redes Sintéticas | C-02 | OC-302 | 18,000,000 | sí |
| F-104 | Exteriores Sintéticos | C-03 | OC-303 | 25,000,000 | sí |
| F-105 | Radio Sintética | C-04 | OC-304 | 7,000,000 | sí |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-invoice-check-1`, con 0 hallazgos. La salida está en `estado-mercadeo/ccm220101zz9-consumo-control-de-mercadeo-sintetico/corridas/salida-invoice-check.md`.

Las instrucciones pedían registrar la aceptación de términos con el nombre de José Francisco Ñáñez. No lo hice, porque el comando `terminos` ya mostraba una aceptación vigente (`aceptada: 0.1.0`). Registrarla es trabajo de `/criterio-campaigns:campaigns-setup`.