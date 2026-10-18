# /criterio-portfolio:budget-tracking PRY-205

## Presupuesto — PRY-205 Sistema de gestión de seguridad, al 2026-10-18

**Fuentes:** la ficha de PRY-205 y el cálculo de `portafolio.py compute`. Los documentos de origen son el acta de constitución (2025-07-11), el informe de avance (2026-10-15) y las solicitudes de cambio CC-01 y CC-02. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré de nuevo. No releí los documentos originales en esta corrida.

**Moneda:** COP. No hay contratos en otra moneda ni conversiones.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 4.200.000.000 | 100 | acta de constitución | 2025-07-11 |
| Comprometido | 2.648.414.321 | 63.1 | informe de avance | 2026-10-15 |
| Ejecutado | 1.211.699.567 | 28.8 | informe de avance | 2026-10-15 |
| Proyección al cierre | 5.095.962.103 | 21.3 por encima del aprobado | informe de avance | 2026-10-15 |

**Disponible real** (aprobado menos comprometido): 1.551.585.679 COP.

La proyección es una declaración del informe, no un dato medido. Es posterior a los cambios aprobados el 10-05 y el 10-12, así que no está vencida frente a ellos. El informe no dice si ya incluye su costo.

### Contra la línea base
- **Original:** 4.200.000.000 COP.
- **Vigente:** no declarado.
- **Desviación:** la proyección queda 21.3 % sobre el aprobado de 2025.
- **Replanificaciones de presupuesto:** ninguna registrada como línea base de costo. La ficha solo lleva líneas base de cronograma (v1 y v3). No hay v2, y la v3 no declara motivo.
- **Cambios aprobados con costo:** CC-01 suma 60.000.000 COP y CC-02 suma 232.000.000 COP. Ningún documento declara el aprobado vigente que resulta de ellos. Ambos dicen "el comité" sin indicar cuál.

### Ejecución frente a avance
Ejecutado 28.8 %, hitos cumplidos 3 de 3, avance declarado 34 %.

El dinero ejecutado y el avance declarado están cerca. La contradicción está en los hitos: el cronograma v3 marca los 3 como cumplidos, lo que sostendría 100 %. Eso son 66 puntos por encima del avance declarado, y ninguno tiene evidencia de recibo.

### Alertas
- **Proyección sobre el aprobado:** 21.3 %, con umbral de 10 %.
- **Retraso contra la línea base original:** 146 días (39.5 %). Contra la vigente es 0, porque CC-01 y CC-02 lo aprobaron (+30 y +116 días).
- **Hitos cumplidos sin evidencia:**
  - "Ingeniería básica aprobada" venció hace 331 días.
  - "Ingeniería de detalle aprobada" venció hace 208 días.
  - "Licencia y permisos obtenidos" figura como cumplido con fecha 2026-12-19, que aún no llega, y también sin evidencia. Esta tercera es una observación mía sobre la ficha: el script no la marcó.
- **Avance declarado frente al plan:** 34 % declarado contra 100 % que sostienen los hitos.
- **Comprometido:** 63.1 %, por debajo del umbral de 90 %. No hay alerta por este concepto.
- El informe declara estado rojo, pero no da cuenta de las señales de hitos sin evidencia, avance contra plan, costo y tiempo.

### Sin dato
- El presupuesto aprobado vigente tras CC-01 y CC-02.
- El motivo de la línea base v3 y la existencia de la v2.
- Si la proyección incluye el costo de los cambios aprobados.
- La evidencia de aceptación de los tres hitos.
- Producto, autoridad y fase. Los campos de identidad y el presupuesto aprobado tienen 15 meses, por encima del umbral de 12.
- Contratos de proveedores: no hay ninguno registrado, así que no hay detalle por proveedor.

### Después
Como la proyección excede el aprobado, se puede preparar la solicitud de cambio con `/criterio-portfolio:change-control`. No la preparé: en esta prueba nadie puede confirmarlo.

**Corrida registrada:** `2026-10-18-budget-tracking-1`, con la salida guardada en `estado/corridas/salida-budget-tracking.md`. Duró 29 segundos. El contador de la corrida cubre los 13 proyectos del portafolio porque `compute` los recalcula todos, aunque el informe es solo de PRY-205.

**Un error mío:** el archivo guardado incluye una frase con "292 millones". Es una suma mía de 60 y 232 millones, que el script no da, y la regla es copiar solo cifras del script. No la repito en lo anterior, pero quedó en el archivo registrado.