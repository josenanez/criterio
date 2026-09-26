---
name: product-metrics
description: La serie medida de un producto con su fuente y su fecha, y el contraste entre lo que el negocio declara y lo que los datos miden. Se carga al consolidar métricas de producto o al revisar una cifra del caso de negocio.
---

# Las métricas del producto, y la cifra del negocio

Dos cosas que se parecen y no son lo mismo:

- **Lo declarado** — el número que está en el caso de negocio, en la presentación del
  comité o en la definición. Tiene autor y tiene fecha.
- **Lo medido** — el número que sale del sistema donde el producto vive. Tiene fuente y
  tiene fecha de corte.

Cuando no coinciden, el hallazgo no es que alguien se equivocó: **es que la cifra con la
que se está decidiendo es de marzo y la realidad es de septiembre.** Nadie miente. El
documento no se reexpide.

## La serie

Una métrica por archivo, en `<estado>/metrics/<nombre>.json`:

```json
{
  "metric": "tx_mensuales",
  "source": "tablero transaccional · reporte mensual",
  "definition": "transacciones confirmadas, sin reversiones, del canal QR",
  "series": [{"date": "2026-08-01", "value": 150000},
             {"date": "2026-09-01", "value": 180000}]
}
```

Tres reglas:

1. **`source` es obligatoria.** Una serie sin fuente no se puede auditar, y una cifra que
   no se puede auditar no debería estar en un comité.
2. **`definition` importa más de lo que parece.** *«Transacciones»* con reversiones y sin
   reversiones son dos series distintas con el mismo nombre, y esa es la discusión que se
   descubre en el comité a mitad de la presentación.
3. **La serie se agrega, no se corrige.** Un punto mal tomado se corrige agregando el punto
   correcto con su fecha, no reescribiendo el anterior. Es la misma regla de la línea base.

## El contraste

En `producto.json`, cada afirmación numérica de la definición se declara así:

```json
"claims": [{"metric": "tx_mensuales", "declared": 250000,
            "source": "caso-negocio-2026-03.md", "source_date": "2026-03-04"}]
```

El cálculo compara contra **el punto más reciente de la serie** y emite `claim_vs_metric`
cuando la diferencia pasa de `claim_gap_pct`. La señal lleva **las dos fuentes y las dos
fechas**, y eso no es un detalle de formato:

> *«el negocio y los datos no coinciden»* no le permite a nadie hacer nada.
> *«el caso de negocio del 4 de marzo dice 250.000 y el tablero transaccional mide 180.000
> al 1 de septiembre»* sí.

Y lleva la dirección. **Declarado por encima de lo medido** es la que se mira en un comité;
**declarado por debajo** es la que nadie revisa y suele significar que la definición se
escribió contra un dato viejo y el producto ya la pasó.

## Cómo se lee la diferencia

| Lo que se observa | Qué significa |
|---|---|
| Declarado muy por encima | La decisión se tomó con una expectativa que los datos no sostienen **hoy**. Puede ser una proyección legítima: mira si `declared` era meta o diagnóstico |
| Declarado por debajo | El documento envejeció. Nadie lo revisa porque la noticia es buena |
| No hay serie para esa afirmación | **El caso más común.** No es contradicción: es que nadie está midiendo lo que el negocio afirmó. Se declara así |
| La serie existe y se llama igual con otra definición | El hallazgo caro. Ver la regla 3 de arriba |
| Diferencia por debajo del umbral | Imprecisión, no contradicción. **No se reporta**: reportarla mata el informe |

## Lo que este skill no hace

- **No proyecta.** Una serie de dos meses no predice el año, y ajustar una tendencia sobre
  cuatro puntos es darle precisión a un dato que no la tiene.
- **No decide qué métrica importa.** Cuál es la métrica del producto es una decisión de
  producto, y sale de la definición y de la estrategia, no de los datos.
- **No entra a los sistemas.** La serie llega como documento o como exportación. Este
  agente no se conecta a la base de datos del producto, y si un día lo hiciera, tendría que
  decirlo aquí.
- **No corrige el número del negocio.** Deja los dos, con sus fuentes. Quién tiene razón es
  una conversación, y casi siempre la respuesta es *«los dos, en fechas distintas»*.
