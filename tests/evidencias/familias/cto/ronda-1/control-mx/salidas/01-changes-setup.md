# /criterio-changes:changes-setup tecnologia/rct190101ab2-retail-control-de-tecnologia-sintetico

Soy Fausto. Pongo cada cambio al lado de su aprobación y cada servicio al lado de su nivel; no apruebo cambios ni califico incidentes.

**Carpeta:** solo encontré una candidata, `tecnologia/rct190101ab2-retail-control-de-tecnologia-sintetico`. Tiene `00-politica/`, `10-cambios/`, `20-servicio/`, `30-activos/`, `40-proveedores/` y `50-nube/`, así que la tomé. Procesé sus 19 documentos y todos están donde deben estar.

**Respuestas que tomé de los documentos:**
- **Entidad:** Retail Control de Tecnología Sintético, RFC RCT190101AB2, México (MXN).
- **Periodo:** 2026-10.
- **Plazos:** 5 días para revisar un cambio de emergencia y 10 días para registrar el problema de un incidente mayor. Los dos salen de la política aprobada el 2025-11-20.
- **Rostrum:** sí se publica. La política no dice lo contrario.
- **Dónde guardo el estado:** `estado-tecnologia/rct190101ab2-retail-control-de-tecnologia-sintetico`.
- **Marca:** sí, dejé `_CRITERIO_TECNOLOGIA.txt` en la carpeta.
- **Términos 1.6:** los mostré tal cual y quedaron aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-changes-0.1.0-2026-11-25.md` y en su `.pdf`.

La configuración quedó en `.criterio/cambios/RCT190101AB2/config.json`.

Pasé las tres actas del comité de cambios a la ficha y las crucé contra la exportación de cambios y la de despliegues. Salieron tres aprobaciones y dos revisiones posteriores.

---

# Cada cambio con su aprobación · Retail Control de Tecnología Sintético · periodo 2026-10

**Entidad:** Retail Control de Tecnología Sintético (RCT190101AB2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `change-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Días de la política para revisar un cambio de emergencia:** 5.

| Cambio | Tipo | Implementado | Resultado | Aprobado | Revisado |
|---|---|---|---|---|---|
| CHG-100 | Normal | 2026-10-05 | Exitoso | 2026-10-01 | — |
| CHG-101 | Estándar | 2026-10-20 | Exitoso | — | — |
| CHG-102 | Emergencia | 2026-10-10 | Exitoso | — | 2026-10-15 |
| CHG-103 | Normal | 2026-10-08 | Exitoso | 2026-10-08 | — |
| CHG-104 | Normal | 2026-10-12 | Revertido | 2026-10-08 | 2026-10-15 |

| Despliegue | Fecha | Sistema | Cambio | En la exportación |
|---|---|---|---|---|
| D-100 | 2026-10-05 | Portal | CHG-100 | sí |
| D-101 | 2026-10-08 | Portal | CHG-103 | sí |

Si un cambio se aprueba lo decide el comité de cambios: aquí se dice cuál llegó a producción sin su aprobación o sin su revisión.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cto/FUENTES.es.md)

---

**Un fallo del motor:** la sección «Fuentes» del reporte dice «Sin documentos citados», pero cada aprobación y cada revisión de la ficha trae el acta de la que sale. El motor no está llevando esas fuentes al reporte, y hay que corregirlo.

**Cuándo vuelvo:** sin reloj, porque nadie dijo que sí a la tarea programada. Se corre a mano con `/criterio-changes:changes-wake`.

La corrida quedó registrada como `2026-11-25-changes-setup-1`. Lo que mostré aquí está en `estado-tecnologia/rct190101ab2-retail-control-de-tecnologia-sintetico/corridas/salida-changes-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.