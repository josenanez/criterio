# /criterio-roles:roles-setup talento/20601234567-servicios-andinos-control-sinteticos

Norma quedó configurada para Servicios Andinos Control Sintéticos (RUC 20601234567). La primera revisión de los dos perfiles de cargo no encontró nada que atender.

Es una prueba sin nadie que contestara, así que no hice preguntas: tomé ocho respuestas de los documentos y de la política de selección. Una destreza es exigible desde una importancia de 3,5 sobre 5; cada perfil se revisa cada 12 meses; y ningún perfil puede pedir edad, sexo, estado civil ni fotografía.

- **Configuración:** `.criterio/perfiles/20601234567/config.json`. El país, Perú, lo saqué del RUC en el nombre de la carpeta.
- **Términos (versión 1.6):** quedan aceptados a nombre de José Francisco Ñáñez, con fecha 2026-11-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-roles-0.1.0-2026-11-16.md` y `.pdf`.
- **Marca:** dejé `_CRITERIO_TALENTO.txt` en la carpeta de la entidad.
- **Estándar:** la descarga de O*NET se procesa; las ocupaciones 15-1232.00 y 41-2011.00 salen bien.
- **Estudios:** igualé Secundaria con CINE 3 y Técnico con CINE 5, pero con O*NET esa comparación no se calcula.
- **Fechas de revisión:** ningún perfil trae la fecha de su última revisión, así que la ficha la deja vacía y usa la próxima revisión que fija cada perfil.
- **Reloj:** no creé la tarea diaria porque pide un sí explícito y nadie lo dio. Se corre a mano con `/criterio-roles:roles-wake`.

Aparte de los perfiles, el inventario marcó un archivo que no se puede procesar: `30-candidatos/VAC-41/CAN-506/diploma.jpg`, porque el formato .jpg no se admite. Le toca a la selección (Cándido), no a esta revisión.

Este es el reporte tal como lo escribió el motor:

---

# Los perfiles contra su ocupación · Servicios Andinos Control Sintéticos · periodo 2026-11

**Entidad:** Servicios Andinos Control Sintéticos (20601234567) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Norma, versión 0.1.0 · **Comando:** `profile-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Perfil | Ocupación | Nivel | Estudios | Requisitos | Tareas | Del estándar sin recoger | Revisión |
|---|---|---|---|---|---|---|---|
| SA-01 · Analista de soporte | 15-1232.00 · Computer User Support Specialists (synthetic) | — | Técnico | 3 | 1 | 0 | 2027-02-01 |
| SA-02 · Cajero | 41-2011.00 · Cashiers (synthetic) | — | Secundaria | 2 | 1 | 0 | 2027-02-01 |

El perfil lo aprueba una persona: aquí se dice qué le falta frente a su ocupación y qué requisito no se apoya en una tarea.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-02 (families/criterio-chro/FUENTES.es.md)

---

El reporte cita O*NET solo como «F-02» y no trae la atribución que pide su licencia: «O*NET 31.0 Database, USDOL/ETA». Esa línea la agregué en la salida guardada, y faltaría que el motor la escriba. Además dice «Sin documentos citados», aunque procesó los dos archivos de `10-perfiles/`.

El reporte está en `estado-talento/20601234567-servicios-andinos-control-sinteticos/perfiles/2026-11/reporte-profile-check.md`. Lo que se mostró en la sesión quedó en `corridas/salida-roles-setup.md`, en esa misma carpeta, y la corrida quedó registrada como `2026-11-16-roles-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.