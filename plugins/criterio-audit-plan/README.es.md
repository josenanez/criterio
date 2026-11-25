<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-cae-oscuro.svg"><img src="../../docs/img/marca/es/criterio-cae-claro.svg" alt="Criterio CAE · La auditoría interna" height="48"></picture>

# Prudencia · el plan de auditoría

<img src="../../docs/img/es/robot-prudencia.gif" alt="Prudencia" width="220" align="right">

**Prudencia pone el plan de auditoría al lado de los riesgos.**
Tú respondes por el plan de auditoría interna. Ella llega con el plan al lado de la matriz de riesgos y del universo auditable: el riesgo alto que ningún trabajo cubre, la unidad que pasó su ciclo, la evaluación de riesgos que ya tiene más de un año, el área que el plan no considera, el cambio que no tiene su acta, el trabajo atrasado, las horas que no alcanzan, el requisito temático que falta y la evaluación externa de calidad que se venció.

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**El nombre.** Prudencia, del latín *prudentia*, contracción de *providentia*, «ver antes»: el plan que mira el riesgo antes de que ocurra.
<!-- /agente:nombre -->

[English](README.md) · `criterio-audit-plan` · Apache 2.0 · Una instancia por entidad

**Estado: construido, en pruebas, con la familia CAE.** El motor de cálculo, probado contra todo el material sintético de la familia con una clave que el agente no ve y entidades de control. En la 0.2.0, el agente corrió sobre todas las entidades del material, con una clave que no ve; no se ha probado sobre la documentación de una organización concreta.

**Esta página se lee sola.** Prudencia funciona sin los otros agentes de la familia. La familia —cómo se encuentran entre sí y con Rostrum— está en la [familia criterio-cae](../../families/criterio-cae/README.es.md).

---

## Qué es

| | |
|---|---|
| **A quién extiende** | A quien dirige la auditoría interna —el CAE o el auditor general— y a quien arma y sigue el plan |
| **Sobre qué trabaja** | **El plan de auditoría de una entidad, periodo a periodo** |
| **Qué mira** | El universo auditable, la matriz de riesgos, el plan anual, las actas del comité y el equipo con sus horas |
| **Cadencia** | Cuando llega un acta o cambia el plan, y una vez por semana |
| **Instancias** | Una por entidad |

## Qué hace

**Lo que hace y hoy no se hace a mano: poner todo, no una muestra, al lado de su norma y de su evidencia.**

**Lo que puede responder:** qué riesgo alto no tiene un trabajo, qué unidad lleva más tiempo del que permite su ciclo sin auditarse, si el plan considera el gobierno de TI, el fraude y el cumplimiento, qué trabajo agregado o cancelado no tiene acta, qué trabajo va atrasado, si las horas alcanzan y cuándo toca la evaluación externa.

<!-- cae:comandos · generado por scripts/familias.py; no se edita a mano -->
### Los nueve comandos

> Se escriben con el prefijo del plugin: `/criterio-audit-plan:` y autocompletar hace el resto. Es la única forma que resuelve en una sesión de Claude Code.

| Comando | Qué hace |
|---|---|
| `/criterio-audit-plan:plan-setup` | La configuración, el inventario y las tablas reconocidas |
| `/criterio-audit-plan:prudencia` | Lo que necesites, en tus palabras: Prudencia elige el comando que lo resuelve y lo corre |
| `/criterio-audit-plan:plan-scan` | La ficha del periodo al día |
| `/criterio-audit-plan:plan-coverage` | Qué riesgo y qué unidad quedan sin cubrir, con su cita |
| `/criterio-audit-plan:plan-status` | El estado del plan para el comité |
| `/criterio-audit-plan:plan-capacity` | Si las horas alcanzan, con la cuenta |
| `/criterio-audit-plan:quality-status` | Cuándo toca la siguiente |
| `/criterio-audit-plan:plan-wake` | El plan al día sin que nadie se acuerde |
| `/criterio-audit-plan:share-findings` | Un resumen sin datos, solo si se dice que sí |
<!-- /cae:comandos -->

`plan-setup` va primero porque los demás lo necesitan, y `plan-wake` es el que se le pone a un reloj.

<!-- cae:skills · generado por scripts/familias.py; no se edita a mano -->
### Los tres skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten, y se consultan como un manual.

| Skill | Qué encapsula | De quién es |
|---|---|---|
| `audit-intake` | La estructura recomendada de la carpeta de auditoría, qué va en cada carpeta y qué agente la usa, cómo se nombran los trabajos y qué hacer con lo que no encaja | Propio · también en Justo y Remedios |
| `audit-methodology` | La metodología de auditoría en la configuración: los ciclos por nivel de riesgo, la escala de prioridad con su impacto y su probabilidad, quién aprueba el plan, el programa y los papeles, y cuántas reprogramaciones se permiten | Propio · también en Justo y Remedios |
| `plan-record` | Cómo se lleva a la ficha cada acta del comité: qué trabajo agrega, cancela o aplaza, quién lo aprobó y la cita | Propio |
<!-- /cae:skills -->

