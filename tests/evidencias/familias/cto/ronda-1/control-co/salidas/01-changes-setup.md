# /criterio-changes:changes-setup tecnologia/901333666-banco-control-de-tecnologia-sintetico

Soy Fausto. Pongo cada cambio al lado de su aprobación y cada servicio al lado de su nivel; no apruebo cambios ni califico incidentes.

**Carpeta:** encontré una sola, `tecnologia/901333666-banco-control-de-tecnologia-sintetico`, con las seis carpetas que espera la estructura (00-politica a 50-nube). Esa es. Tiene 19 documentos nuevos, ninguno fuera de lugar ni ilegible.

**Las respuestas, tomadas de los documentos porque nadie respondía en esta sesión:**
- **Entidad:** Banco Control de Tecnología Sintético, NIT 901333666, Colombia (COP).
- **Periodo:** 2026-10, el de las tablas de cambios y de servicio.
- **Revisión de un cambio de emergencia:** 5 días, según la política aprobada el 2025-11-20.
- **Problema de un incidente mayor:** 10 días, según la misma política.
- **Publicar en Rostrum:** sí. Es lo que se hace por omisión y la política no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-tecnologia/901333666-banco-control-de-tecnologia-sintetico`.
- **Marca:** `_CRITERIO_TECNOLOGIA.txt` quedó en la carpeta de la entidad.

**Términos (versión 1.6, 2026-11-16):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Aceptados por José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-changes-0.1.0-2026-11-25.md` y en el `.pdf` con el mismo nombre.

**Configuración:** quedó en `.criterio/cambios/901333666/config.json` y pasó la validación.

Procesé las 3 actas del comité de cambios. A la ficha llevé 3 aprobaciones (CHG-100, CHG-103 y CHG-104) y 2 revisiones posteriores (CHG-102 y CHG-104). En octubre no encontré nada que atender: no hay cambios sin aprobación ni sin revisión, ni despliegues sin su cambio.

---

# Cada cambio con su aprobación · Banco Control de Tecnología Sintético · periodo 2026-10

**Entidad:** Banco Control de Tecnología Sintético (901333666) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Fausto, versión 0.1.0 · **Comando:** `change-check`

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

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión nadie lo dio. Se corre a mano con `/criterio-changes:changes-wake`.

La salida quedó en `estado-tecnologia/901333666-banco-control-de-tecnologia-sintetico/corridas/salida-changes-setup.md` y la corrida quedó registrada como `2026-11-25-changes-setup-1`.

Algo que debes saber de la prueba: la llamada a `dejar-listo` la corrí con `cd … &&`, y el comando pide llamar al motor sin `cd` ni `&&`. El resultado es el mismo, pero esa llamada no siguió la regla.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.