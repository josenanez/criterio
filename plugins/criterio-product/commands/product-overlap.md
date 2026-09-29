---
description: Dónde tu producto y otro se pisan — la misma métrica contada dos veces, el mismo proyecto construyendo para dos dueños, y el mismo segmento
argument-hint: "[código de otro producto] o vacío para cruzar contra todos"
---

# /product-overlap — La canibalización, y las dos cosas que la anteceden

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.


## Lo primero, antes de leer nada

```
python3 scripts/producto.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

*«Canibalización»* es una palabra grande para tres preguntas concretas, y **las tres se
responden con aritmética** sobre lo que cada producto publicó:

1. **¿Dos productos afirman la misma métrica?** Entonces los dos casos de negocio están
   contando las mismas transacciones, y **la suma que vio el comité no existe.** Es el
   hallazgo más caro de los tres, el que nadie busca, y casi siempre nadie lo hizo a
   propósito.
2. **¿El mismo proyecto ejecuta requerimientos de dos productos?** O uno de los dos
   registros está mirando mal, o el proyecto está construyendo para dos dueños y todavía
   no lo sabe.
3. **¿Dos productos dicen servir al mismo segmento?** No es un defecto por sí solo —una
   organización puede tener dos productos para el mismo cliente a propósito—, pero es una
   pregunta que alguien tiene que haber respondido, y normalmente nadie se la hizo.

## Invocación

```
/product-overlap                 contra todos los productos publicados
/product-overlap PRD-COBROS      contra uno
```

## Lo primero: si no hay nada publicado, no hay pregunta

```
python3 scripts/producto.py overlap --state <estado> --otros <carpeta> --config <archivo>
```

Si `totals.others` es cero, **dilo y termina ahí**: sin otro producto publicado,
canibalización no es una pregunta que se pueda responder, y fingir que se revisó es peor
que no revisarla. Ofrece `/product-publish` y explica que esto sirve cuando los demás
también publican.

## Flujo

**1. Las métricas compartidas van primero.** Con las dos cifras, las dos fuentes y las dos
fechas. Sin eso el hallazgo no sirve: *«los dos cuentan transacciones»* no le permite a
nadie hacer nada, y *«tu caso de negocio del 4 de marzo afirma 250.000 transacciones
mensuales y el de Cobros del 2 de mayo afirma 90.000, sobre la misma métrica»* sí.

**Y no concluyas que se suman mal.** Puede que sean el mismo universo contado dos veces, o
puede que las definiciones sean distintas con el mismo nombre — que es el caso más común y
el más feo. Aplica **product-metrics**: la pregunta que sigue es **qué mide exactamente
cada una**, y esa se responde leyendo, no calculando.

**2. Los proyectos compartidos, con el requerimiento de cada lado.** Di qué pone cada
producto en ese proyecto. Si tu requerimiento y el suyo son claramente lo mismo escrito
distinto, **dilo como lectura tuya y no como cálculo** — el código no lo sabe y no lo
pretende.

**3. El segmento, al final y sin dramatizarlo.** Dos productos para el mismo cliente puede
ser estrategia. La forma útil de reportarlo es como pregunta: *«los dos dicen servir a
comercios con recaudo QR sin punto de venta integrado — ¿está decidido que sean dos
productos?»*

**4. Compara los registros con la lista a la vista.** Esto es lo único de este comando que
no es aritmética, y por eso va después: con los requerimientos de los dos productos al
frente, di **cuáles parecen el mismo problema escrito de dos formas**. Aplica
**requirement-record**: lo mismo pedido con otro alcance no es lo mismo, y fusionarlo
pierde la diferencia.

Marca cada uno como **lectura**, no como hallazgo del cálculo. La diferencia importa: lo
que sale del código lo puede auditar cualquiera; lo que sale de una lectura hay que
discutirlo.

## Salida

```markdown
## Solapamiento — [producto] · al [fecha]
Cruzado contra [N] productos publicados: [códigos]

### La misma métrica, en dos casos de negocio
| Métrica | Tu cifra | La de [otro] | Tus fuentes y las suyas |
[Si hay alguna, va primero. Con la pregunta de qué mide cada una.]

### El mismo proyecto, dos dueños
| Proyecto | Tus requerimientos | Los suyos |

### El mismo segmento
| A quién dices servir | Quién más dice servirle |

### Lectura — requerimientos que parecen el mismo
| El tuyo | El suyo | Por qué lo parecen |
[Marcado como lectura. No sale del cálculo.]

### Qué no se cruzó
[Los productos que no han publicado. Si falta alguno que importa, esto es lo primero.]
```

**Si no hay ni un solo solapamiento, una línea:** *«cruzado contra [N] productos: ninguna
métrica compartida, ningún proyecto compartido, ningún segmento repetido»*. Y se acaba.

## Lo que este comando no hace

- **No decide si un producto canibaliza a otro.** Eso necesita conocer la estrategia, y la
  estrategia no está en ningún documento.
- **No recomienda matar ni fusionar nada.** Retirar un producto es autoridad.
- **No lee el registro completo de los demás.** Solo lo que publicaron, que es lo mínimo
  para cruzar.
- **No le escribe a nadie**, y no avisa al otro gerente de producto. Esa conversación es la
  que resuelve el punto, y es tuya.
- **No concluye que dos requerimientos son el mismo.** Lo propone como lectura, con las dos
  listas a la vista.

## Después

Si aparece una métrica compartida, **eso es material de comité de producto**, no una nota
al pie: ofrece formularlo como decisión —qué mide cada una, cuál se usa para decidir, y
qué pasa con las dos cifras que ya se presentaron—. Y si el solapamiento es de proyecto,
la salida es una conversación con ese gerente de proyecto, que casi siempre lo resuelve
antes de que llegue a ningún comité.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 scripts/producto.py corrida --state <estado> --what crossed \
    --salida <estado>/corridas/salida-crossed.md \
    --nota "qué productos se pisan"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` cuenta lo que hay que contar y deja `<estado>/corridas/<fecha>-crossed.md`: qué encontró por señal, cuánto tardó, y cuántos hallazgos más o menos que la vez anterior.
