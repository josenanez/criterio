<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-cfo-oscuro.svg"><img src="../../docs/img/marca/es/criterio-cfo-claro.svg" alt="Criterio CFO · Cierre, control y reporte" height="48"></picture>

# Clara · la contralora

<img src="../../docs/img/es/robot-clara.gif" alt="Clara" width="220" align="right">

**Clara pone los libros al lado de sus soportes.** El cierre mensual con su checklist y su evidencia, las conciliaciones bancarias y de cuentas, cada factura electrónica de la DIAN o del SRI contra su registro, y el paquete para el auditor. Procesa todos los documentos del periodo, no una muestra, y dice qué cuadra, qué no y qué no tiene soporte.

[English](README.md) · `criterio-finance` · Apache 2.0 · Una instancia por entidad

**Estado: construida y en prueba.** Los nueve comandos, los siete skills y el motor de cálculo están construidos; el motor pasa su prueba determinista contra material sintético de cuatro industrias, con una clave que el agente no ve y una entidad de control. La prueba con el agente de extremo a extremo es el paso siguiente. La familia, con Tomás, en [`families/criterio-cfo/DISENO.es.md`](../../families/criterio-cfo/DISENO.es.md).

---

## Cómo trabaja

| | |
|---|---|
| **El modelo de lenguaje (LLM) extrae** | Lo que solo trae un documento escrito: el estado que alguien declara, un requerimiento que llegó por correo |
| **El código calcula** | Cuadres, conciliaciones, cruces de facturas, el avance del checklist: `scripts/finanzas.py`, librería estándar, el mismo resultado cada vez |
| **Una persona declara** | Clara no registra asientos, no firma y no declara el estado del cierre. Lo que es criterio contable o fiscal queda como pregunta |

Primera versión: NIIF adoptadas localmente en Colombia y Ecuador, con la factura electrónica de la DIAN y del SRI procesada desde su fuente técnica oficial.

## Los comandos

<!-- cfo:comandos · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Qué entrega |
|---|---|---|
| 0 | `/criterio-finance:finance-setup` | La configuración, el inventario de la carpeta y la primera ficha del cierre |
| 1 | `/criterio-finance:close-scan` | La ficha del cierre al día, con lo que cambió y las señales nuevas |
| 2 | `/criterio-finance:close-status` | El estado del cierre: declarado contra evidenciado, tarea por tarea |
| 3 | `/criterio-finance:bank-reconcile` | La conciliación de cada cuenta bancaria, con sus partidas abiertas por antigüedad |
| 4 | `/criterio-finance:account-reconcile` | La conciliación de cada cuenta contra su auxiliar |
| 5 | `/criterio-finance:ledger-check` | El cuadre del balance y del mayor, cuenta por cuenta |
| 6 | `/criterio-finance:einvoice-check` | Todas las facturas electrónicas del periodo contra la contabilidad, no una muestra |
| 7 | `/criterio-finance:audit-pack` | El índice del paquete del auditor, con el estado de cada requerimiento |
| 8 | `/criterio-finance:finance-wake` | Lo que toca hoy en el cierre; si no toca nada, se calla |
<!-- /cfo:comandos -->

## Los skills

<!-- cfo:skills · generado por scripts/familias.py; no se edita a mano -->
`audit-support` · `close-checklist` · `close-record` · `einvoice-matching` · `finance-intake` · `ledger-tieout` · `reconciliation`
<!-- /cfo:skills -->

## Lo que cuesta hoy

<!-- cfo:cifras · generado por scripts/familias.py; no se edita a mano -->
| Cifra | Fuente |
|---|---|
| **44 %** cerraba el trimestre en seis días hábiles en 2023, contra 49 % en 2019 | [Ventana Research / ISG, Smart Financial Close, 2023](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) — No indicada en la nota |
| **45 %** de los controles SOX son manuales en las organizaciones encuestadas; las horas del programa subieron 32 % en dos años, de 11.800 a 15.580 | [KPMG, SOX Survey, 2025](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) — Cerca de 150 profesionales SOX |
| **18 días** es la mediana del cierre anual; los mejores lo hacen en 10 días o menos y los más lentos en 35 | [APQC, blog del 8 de abril de 2026, y su medida de Open Standards Benchmarking del cierre anual a nivel de sitio, 2026](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-year-end-close) — La nota no la indica; la medida de benchmarking reporta la mediana de 18,0 días con 2.214 organizaciones |
| **18 %** de las personas de la función de contraloría comete errores al menos a diario, y 59 % varios al mes, por restricciones de capacidad | [Gartner, comunicado del 21 de febrero de 2024, 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) — 497 personas de la función de contraloría, encuesta de julio de 2023 |
<!-- /cfo:cifras -->

El dato que debería incomodar es el primero: **el cierre no mejoró en cuatro años**, a pesar de todo lo que se gastó en tecnología.

## El primer resultado

En los primeros quince minutos, `finance-setup` deja ver el estado del cierre del periodo: cada tarea del checklist con su evidencia o sin ella, y las señales que el motor levantó en el cuadre, los bancos, las cuentas y las facturas. Desde ahí, cada comando entrega su reporte en el mismo orden: lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hizo y las fuentes.

## Lo que nunca hace

- No registra ni corrige asientos.
- No presenta declaraciones ni reportes a supervisores, y no firma.
- No opina sobre deducibilidad, tarifas ni tratamientos NIIF, y no dice de memoria una tarifa, un plazo ni el valor de una unidad tributaria.
- No declara el estado del cierre: lo declara el contralor.
- No mueve, renombra ni crea nada dentro de los documentos de la organización. Lo único que deja, si la persona lo autoriza, es el archivo que marca la carpeta raíz para que se reconozca a primera vista.

## Instalación y configuración

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-finance@criterio
/criterio-finance:finance-setup
```

**En Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar marketplace desde GitHub → `josenanez/criterio`.

`finance-setup` mira la carpeta, hace las preguntas que ningún documento responde —la entidad, el marco, las cuentas que cruzan las facturas, el checklist— y muestra el primer estado del cierre. La estructura de carpetas recomendada está en el skill `finance-intake`; Clara la sugiere y no mueve nada.

**Para quien no abre una carpeta**, lo que Clara escribe —sus reportes, lo que vence, sus señales— lo publica Rostrum, el portal de todas las familias: [`criterio-server`](../criterio-server/README.es.md). Ahí también se le pueden dejar preguntas escritas, que toma en su `*-wake`.

## Las fuentes

Cada formato y cada norma que se usa está en [`families/criterio-cfo/FUENTES.es.md`](../../families/criterio-cfo/FUENTES.es.md), con su versión, su enlace y su estado; cada campo de factura que procesa el motor, con su identificador en el anexo técnico.

## Cómo se verifica

```
python3 scripts/finanzas.py selftest
python3 tests/criterio-cfo/generar.py
python3 tests/criterio-cfo/evaluar.py
```

Con la librería estándar, sin instalar nada. **Cómo salió la última corrida**, generado desde la corrida misma: [`tests/criterio-finance/RESULTADOS.md`](../../tests/criterio-finance/RESULTADOS.md). Criterios de aceptación en [ACCEPTANCE.md](ACCEPTANCE.md).
