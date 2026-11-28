# /criterio-claims:approval-check 

Los términos de la versión 1.6 están vigentes. Salieron seis señales: dos piezas publicadas antes de su aprobación, dos bases de contactos sin autorización para mercadeo y dos piezas pagadas a influenciadores sin identificarse como publicidad. La decisión sobre cada una es de legal y de mercadeo.

# La aprobación y la autorización · Seguros Cordillera Sintéticos · periodo 2026-11

**Entidad:** Seguros Cordillera Sintéticos (96789012-3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 1.0.0 · **Comando:** `approval-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Pieza publicada sin la aprobación que pide la política, o antes de ella (`piece_published_unapproved`) | P-05 · Hecho en casa: se publicó el 2026-10-12 y se aprobó el 2026-10-15, después | 3 | `10-piezas/registro_de_piezas.xlsx` fila 6 |
| 2 | Ídem | P-42 · Devoluciones: se publicó el 2026-10-14 y se aprobó el 2026-10-16, después | 2 | `10-piezas/registro_de_piezas.xlsx` fila 11 |
| 3 | Base de contactos usada en una campaña sin autorización para mercadeo (`contact_base_without_consent`) | B-02: la usa la campaña C-02 y el registro de bases no le da autorización | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 3 |
| 4 | Ídem | B-12: la usa la campaña C-12 y el registro de bases no le da autorización | — | `50-campanas/plan_de_mercadeo.xlsx` fila 6 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 5 |
| 5 | Pieza pagada a un influenciador sin identificarse como publicidad (`sponsored_content_unidentified`) | P-04 · Reseña de una creadora: pagada a @creadora_sintetica | — | `10-piezas/registro_de_piezas.xlsx` fila 5 |
| 6 | Ídem | P-32 · Visita de un creador: pagada a @creador_invitado_sintetico | — | `10-piezas/registro_de_piezas.xlsx` fila 10 |

El reporte completo, con las tablas de resultado por pieza y por base, está en `estado-mercadeo/96789012-3-seguros-cordillera-sinteticos/piezas/2026-11/reporte-approval-check.md`. Todo lo que llegó se procesó y el motor no hizo preguntas. Fuentes: `registro_de_piezas.xlsx`, `registro_de_bases_de_contactos.xlsx` y `plan_de_mercadeo.xlsx`.

La corrida quedó registrada como `2026-11-25-approval-check-1`, con la salida en `corridas/salida-approval-check.md`.

Dos cosas que no coinciden con lo que pedía la prueba:

- **Términos:** el motor los dio por vigentes, con la aceptación `1.0.0` ya registrada. No mostró ningún texto para aceptar, así que no registré ninguna aceptación a nombre de José Francisco Ñáñez.
- **Salida guardada:** en este mensaje acorté la tabla de señales (quité la columna de monto y responsable, que iban vacías). El archivo guardado lleva el reporte íntegro, con una nota breve antes del encabezado.