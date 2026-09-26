# Cómo aportar

[English](CONTRIBUTING.md)

## Antes de empezar

Lea [TERMS.es.md](TERMS.es.md). Los aportes se licencian bajo Apache 2.0 por el solo hecho de enviarlos, y al aportar usted declara que el contenido es suyo y no contiene material confidencial ni de clientes.

Abra primero un issue describiendo qué quiere cambiar, para que dos personas no escriban lo mismo.

## La forma del trabajo

Un plugin es markdown. No hay código ejecutable en un skill ni en un comando —solo instrucciones—, así que un aporte es un cambio de texto que tiene que sobrevivir a ser leído literalmente por un modelo.

- **Los skills son sustantivos.** Conocimiento y marcos que el modelo carga solo cuando el tema aparece. La `description` es lo que dispara la carga: escríbala con las palabras que un usuario realmente teclea.
- **Los comandos son verbos.** Flujos que el usuario invoca. Encadenan skills.
- **Un comando solo puede referenciar skills de su propio plugin.** Los plugins se instalan por separado; una referencia cruzada se rompe.
- El `name` de un skill debe coincidir con el nombre de su directorio.
- Mantenga el frontmatter corto — siempre está cargado. El detalle va en el cuerpo, que solo se carga cuando el skill se dispara.

## Qué es un buen aporte

La prueba es simple: **¿qué diría distinto la salida por culpa de este cambio?** Si la respuesta es nada, es lectura de contexto, no un aporte.

Tres formas que no funcionan:

- *"La gestión de portafolio consiste en entregar valor."* Cierto, no cambia nada.
- *"Considere consultar a un especialista."* Consejo al lector, no instrucción para el análisis.
- Tres párrafos de un marco transcritos de un libro. Nómbrelo y diga cuándo aplicarlo.

Y la que sí funciona: una señal concreta que buscar en el material, qué significa, y qué debe afirmar el análisis entonces.

## Las reglas que no se negocian

**La aritmética va en código.** Si una instrucción le pide al modelo calcular días, porcentajes, proyecciones o saldos, está en el lugar equivocado. El modelo extrae; el script calcula.

**Toda afirmación lleva su cita.** Una salida que afirma algo que ningún documento sustenta es justamente la falla que este proyecto existe para evitar. "No está dicho en ninguna parte" es un hallazgo válido.

**Nada de datos inventados.** Ni un nombre, ni una fecha, ni una cifra, ni un doliente. Donde el material calla, la salida lo dice.

**Nunca escriba una cifra que cambia.** Los umbrales y las tasas van en configuración, no en prosa.

## Antes del pull request

- [ ] **`python3 scripts/verificar.py` pasa sin errores.** Es una sola puerta y corre todo: el material sintético, la aritmética de los dos plugins, las respuestas escritas a mano, y que la documentación diga lo que el código hace.
- [ ] El nombre del skill coincide con su directorio; el comando tiene `description` y `argument-hint`.
- [ ] El README del plugin lista lo que agregó — el validador lo revisa.
- [ ] Hay material de prueba en `tests/` que cubre el comportamiento nuevo, y el evaluador lo detecta cuando se rompe.
- [ ] Ningún dato real de ninguna empresa, cliente ni persona. El material de prueba es sintético y construido desde cero. No anonimice un documento real: la anonimización falla.
