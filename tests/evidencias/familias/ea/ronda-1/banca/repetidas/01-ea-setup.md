# /criterio-assistant:ea-setup direccion/presidencia

Me detuve en el paso 3: la configuración no valida y no la completé. Aún no hay aceptación de términos registrada, ni estado, fichas, reporte ni corrida.

**Qué falta.** El motor exige `entity.id` (la identificación fiscal de Banco Andino) y no aparece en ningún documento. `oficina.md` trae el nombre de la entidad, la asistente, el correo de la oficina y la zona horaria, pero no el NIT. No lo inventé ni usé el número del ejemplo. Con el campo vacío, `config` devolvió: `entity.id vacío`.

**Lo que sí hice**
- **Carpeta raíz:** la única candidata era `direccion/presidencia`, con 00-referencia/, 10-agenda/, 20-correspondencia/ y 90-borradores/. La tomé como la raíz. No dejé `_CRITERIO_DIRECCION.txt` ni moví nada.
- **Agenda:** hay una exportación en `10-agenda/` (`agenda-2026-10-25.ics`). El inventario la marca como ilegible: «formato .ics no soportado». Es probable que el reporte de agenda salga vacío o sin cruces, a menos que el motor la convierta (tiene un comando `convertir`, que no probé).
- **Sesiones:** `organos/` tiene 4 sesiones. Comité de presidencia: 2026-09-21 y 2026-10-19. Junta directiva: 2026-09-24 y 2026-10-29.
- **Correspondencia:** hay 4 correos en `20-correspondencia/`.
- **Órganos que se siguen** (de `organos.csv`):
  - junta-directiva: nueve miembros, último jueves de cada mes.
  - comite-de-presidencia: los vicepresidentes, los lunes.
- **Configuración:** la escribí en `.criterio/direccion/presidencia/config.json` con estas respuestas:

| Campo | Valor |
|---|---|
| Entidad | Banco Andino, país CO |
| Ejecutivo y asistente | Presidencia; Laura Gómez |
| Correo de la oficina | presidencia@bancoandino.test |
| Zona horaria | America/Bogota |
| Carpetas excluidas | ninguna |
| Publica en Rostrum | no |
| Umbrales | los de `config.example.json` |
| Estado | `estado-direccion/presidencia`, fuera de la carpeta de documentos |

- **Términos:** el motor dice que no están vigentes porque no hay aceptación registrada (versión 1.2). Los mostré tal cual y no los acepté. Cuando esté el NIT, se registra la aceptación a nombre de José Francisco Ñáñez, con fecha 2026-10-26, como indicaste.

**Para continuar:** dime el NIT, o confirma que uso un valor de prueba, y corro `init`, `config`, `aceptar`, `compute` y `reporte`, y dejo la corrida registrada.