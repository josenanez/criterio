# /criterio-portfolio:budget-tracking PRY-203

El presupuesto de PRY-203 (Despacho automático de flota) proyecta cerrar 20.8% por encima del aprobado, y el informe lo declara en rojo.

Los términos ya estaban vigentes (v1.1, José Francisco Ñáñez, 2026-10-16), así que no los volví a registrar. Las cifras salen del informe de avance del 2026-10-13 y del cálculo del script.

| | COP | % del aprobado |
|---|---|---|
| Aprobado | 800.000.000 | — |
| Comprometido | 339.448.354 | 42.4% |
| Ejecutado | 389.245.930 | 48.7% |
| Proyección al cierre | 966.342.753 | 20.8% por encima del aprobado |

- **Comprometido y ejecutado no cuadran:** el informe declara menos comprometido que ejecutado. El disponible real que da el script (460.551.646) por eso no es confiable. Hay que pedirle a la gerente el comprometido correcto.
- **Sin línea base de costo:** ningún documento tiene un presupuesto original ni vigente, así que la desviación de costo contra línea base va como `not_found`.
- **Cambio sin decidir:** el cambio CC-01 pide 132.000.000 COP más y 66 días más. Sigue pendiente de presentarse al comité. El fin del proyecto ya se movió 66 días (de 2027-01-08 a 2027-03-15) sin que nadie lo autorizara.
- **Avance declarado:** el informe dice 82%, pero los hitos sustentan entre 50% y 75%, y la ejecución va en 48.7%. Además, el hito "Ingeniería básica aprobada" figura cumplido sin evidencia.
- **Proveedores:** no hay ninguno registrado, así que no hay detalle por proveedor que ofrecer.
- **Siguiente paso:** puedo preparar la solicitud de cambio de presupuesto, porque la proyección excede el aprobado.

La corrida quedó registrada como `2026-10-16-budget-tracking-1`.

Archivos en `/home/claude/banco/ronda-5/mineria/espacio/estado/corridas/`:
- `salida-budget-tracking.md`