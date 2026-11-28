# /criterio-talent:candidate-fit 

Los términos están vigentes (versión 1.6). Dos candidatos tienen un requisito esencial sin evidencia. El perfil PT-03 también incluye un requisito de religión, que es un dato protegido. Conviene revisarlo con `/criterio-talent:privacy-check` o con Norma. Las tablas van en el orden del identificador, sin puntaje.

# Cada candidato contra el perfil · Almacenes del Pacífico Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Pacífico Sintéticos (1792345678001) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 1.0.0 · **Comando:** `candidate-fit`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Requisito esencial sin evidencia (`requirement_not_evidenced`) | CAN-601: el requisito esencial R1 «Escucha activa con el cliente» del perfil PT-01 no tiene evidencia ni en la hoja de vida ni en sus soportes | `30-candidatos/VAC-51/CAN-601/hoja-de-vida.pdf` |
| 2 | Requisito esencial sin evidencia (`requirement_not_evidenced`) | CAN-608: el requisito esencial R1 «Coordinación del equipo de ventas» del perfil PT-03 no tiene evidencia ni en la hoja de vida ni en sus soportes | `30-candidatos/VAC-52/CAN-608/hoja-de-vida.pdf` |

## El resultado

Las tablas se copian tal cual del reporte. Las rutas de «Dónde» son `30-candidatos/<vacante>/<candidato>/hoja-de-vida.pdf, p. 1`. Ningún requisito de ningún candidato tiene soporte.

**CAN-601 · VAC-51 · PT-01**

| Requisito | Esencial | Evidencias | Con soporte | Dónde |
|---|---|---|---|---|
| R1 · Escucha activa con el cliente | sí | 0 | no | — |
| R2 · Matemáticas para el arqueo de caja | sí | 1 | no | VAC-51/CAN-601, p. 1 |
| R3 · Buena presencia | no | 0 | no | — |

**CAN-602, CAN-603, CAN-604, CAN-605, CAN-606 y CAN-610 · VAC-51 · PT-01.** Cada uno tiene la misma tabla:

| Requisito | Esencial | Evidencias | Con soporte | Dónde |
|---|---|---|---|---|
| R1 · Escucha activa con el cliente | sí | 1 | no | su hoja de vida, p. 1 |
| R2 · Matemáticas para el arqueo de caja | sí | 1 | no | su hoja de vida, p. 1 |
| R3 · Buena presencia | no | 0 | no | — |

**CAN-607 · VAC-52 · PT-03**

| Requisito | Esencial | Evidencias | Con soporte | Dónde |
|---|---|---|---|---|
| R1 · Coordinación del equipo de ventas | sí | 1 | no | VAC-52/CAN-607, p. 1 |
| R2 · Percepción social | no | 0 | no | — |
| R3 · Ventas y mercadeo | no | 0 | no | — |
| R4 · Profesar la religión católica | no | 0 | no | — |

**CAN-608 · VAC-52 · PT-03**

| Requisito | Esencial | Evidencias | Con soporte | Dónde |
|---|---|---|---|---|
| R1 · Coordinación del equipo de ventas | sí | 0 | no | — |
| R2 · Percepción social | no | 0 | no | — |
| R3 · Ventas y mercadeo | no | 0 | no | — |
| R4 · Profesar la religión católica | no | 0 | no | — |

**CAN-609 · VAC-53 · PT-02**

| Requisito | Esencial | Evidencias | Con soporte | Dónde |
|---|---|---|---|---|
| R1 · Escucha activa con el cliente | no | 0 | no | — |
| R2 · Matemáticas para el arqueo de caja | no | 0 | no | — |
| R3 · Servicio al cliente | no | 0 | no | — |

Los candidatos van en el orden de su identificador. No hay puntaje ni orden por número: quien selecciona decide.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Plazo de cobertura de una vacante → 30 días, de la política de selección (respuesta sugerida, sesión sin interfaz).
- Días de conservación de los datos de un candidato → 120 días, de la política de selección (respuesta sugerida, sesión sin interfaz).
- ¿Se publican los reportes de candidatos en Rostrum? → No (propuesta por omisión, sesión sin interfaz).

## Fuentes

- `30-candidatos/VAC-51/CAN-601/hoja-de-vida.pdf`
- `30-candidatos/VAC-52/CAN-608/hoja-de-vida.pdf`

La corrida quedó registrada como `2026-11-16-candidate-fit-1`, con 13 hallazgos. El reporte completo está en `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos/seleccion/2026-11/reporte-candidate-fit.md`.

Dos aclaraciones sobre esta respuesta:
- **Términos:** no hizo falta registrar la aceptación. Ya estaba vigente, con aceptación de la versión 1.0.0, así que no corrí `talent-setup`.
- **Tablas:** resumí las de CAN-602 a CAN-606 y CAN-610 en una sola tabla común, porque son idénticas. El archivo guardado en `corridas/salida-candidate-fit.md` lleva las tablas completas, una por candidato.