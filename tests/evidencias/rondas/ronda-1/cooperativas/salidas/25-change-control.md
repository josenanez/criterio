# /criterio-portfolio:change-control PRY-211 mover la salida a producción 30 días

## Solicitud de cambio — PRY-211 Cobranza digital — 2026-10-14

Esto sale de la ficha `estado/records/PRY-211.json`. Los términos están aceptados: José Francisco Ñáñez, versión 1.0, 2026-10-14.

**La solicitud no se puede aprobar tal como está.** Mover la salida a producción 30 días da el 2026-07-17, que ya pasó hace 89 días (hoy es 2026-10-14). La línea base v1 (2025-10-28) fija la salida el 2026-06-17, así que el proyecto ya lleva 119 días de atraso. Sigue en ejecución, con 59 % declarado y estado Amarillo. Lo que hace falta es una fecha nueva posterior a hoy, y esa fecha la tiene que dar el gerente, Carlos Peña. Yo no la inventé.

| Dimensión | Hoy | Con el cambio |
|---|---|---|
| Alcance | Componentes 1, 2 y 3 (sin detalle en el acta) | Sin declarar |
| Tiempo | Salida 2026-06-17 (vencida) | 2026-07-17 (también vencida) |
| Costo | Aprobado COP 9.500.000.000; proyección 9.109.449.352 | Sin declarar |

- **Quién absorbe lo no declarado:** el pedido declara solo tiempo. Si alcance y costo quedan "sin cambio", alguien absorbe 30 días más de equipo y proveedor sin presupuesto.
- **Efecto en el portafolio:** el cálculo da 0 proyectos alcanzados. Eso viene de que la ficha no declara ninguna dependencia, no de que nadie dependa de PRY-211. El riesgo registrado "Dependencia del proveedor del core cooperativo" sugiere que sí hay dependencias sin anotar. El cálculo tampoco dice cuántos días se mueve cada afectado, porque la ficha no tiene holgura por actividad.
- **Quién decide:** no se puede determinar, porque el acta no declara autoridad de cambios. Va a comité por defecto (Comité de Crédito, próximo el 2026-10-21). Que el acta no diga quién aprueba cambios es el hallazgo de fondo.
- **Inconsistencia en los hitos:** la ficha marca los cinco hitos como cumplidos, incluida la salida a producción, y ninguno tiene evidencia. Esa marca sale del cronograma de 2025-10-28, no de un documento de cumplimiento. Con el proyecto al 59 %, no se sostiene.
- **Proveedor CT-509:** se facturaron COP 2.179.464.246 por tres entregables y solo uno tiene acta de recibo. La mesa de ayuda vencía el 2026-05-22 y sigue pendiente.
- **Si no se aprueba:** el proyecto sigue sin una fecha vigente contra la cual medirse.
- **Si se aprueba:** no se creó línea base nueva. La cifra que importa es que ningún documento autoriza hoy los 119 días ya corridos, porque `changes` está vacío.

**Para completar la solicitud falta:**
1. Quién la pide y por qué.
2. La fecha nueva real de salida.
3. El impacto declarado en alcance y costo.
4. Quién tiene autoridad de aprobar cambios.
5. Las dependencias de otros proyectos sobre PRY-211.

La corrida quedó registrada como `2026-10-14-change-control-1`, con el texto completo en `estado/corridas/salida-change-control.md`. Trabajé solo con la ficha, sin releer los documentos originales.