## Lo que cuesta hoy

<!-- cae:cifras · generado por scripts/familias.py; no se edita a mano -->
| Cifra | Fuente |
|---|---|
| **5 %** de sus ingresos pierden las organizaciones por fraude cada año, según la estimación de los examinadores de fraude | [ACFE, Occupational Fraud 2026: A Report to the Nations, 2026](https://acfe.com/RTTN) — 2.402 casos de 143 países y territorios, investigados entre enero de 2024 y septiembre de 2025 |
| **43 %** de los fraudes se detectan por una denuncia, casi tres veces más que por el método que le sigue | [ACFE, Occupational Fraud 2026: A Report to the Nations, 2026](https://acfe.com/RTTN) — 2.402 casos de 143 países y territorios, investigados entre enero de 2024 y septiembre de 2025 |
| **12 meses** dura, en la mediana, un fraude antes de que se detecte | [ACFE, Occupational Fraud 2026: A Report to the Nations, 2026](https://acfe.com/RTTN) — 2.402 casos de 143 países y territorios, investigados entre enero de 2024 y septiembre de 2025 |
<!-- /cae:cifras -->

## Para qué sirve

`/criterio-audit-plan:plan-coverage` pone cada caso al lado de su norma y de su evidencia. **Lo que falta se dice con su cita.**

### Y para qué no sirve

- **No aprueba el plan ni decide qué se audita.** Dice qué falta y dónde; la opinión es del auditor.
- **No entra a los sistemas auditados ni a la herramienta de auditoría.** Procesa lo que la organización le entrega.
- **No copia el texto de las Normas.** Las Normas Globales de Auditoría Interna se citan por su número y su título.

Y una que hay que decir en voz alta: **tus documentos se procesan en la infraestructura de la plataforma de IA**, no solo en tu equipo. Un papel de trabajo puede traer información confidencial: confirma que sea admisible bajo tu política antes de apuntarla a esa carpeta. Descargo completo en [DISCLAIMER.es.md](../../DISCLAIMER.es.md), términos en [TERMS.es.md](../../TERMS.es.md).

## Instalación y configuración

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-audit-plan@criterio
/criterio-audit-plan:plan-setup
```

### El primer resultado

`/criterio-audit-plan:plan-setup` no te pide que ordenes nada antes de empezar. Mira la carpeta de auditoría de la entidad, la compara con la [estructura recomendada](../../families/criterio-cae/README.es.md#la-estructura-de-carpetas-recomendada), procesa la metodología y hace las preguntas que ningún documento responde. En los primeros quince minutos deja ver el primer resultado.

### Cada cuánto corre

`/criterio-audit-plan:plan-wake` es el comando que el reloj invoca: hace lo que toca, responde primero las preguntas que alguien dejó en Rostrum, y **si no toca nada no produce nada.** La decisión de qué toca es aritmética de fechas, y la toma el código:

```
python3 scripts/auditoria.py despertar --config <archivo>
```

## Trabajo en equipo

| Con quién | Qué pasa |
|---|---|
| **Justo** | Comparten la carpeta y la metodología; cada uno escribe solo su ficha |
| **Remedios** | Comparten la carpeta y la metodología; cada uno escribe solo su ficha |
| **Rostrum** | Solo si la configuración lo dice (`publish_rostrum`; por omisión no, decisión 0014): publica sus reportes, lo que vence y sus señales para quien no abre una carpeta, y le devuelve las preguntas que deja quien lo mira. **No escribe en el estado** |

## Pruebas

[`scripts/auditoria.py`](scripts/auditoria.py), con la librería estándar, hace todo lo que es cálculo: procesa cada tabla con su fila de origen, cuenta los días contra los plazos de la metodología y de las Normas y cruza cada hallazgo con su evidencia, el mismo resultado cada vez. Vive en `criterio-audit-plan` y se copia a los otros dos agentes; `scripts/sincronizar.py --check` falla si la copia se separa.

```
python3 scripts/auditoria.py selftest
python3 tests/criterio-cae/generar.py
python3 tests/criterio-cae/evaluar.py
```

Qué se siembra en cada entidad y **qué no prueba el material**, en [`EVIDENCIA.md`](../../tests/criterio-cae/EVIDENCIA.md). El diseño, con la entrada, el proceso y el reporte de cada comando, en el [diseño de la familia](../../families/criterio-cae/DISENO.es.md).
