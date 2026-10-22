# /criterio-finance:einvoice-check 

Los términos (versión 1.2) ya estaban aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-06. El cruce del periodo 2026-09 no deja nada abierto.

# Facturas electrónicas · Distribuidora Control · periodo 2026-09

**Entidad:** Distribuidora Control (900000001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.7.0 · **Aprueba:** Sofía León · **Comando:** `einvoice-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

17 facturas y notas electrónicas procesadas · 17 cruzadas con su registro · 0 identificadas solo por la clave de acceso · 1 líneas de ventas o compras sin número de documento.

Sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su NIT, país y moneda? → Distribuidora Control, NIT 900000001, Colombia, COP (sesión sin interfaz: tomado de la carpeta y las facturas)
- ¿Qué marco o grupo NIIF aplica? → No encontrado en los documentos; queda 'por confirmar'
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 41; compras 14, 51, 52, 61; IVA generado y descontable 2408
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (traen auxiliar); bancos andino-5301 y pacifico-5302
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv, sin aprobar
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivo 2026-10-12
- ¿Dónde se guarda el estado? → estado-finanzas/900000001-distribuidora-control
- ¿Se deja la marca _CRITERIO_FINANZAS.txt en la carpeta? → No: sin interfaz no hay un sí para escribir dentro de los documentos

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cfo/FUENTES.es.md)

---

La salida quedó en `estado-finanzas/900000001-distribuidora-control/corridas/salida-einvoice-check.md`. La corrida quedó registrada con el id `2026-10-06-einvoice-check-1` y 0 hallazgos.

El reporte cuenta una línea de ventas o compras sin número de documento y no dice cuál es. Eso no sale como asunto abierto, pero conviene mirarla en el auxiliar.