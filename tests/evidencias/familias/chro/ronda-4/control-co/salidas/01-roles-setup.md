# /criterio-roles:roles-setup talento/900777888-cooperativa-control-sintetica

Norma quedó instalada para Cooperativa Control Sintética (NIT 900777888), y el primer reporte de perfiles no tiene nada abierto.

- **Configuración:** `.criterio/perfiles/900777888/config.json`. Usa la CUOC con la descarga de `00-referencia/estandar/`. Las demás respuestas salieron de los documentos:
  - **Revisión de perfiles:** cada 12 meses, según la política de selección.
  - **Lo que no se puede pedir:** edad, sexo, estado civil y fotografía, según la misma política.
  - **Equivalencia de estudios con la CINE:** Profesional 6, Tecnólogo 5, Técnico laboral 4. La propuse yo a partir de los perfiles; ningún documento de la entidad la fija, así que conviene que la confirme una persona.
- **Términos 1.6:** aceptados por José Francisco Ñáñez con fecha 2026-11-16. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-roles-0.2.0-2026-11-16.md` y en `.pdf`.
- **Marca:** dejé `_CRITERIO_TALENTO.txt` en la carpeta de la entidad.
- **Estándar:** la descarga se procesa. Las tres ocupaciones que citan los perfiles (24111, 43111 y 25120) salen completas.
- **Ficha y reporte:** procesé los tres perfiles (PC-11, PC-12 y PC-13). Cada elemento del estándar está recogido o excluido con su motivo; por ejemplo, la legislación tributaria en PC-11 la lleva el área de impuestos. No hay señales abiertas.
  - La próxima revisión de PC-11 es el 2026-11-17, un día después del corte. Todavía no está vencida, pero la siguiente revisión de Norma la va a encontrar.
  - El reporte está en `estado-talento/900777888-cooperativa-control-sintetica/perfiles/2026-11/reporte-profile-check.md`, y la corrida quedó registrada como `2026-11-16-roles-setup-1`.
- **Un archivo no se pudo procesar:** `30-candidatos/VAC-31/CAN-406/diploma.jpg`, porque el motor no lee `.jpg`. Es de la selección, así que le corresponde a Cándido, no a Norma.
- **Sin reloj:** la tarea programada necesita un sí explícito y en esta prueba nadie podía darlo. Para correrlo a mano: `/criterio-roles:roles-wake`.
- **Un error que corregí:** la primera vez escribí las preguntas de la ficha como texto plano y el motor falló al calcular. Las pasé al formato pregunta-respuesta que espera y volví a calcular.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.