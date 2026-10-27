# criterio-ea · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada
vez, byte a byte. La clave de cada oficina, `material/<oficina>/clave.json`, la escribe el
generador al sembrar cada defecto; el motor no la ve. Los nombres, las personas, los órganos y los
correos son sintéticos.

## Las oficinas

| Carpeta del material | País | La oficina | Defectos sembrados | Señales esperadas |
|---|---|---|---:|---:|
| `banca` | Colombia | La presidencia de una entidad financiera | 10 | 10 |
| `cooperativas` | Ecuador | La gerencia general de una cooperativa | 6 | 4 |
| `control-co` | Colombia | Una gerencia general | 0 | 0 |
| `control-ec` | Ecuador | Una presidencia | 0 | 0 |

Las dos de `cooperativas` que no dan señal son reglas, no señales: la agenda vieja y la carpeta
excluida. Cada oficina trae su carpeta al 26 de octubre de 2026: la referencia con sus dos órganos
y la ficha de la oficina, la agenda exportada en .ics, la sesión pasada de la junta con su acta
firmada —tres acuerdos, dos compromisos y una decisión pendiente con su propuesta—, la próxima
sesión de la junta, dos sesiones del comité y cuatro correos guardados.

## Lo que se siembra, y la señal que tiene que levantar

| Defecto | Señal | Dónde |
|---|---|---|
| La sesión de la junta y la visita del supervisor se cruzan el 29 de octubre | `meeting_conflict` | banca |
| Una llamada semanal a las 9:00 de Nueva York y una revisión semanal a las 9:00 de Bogotá: solo se cruzan el 3 de noviembre, después del cambio de hora | `meeting_conflict` | banca |
| La junta del 29 de octubre sin material a tres días | `meeting_without_material` | banca |
| El comité del 21 de septiembre con notas y sin acta firmada | `meeting_without_minutes` | banca |
| El mismo comité con un borrador puesto en `40-acta/`, que no cuenta como acta | `meeting_without_minutes` | cooperativas |
| Un acuerdo del acta sin responsable | `agreement_without_owner` | banca, cooperativas |
| Un acuerdo del acta sin fecha, «por definir» | `agreement_without_date` | banca |
| Un compromiso que venció el 15 de octubre sin un documento que lo sostenga | `commitment_overdue` | banca, cooperativas |
| Un compromiso movido tres veces | `commitment_rescheduled` | banca |
| Una decisión pendiente cuya oferta vence el 2 de noviembre | `decision_deadline` | banca |
| Un requerimiento del supervisor con plazo el 20 de octubre, sin respuesta guardada | `correspondence_unanswered` | banca, cooperativas |

## Las reglas de la operación real

| Caso | Lo que tiene que pasar | Dónde |
|---|---|---|
| La agenda exportada el 12 de octubre, con un cruce | Avisa que la agenda es vieja y no cuenta el cruce | cooperativas |
| Un borrador en `40-acta/` | Lo dice como no procesado y la sesión sigue sin acta | cooperativas |
| Un correo en `20-correspondencia/personal/`, excluida, que pide respuesta con el plazo vencido | No se procesa ni se menciona como pendiente | cooperativas |
| Un bloque de concentración marcado como libre y una visita cancelada, a la misma hora que otras reuniones | No cruzan | todas |
| Un día completo sin reuniones | No cruza con nada | todas |
| El informe | No se publica en Rostrum: la configuración no lo dice | todas |

## Lo que se parece a un defecto y no lo es

Las oficinas de control traen lo mismo que las otras, sin un defecto: el compromiso con su evidencia
en el material, el comité con su acta firmada, el requerimiento del supervisor con su respuesta
guardada, el correo de un cliente respondido a tiempo y un boletín que no pide respuesta. Las cuatro
oficinas traen además el comité reciente, todavía en plazo para su acta, y un compromiso movido una
sola vez. **Cualquier señal en un control es una falla.**

## Lo que el material no prueba

- **La oficina de un ejecutivo real.** Nada de esto se ha corrido sobre la agenda, las actas o la
  correspondencia de una organización.
- **Los formatos de exportación de cada proveedor de calendario y de correo.** El .ics y el .eml del
  material siguen sus normas (F-02, F-03); una exportación con extensiones propias de un proveedor
  puede traer lo que el lector no procesa, y entonces lo declara.
- **Las repeticiones fuera de lo soportado.** Diarias, semanales por día y mensuales por día del mes,
  con intervalo, conteo, fecha final, excepciones y ocurrencias movidas; cualquier otra se declara,
  no se adivina.
- **Los correos .msg.** La estructura los acepta en `20-correspondencia/`; el motor procesa .eml.
- **Los viajes.** Los itinerarios contra la agenda son el incremento 2.
- **Otras oficinas de otros países.** Ofelia no procesa nada propio de un país; el material es de Colombia y Ecuador, con una tercera zona horaria, y lo que falta probar son las exportaciones de cada proveedor, no los países.
