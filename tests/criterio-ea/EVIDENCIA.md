# criterio-ea · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada
vez, byte a byte. La clave de cada oficina, `material/<oficina>/clave.json`, la escribe el
generador al sembrar cada defecto; el motor no la ve. Los nombres, las personas, los órganos y los
correos son sintéticos.

## Las oficinas

| Carpeta del material | País | Proveedor | La oficina | Defectos sembrados | Señales esperadas |
|---|---|---|---|---:|---:|
| `banca` | Colombia | Outlook | La presidencia de una entidad financiera | 10 + 31 + 9 | 50 |
| `cooperativas` | Ecuador | Google | La gerencia general de una cooperativa | 6 + 31 | 35 |
| `control-co` | Colombia | Outlook | Una gerencia general | 0 | 0 |
| `control-ec` | Ecuador | Google | Una presidencia | 0 | 0 |

En total, **85 señales sembradas**: más de las 73 que pide un piso del 95 % sin fallas (decisión
0020). Cada defecto sembrado es la siembra —la señal una vez— más el lote de la oficina y, en
`banca`, los nueve de sus tres viajes.

**Cada oficina con su proveedor.** Lo que de verdad cambia de una oficina a otra no es el país sino
de dónde exporta. Las de Outlook traen la agenda como la exporta Outlook —la zona con su nombre de
Windows («SA Pacific Standard Time», «Eastern Standard Time»), el estado «libre» con
`X-MICROSOFT-CDO-BUSYSTATUS` y el día completo marcado aparte— y cada correo como un `.msg`, el
archivo compuesto de Outlook. Las de Google traen la agenda como la exporta Google Calendar —los
eventos únicos en UTC, la zona del calendario en el encabezado y la ocurrencia cancelada de una
serie como un evento aparte— y los correos en `.eml`.

Las dos de `cooperativas` que no dan señal son reglas, no señales: la agenda vieja y la carpeta
excluida. Cada oficina trae su carpeta al 26 de octubre de 2026: la referencia con sus dos órganos
y la ficha de la oficina, la agenda exportada en .ics, la sesión pasada de la junta con su acta
firmada —tres acuerdos, dos compromisos y una decisión pendiente con su propuesta—, la próxima
sesión de la junta, dos sesiones del comité y cuatro correos guardados, además de su lote.

## El lote

Las señales que se repiten se siembran además en un lote: casi todas en una sesión más del comité,
la del 5 de octubre, con su acta firmada, y en correos y reuniones propios.

| Defecto del lote | Señal | banca | cooperativas |
|---|---|---:|---:|
| Un acuerdo del acta sin responsable | `agreement_without_owner` | 6 | 6 |
| Un acuerdo del acta sin fecha | `agreement_without_date` | 5 | 6 |
| Un compromiso vencido entre el 12 y el 17 de octubre, sin un documento que lo sostenga | `commitment_overdue` | 6 | 6 |
| Un compromiso movido tres veces | `commitment_rescheduled` | 3 | 3 |
| Una decisión pendiente con su plazo el 3 o el 4 de noviembre | `decision_deadline` | 2 | 2 |
| Un correo que pide respuesta, con el plazo vencido y sin respuesta | `correspondence_unanswered` | 5 | 5 |
| Dos reuniones que se cruzan, un día distinto cada par | `meeting_conflict` | 4 | — |
| Una sesión extraordinaria del comité sin acta firmada pasados quince días | `meeting_without_minutes` | — | 3 |

La agenda de `cooperativas` es vieja: ahí un cruce no se cuenta, y por eso su lote no trae cruces.

## Los viajes

Cada oficina trae en `30-viajes/` el itinerario de la agencia de cada viaje, con cada vuelo, su
ruta, y su salida y su llegada en la hora local de cada ciudad con su desfase. La agente lleva cada
vuelo a la ficha del viaje; el motor lo cruza con la agenda.

| Viaje | Lo sembrado | Señal | Dónde |
|---|---|---|---|
| Quito, del 3 al 5 de noviembre | El vuelo de ida no está en la agenda | `trip_not_in_agenda` | banca |
| | El comité de riesgos, presencial en la sede de Bogotá, el 4 de noviembre | `meeting_while_away` | banca |
| | La cena del gremio, en Bogotá, empieza durante el vuelo de vuelta | `meeting_during_flight` | banca |
| Medellín, el 27 de octubre | El vuelo de ida no está en la agenda | `trip_not_in_agenda` | banca |
| | La reunión con el sindicato, presencial en la sede de Bogotá | `meeting_while_away` | banca |
| | Una llamada durante el vuelo de vuelta | `meeting_during_flight` | banca |
| Cali, el 28 de octubre | Ninguno de los dos vuelos está en la agenda | `trip_not_in_agenda` × 2 | banca |
| | La visita a la oficina principal, presencial en Bogotá | `meeting_while_away` | banca |

Lo que se parece a un defecto y no lo es: en el viaje a Quito, una reunión en Quito y un comité por
Microsoft Teams; el vuelo de vuelta en la agenda, que no se cruza como reunión. En `control-co`, un
viaje a Medellín con los dos vuelos en la agenda, una visita a la planta en Medellín y un comité
por Teams. En `control-ec`, un viaje a Santiago de Chile —la llegada en la hora de Santiago, dos
horas más que Quito en noviembre— con una reunión allá y un directorio por Google Meet. En
`cooperativas`, un viaje a Guayaquil con los dos vuelos fuera de la agenda y una asamblea en Quito:
su agenda es vieja, y entonces el viaje no se cruza.

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
| Una reunión de seguimiento dentro del bloque libre —en Outlook, libre por su `X-MICROSOFT-CDO-BUSYSTATUS`— | No cruza | control-co, control-ec |
| La ocurrencia del comité del 26 de octubre, cancelada como un evento aparte, y un desayuno a esa hora | No cruzan | control-ec |
| Los correos en `.msg`, con su respuesta guardada también en `.msg` | El motor los lee como un `.eml` y la respuesta cierra el pedido | banca, control-co |
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
- **Todas las variantes de cada proveedor.** El material trae lo que Outlook y Google Calendar
  ponen distinto en el .ics y el .msg de Outlook; una exportación con otra extensión propia puede
  traer lo que el lector no procesa, y entonces lo declara. Las zonas con nombre de Windows son las
  de la región y las de las casas matrices más comunes; una que no está se declara.
- **Las repeticiones fuera de lo soportado.** Diarias, semanales por día y mensuales por día del mes,
  con intervalo, conteo, fecha final, excepciones y ocurrencias movidas; cualquier otra se declara,
  no se adivina.
- **Un itinerario sin la zona de sus horas.** Si el documento no la dice, el vuelo queda sin esa
  hora y no se cruza: el motor lo pide en la ficha.
- **Otras oficinas de otros países.** Ofelia no procesa nada propio de un país; el material es de Colombia y Ecuador, con una tercera zona horaria, y lo que falta probar son las exportaciones de cada proveedor, no los países.
