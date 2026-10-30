---
name: ea-intake
description: "Qué documentos procesa Ofelia en la oficina de un ejecutivo, dónde va cada uno, qué procesa el código directamente y qué extrae la agente a la ficha. Úsalo al recorrer la carpeta de la oficina, al recibir una exportación de la agenda, un correo guardado, un itinerario, una convocatoria, notas o un acta, o al explicar dónde va un archivo. Executive office document intake, folder structure."
---

# Los documentos de la oficina del ejecutivo

## Dos clases de documento, dos formas de procesarlo

**Lo que tiene formato lo procesa el código.** La agenda exportada en `.ics` —eventos, repeticiones, excepciones y zonas horarias, como la exportan Outlook y Google Calendar— y los encabezados de cada correo guardado en `.eml` o en `.msg` de Outlook —quién, a quién, cuándo, el asunto y a qué mensaje responde— los procesa `asistente.py`. No se transcriben ni se interpretan: un evento que el código no puede leer se declara, no se adivina.

**Lo que solo trae un documento escrito lo extrae la agente a la ficha.** La convocatoria y el orden del día, las notas o la transcripción, el acta firmada con sus acuerdos y compromisos, el material que plantea una decisión, el cuerpo de un correo que pide algo, los vuelos de un itinerario. Se convierte con `asistente.py convertir` y se registra con su cita: la ficha de cada sesión con **meeting-record**, la de cada decisión con **decision-brief**, la de cada correo con **correspondence-record**, la de cada viaje con **travel-record**.

## Exportaciones, no cuentas

Ofelia no se conecta al buzón ni al calendario. Procesa lo que la oficina exporta: la agenda en `.ics`, con la fecha de la exportación en el nombre (`agenda-AAAA-MM-DD.ics`), los correos guardados como archivo, uno por mensaje, y los itinerarios de cada viaje. Una conexión directa es otra decisión, con su revisión de privacidad.

## Lo que nunca toca

Las actas, las agendas y los correos originales no se editan. Ofelia escribe solo en su estado, en `.criterio/direccion/` y en `90-borradores/`, y cada borrador lleva «BORRADOR» en el nombre y en el texto. Un borrador que aparece en `40-acta/` no es el acta: el motor lo dice.

Las carpetas excluidas de la configuración no se procesan, y cada informe las nombra.

<!-- ea:intake · generado por scripts/familias.py; no se edita a mano -->
Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo está fuera de su lugar y dónde iría (ADR 0007). Cada sesión tiene un solo lugar, su carpeta en `organos/<órgano>/<AAAA-MM-DD>/`: Ofelia procesa su convocatoria, su material, sus notas y su acta firmada.

Una carpeta por ejecutivo que se asiste. Dentro, la referencia de su oficina, su agenda, su correspondencia, los borradores que prepara Ofelia y una carpeta por reunión de cada órgano.

```
direccion/
└── <ejecutivo>/
    ├── 00-referencia/
    ├── 10-agenda/
    ├── 20-correspondencia/
    ├── 30-viajes/
    ├── 90-borradores/
    └── organos/<órgano>/<AAAA-MM-DD>/
        ├── 10-convocatoria/
        ├── 20-material/
        ├── 30-notas/
        └── 40-acta/
estado-direccion/
```

**`<ejecutivo>/`** · La oficina de un ejecutivo

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | Los órganos que se siguen —junta, comité de presidencia, comités de la junta—, quién los integra y su calendario de sesiones | Ofelia |
| `10-agenda/` | Las exportaciones de la agenda en .ics, con la fecha de la exportación en el nombre | Ofelia |
| `20-correspondencia/` | Los correos guardados como archivo, uno por mensaje: .eml, o .msg de Outlook | Ofelia |
| `30-viajes/` | Los itinerarios de cada viaje —el de la agencia, el pasaje de la aerolínea—, uno por viaje, con la fecha de salida en el nombre | Ofelia |
| `90-borradores/` | Lo único que escribe Ofelia entre los documentos: borradores de actas y de respuestas, con «BORRADOR» en el nombre | Ofelia |

**`organos/<órgano>/<AAAA-MM-DD>/`** · Una sesión de un órgano, con su fecha como nombre de la carpeta

| Carpeta | Qué va | Agente |
|---|---|---|
| `10-convocatoria/` | La convocatoria y el orden del día | Ofelia |
| `20-material/` | El material que se envía a los miembros antes de la sesión | Ofelia |
| `30-notas/` | Las notas o la transcripción de la sesión | Ofelia |
| `40-acta/` | El acta firmada. Ofelia nunca archiva un borrador aquí | Ofelia |

**`estado-direccion/`** · Lo que escribe Ofelia: la configuración, las fichas de cada reunión, de cada hilo y de cada exportación, y los informes. Ninguna persona lo edita, y Ofelia no escribe fuera de aquí ni de `90-borradores/`.
<!-- /ea:intake -->
