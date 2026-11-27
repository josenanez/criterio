# /criterio-campaigns:campaigns-setup mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos

Soy Próspero. Pongo cada campaña al lado de su presupuesto, su factura y su resultado en la plataforma; no apruebo presupuestos ni juzgo campañas.

- **Carpeta:** solo encontré una, y ya está marcada con `_CRITERIO_MERCADEO.txt`: Almacenes Control de Mercadeo Sintéticos, NIT 901444666. Uso esa.
- **Entidad, país y estado:** tomo los mismos que dejó el setup de Lucía: NIT 901444666, CO, COP y el estado en `estado-mercadeo/901444666-almacenes-control-de-mercadeo-sinteticos`.
- **Periodo:** 2026-10, que es el corte del informe de resultados.
- **Tolerancias:** la política de publicidad fija un 5 % sobre el presupuesto y un 2 % frente a la plataforma.
- **Rostrum:** sí, porque la política no dice lo contrario.
- **Marca:** la carpeta ya la tiene, así que no la pongo otra vez.

Términos (versión 1.6, del 2026-11-16), tal cual:

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Los acepta José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-campaigns-0.2.0-2026-11-25.md` y en el `.pdf` del mismo nombre.

Procesé el informe de resultados y llevé a la ficha del periodo sus tres resultados (C-01, C-03 y C-04), con el corte que declara el informe. Este es el primer reporte; lo escribe el motor y lo dejo tal cual:

# Cada campaña contra su presupuesto · Almacenes Control de Mercadeo Sintéticos · periodo 2026-10

**Entidad:** Almacenes Control de Mercadeo Sintéticos (901444666) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.2.0 · **Comando:** `budget-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 104,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | 1200 recompras | Recompras |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 7,000,000 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |

Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

---

**Reloj:** no creé la tarea programada, porque pide un sí explícito y en esta sesión sin interfaz nadie puede darlo. Para correrlo a mano: `/criterio-campaigns:campaigns-wake`.

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.