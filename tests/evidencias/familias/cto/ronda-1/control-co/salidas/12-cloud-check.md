# /criterio-assets:cloud-check 

Corrí la comparación de la nube contra su presupuesto para 2026-11, pero la tabla salió vacía. El motor no recibió ninguna factura de la nube con cuentas, así que no hay ninguna cuenta que comparar. Tampoco hay ninguna señal abierta, porque no había nada que revisar. Una tabla vacía no prueba que ninguna cuenta se pasara.

Si hay una factura de la nube de noviembre, hay que dejarla en la carpeta de tecnología de la entidad, donde `technology-intake` indica, y volver a correr `/criterio-assets:cloud-check`.

# La nube contra su presupuesto · Banco Control de Tecnología Sintético · periodo 2026-11

**Entidad:** Banco Control de Tecnología Sintético (901333666) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Domingo, versión 0.1.0 · **Comando:** `cloud-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Tolerancia de la política sobre el presupuesto de cada cuenta:** 5 %.

| Cuenta | Facturado | Presupuesto |
|---|---|---|

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-02 (families/criterio-cto/FUENTES.es.md)

Los términos (versión 1.6) ya estaban vigentes, así que no pedí aceptarlos de nuevo ni registré ninguna aceptación. Le pasé `--today 2026-11-25` al motor en cada llamada, también en la de términos.

La salida quedó en `estado-tecnologia/901333666-banco-control-de-tecnologia-sintetico/corridas/salida-cloud-check.md`. La corrida quedó registrada como `2026-11-25-cloud-check-1`, con 0 hallazgos.