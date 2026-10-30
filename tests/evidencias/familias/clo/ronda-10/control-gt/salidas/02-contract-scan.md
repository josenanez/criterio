# /criterio-legal:contract-scan 

Las seis fichas de contrato ya existían y coinciden con sus documentos, así que no corregí ninguna. El motor no encontró señales ni problemas de ficha.

# Qué cambió en los contratos · Comercial Control de Guatemala · al 2026-10-06

**Entidad:** Comercial Control de Guatemala (61077291) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 1.1.0 · **Comando:** `contract-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

(El reporte del motor no trae resultado en esta corrida.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

---

- Los términos de la versión 1.3 ya estaban aceptados a nombre de José Francisco Ñáñez con fecha 2026-10-06, así que no hizo falta registrar nada.
- El inventario marcó los 57 documentos como nuevos, entre ellos los de los 6 contratos. Los 29 que tocan contratos se convirtieron sin ningún ilegible.
- El motor devolvió cero señales. Eso no coincide con lo que se ve en los documentos y no lo investigué:
  - CTR-3506 está terminado, con la póliza vigente hasta 2026-11-30.
  - CTR-3505 termina el 2026-11-20 y tiene una decisión de renovar sin prórroga automática.
  - En CTR-3502 el registro dice 1350000 y el contrato más el otrosí suman lo mismo.
  - Es posible que esas señales las produzcan otros comandos, como `contract-register`, `contract-execution` u `obligations-calendar`.
- La corrida quedó registrada como `2026-10-06-contract-scan-1`.