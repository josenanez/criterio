# /criterio-portfolio:change-control PRY-201 mover la salida a producción 30 días

## Solicitud de cambio — PRY-201 Programa de fidelización — 2026-10-17

Parto de la ficha `estado/records/PRY-201.json`. Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no registré nada nuevo.

**Qué se pide:** mover 30 días la salida a producción. Tomé como esa salida el hito «Despliegue en la cadena» (2027-04-27), porque es el último y coincide con el criterio de éxito del acta. Si te referías a otro hito, el cálculo cambia.
**Quién lo pide y por qué:** la solicitud no lo dice. No lo inventé.

### Impacto
| Dimensión | Hoy | Con el cambio | Diferencia |
|---|---|---|---|
| Alcance | 3 componentes sin nombre en el acta | No declarado | Sin impacto declarado |
| Tiempo | Despliegue 2027-04-27 | 2027-05-27 | +30 días contra la línea base vigente y **+63 contra la original** (2027-03-25) |
| Costo | Aprobado 1.200.000.000 COP; proyección 1.176.832.977 | No declarado | Sin impacto declarado |

Con alcance y costo sin impacto declarado, alguien absorbe los 30 días en horas no pagadas o en calidad, y la solicitud no dice quién. No calculé el costo de esos días: la ficha no trae costo por periodo.

### Efecto en el portafolio
- **Resultado:** el cálculo no alcanza a ningún proyecto (0 directos, 0 indirectos). Eso significa que no hay dependencias declaradas, no que no existan: el acta dice «Ninguna declarada».
- **Pregunta para el gerente (Rubén Cárdenas):** PRY-201 tiene un hito «Integración con el ERP» y el portafolio tiene PRY-209 (Migración del ERP). Ningún documento los relaciona; es solo algo que conviene confirmar.
- **Lo que no se sabe:** cuántos días se movería cada proyecto afectado, porque eso necesita holgura por actividad y la ficha no la tiene.

### Quién decide
- **Autoridad:** no se puede determinar, porque el acta no declara ninguna. Ese es el hallazgo de fondo.
- **Va a comité:** sí, al Comité Comercial, que aprobó el presupuesto. El próximo es el 2026-10-22.

### Lo que ya muestra el control de cambios del proyecto
- **CC-01** (+33 días, +66.000.000 COP) figura como «autorizada por el comité», sin nombre ni fecha de sesión. El acta del comité del 2026-10-14 no la menciona.
- **Línea base v2** (cierre 2027-04-27) no trae motivo y es cinco días anterior a CC-01. Los 33 días cuadran con CC-01, pero CC-01 no dejó su propia línea base.
- **El estado «verde» no se sostiene** (informe del 2026-10-09):
  - El avance declarado es 36% y el plan sustenta entre 60% y 80%.
  - Un hito figura cumplido sin evidencia de recibo.
  - La prueba de carga de temporada falló y se repite.
  - El proveedor no ha confirmado la fecha de la última entrega.
  - No hay contrato de proveedor en la carpeta.

### Si no se aprueba
El cierre sigue en 2027-04-27 (+33 días contra la original). La prueba de carga y el proveedor sin fecha son los dos motivos documentados de riesgo, pero ninguno está medido contra el cronograma, así que no afirmo que la fecha no se sostenga.

### Si se aprueba
Línea base 3 con cierre 2027-05-27, presupuesto y motivo sin declarar. La desviación acumulada contra la original sería **+63 días** y +66.000.000 COP de CC-01 más lo que esta solicitud no cuantificó. Las replanificaciones pasarían de 1 a 2.

### Antes de llevarlo a comité
1. Motivo y solicitante de los 30 días.
2. Qué hito es «salida a producción» y si el piloto (2026-12-08) también se mueve.
3. Impacto en alcance y costo, o quién absorbe cada uno.
4. Nombre y fecha de la sesión que autorizó CC-01, y la autoridad del Comité Comercial por escrito.
5. Revisar el estado «verde» antes de que el comité lo use como punto de partida.

Es un borrador de trabajo. Si quieres, lo llevo a comité; la línea base nueva no la registro porque nadie con autoridad documentada la ha aprobado.

**Corrida registrada:** `2026-10-17-change-control-1` (44 s, caso PRY-201). La salida completa está en `estado/corridas/salida-change-control.md`.