# /criterio-project:pm-plan 

# Plan — Billetera y QR (PRY-206) · borrador del 2026-10-15

**Desde:** el acta de constitución del 2025-06-02. **Criterio de éxito:** «Billetera y QR en producción y medido».

Los términos ya estaban vigentes (versión 1.1, aceptada el 2026-10-15 por José Francisco Ñáñez), así que no los registré otra vez.

**El proyecto ya está en marcha.** El acta tiene 16 meses y existe un cronograma v1 con cinco hitos, todos en «cerrado». El acta de recibo del 2026-10-04 da por recibida la «Salida a producción». Por eso la WBS es una reconstrucción desde los documentos y no un plan desde cero. No hay línea base nueva ni fechas comprometidas.

## Lo que le falta al acta
- **Alcance vacío.** Dice «Componente 1, 2, 3». No hay entregables de donde partir, así que la WBS sale de los contratos y del cronograma, y va marcada así.
- **Fuera de alcance genérico.** Dice «Lo que otro proyecto cubre», sin decir cuál.
- **«Medido» sin métrica.** No dice qué se mide, con qué umbral ni quién lo acepta. Es el entregable que nadie va a poder cerrar.
- **Autoridad del gerente no declarada.** Ni el acta ni la configuración la dicen.
- **Objetivo tautológico.** Dice «Entregar billetera y qr para Banca Hipotecaria», sin beneficio esperado.
- **Dependencias «ninguna declarada».** Hay dos proveedores contratados y una «siguiente fase» mencionada en la reunión.

No relleno nada de esto.

## WBS (resumen)
| Nodos | De dónde salen | Quién acepta |
|---|---|---|
| 1–4: Diseño funcional, Ambiente de pruebas, Integración con el core, Piloto interno | Cronograma v1 | Sin definir |
| 5: Salida a producción | Cronograma v1 y acta de recibo | Camilo Beltrán |
| 6–8: Licenciamiento del motor, Bolsa de horas, Parametrización del tarifario | Contratos CT-279 y CT-725 | El gerente, por la condición de pago |
| 9: Medición en producción | Criterio de éxito, sin métrica | Sin definir |
| 10: Componentes 1–3 | Acta, sin contenido | Sin definir; no se descompone |
| 11: «Siguiente fase» | Una mención en las notas del 2026-10-15 | Sin definir; no se descompone |

Ninguna duración está llenada, porque ningún documento la da.

## Orden
Sin fechas:
- Los hitos 1 → 2 → 3 → 4 → 5 van en cadena.
- La medición (9) necesita la salida a producción (5).
- La relación de los entregables contractuales (6–8) con los hitos es un supuesto: no está escrita en ningún documento.

## Supuestos
- Los cinco hitos del cronograma v1 son la estructura de entregables del proyecto.
- CT-279 y CT-725 cubren de verdad los mismos tres entregables con dos proveedores.
- «En producción» del acta equivale a la «Salida a producción» recibida el 2026-10-04.
- La «siguiente fase» es parte de este proyecto.
- El cierre comprometido del 2026-11-11 sigue vigente.

## Proyectos análogos
Ninguno a la vista, porque la configuración no apunta a una carpeta de fichas de la PMO. No estimo por analogía.

## Contradicciones que el plan hereda
- **CT-279:** «Parametrización del tarifario» sigue *pendiente*, con fecha 2026-07-04 vencida.
- **CT-725:** el mismo entregable figura *recibido*, y «Bolsa de horas» figura *en curso* con fecha 2026-02-25 vencida.
- **Facturas:** hay una de cada contrato del 2026-09-10. No las contrasté aquí.
- **Cronograma v1:** la fecha vigente es igual a la línea base en los cinco hitos. «Salida a producción» figura para el 2026-09-25 y el acta de recibo es del 2026-10-04, 9 días después.
- **Acta de recibo de «Salida a producción»:** tiene una sola línea, sin evidencia de qué se recibió.

## Preguntas para el equipo
1. ¿Cuánto toma cada uno de los hitos 1 a 5 en esta fase?
2. ¿Qué se mide, con qué umbral y cuándo se declara «medido»?
3. ¿Qué son los Componentes 1, 2 y 3?
4. ¿Qué es la «siguiente fase», quién la financia y cuándo empieza?
5. ¿CT-725 duplica a CT-279, o son entregables distintos con el mismo nombre?
6. ¿Quién acepta cada hito?
7. ¿Está confirmado el equipo completo del proveedor para la siguiente fase? Es el riesgo mencionado el 2026-10-15 que nadie registró.

## Para comprometer una fecha falta
- La disponibilidad real del equipo y de los proveedores.
- La fecha del proveedor para la siguiente fase.
- La ventana de despliegue y de medición en producción.
- La definición de «medido».

Ninguna de las cuatro está en un documento.

La corrida quedó registrada como `2026-10-15-pm-plan-1`, con la salida completa en `estado/PRY-206-billetera-y-qr/corridas/salida-pm-plan.md`. El registro de la corrida cuenta además un compromiso abierto sin fecha (Laura Vélez, «la otra semana»), que viene de las notas y no del plan.