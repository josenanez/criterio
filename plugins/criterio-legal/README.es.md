# criterio-legal

Revisión de contratos y cumplimiento con criterio de derecho civil suramericano.

[English](README.md) · Apache 2.0

**Estado: capacidad declarada, sin construir.** No hay contenido, y en este repositorio no
existe ningún paquete por jurisdicción. Aquí no se construye nada hasta que el alcance se
amplíe deliberadamente — ver [ADR 0005](../../docs/decisions/0005-scope-pmo-only.md).

Lo que está construido hoy es la familia PMO: **Vera** para la oficina de proyectos,
**Samuel** para un proyecto y **Alba** para un producto. La familia entera, con sus comandos
y su estado, en el [README del marketplace](../../README.es.md).

## El problema que va a atacar

**Qué es.** La función que responde por lo que la empresa firmó. Sus componentes son la revisión de contratos, el repositorio de lo firmado, el seguimiento de obligaciones y vencimientos, el cumplimiento normativo y las disputas.

**Lo que cuesta hoy**

| Cifra | Fuente |
|---|---|
| La mala gestión contractual erosiona en promedio **8,6% del valor del contrato** — los mejores 3%, los peores más de 20% | [World Commerce & Contracting con Deloitte, 2023](https://info.worldcc.com/roi) — 1.236 organizaciones |
| Los equipos de contratación gastan **más del 40% de su tiempo y su presupuesto** en contratos de baja complejidad | [EY con Harvard Law School, 2021](https://clp.law.harvard.edu/wp-content/uploads/2022/10/ey-contracting-report-june-2021.pdf) — 1.000 profesionales, 22 países |
| Una organización grande maneja **19.000 contratos al año**, y **90% tiene dificultad para encontrar los suyos** | EY / Harvard Law School, 2021 |
| Solo el **27%** guarda todos sus contratos firmados en un único repositorio | [Sirion y World Commerce & Contracting, 2026](https://www.sirion.ai/press/trusted-contract-data-world-cc-research-report/) — 170 empresas |

Una empresa que no encuentra sus propios contratos no puede saber qué firmó, ni qué vence, ni a qué se obligó.

→ Agente CLO: capacidad declarada, sin construir

---

La lista no está cerrada. **Una capacidad entra cuando alguien que la ejerce quiere construir su agente.**

---

Cuando esta capacidad se construya, seguirá las mismas reglas que las otras tres: cada dato
con la cita del documento del que salió, declarado y evidenciado sin fusionar, y el agente
callado mientras no haya novedad.
