# /criterio-portfolio:health-check PRY-204

## Diagnóstico · PRY-204 Tarjeta débito para asociados · 2026-10-23

**Leí** 7 documentos, del 2026-05-28 al 2026-10-23: .docx (2), .md (2), .pdf (2), .xml (1). Pude leerlos todos. Ninguna minuta de los otros 12 proyectos nombra a PRY-204.

Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no los registré de nuevo. Las cifras derivadas salen de `portafolio.py compute`. Ese cálculo parte de la ficha del barrido de hoy, y cada dato lo contrasté con el documento original.

### Dictamen
**Sostenido:** 4 · **Sin sustento:** 8 · **Contradicho:** 3 (15 afirmaciones; el conteo es mío).

La carpeta sostiene quién es el patrocinador y quién el gerente, el presupuesto aprobado, las fechas comprometidas y que la integración con el core se recibió el 2026-10-15. No sostiene el "Verde" del informe del 2026-10-07. Ninguna cifra de dinero tiene más respaldo que ese mismo informe, y ningún documento dice quién autoriza desviaciones.

### Gobierno
- **Patrocinador:** Diana Molina (acta).
- **Gerente:** Sandra Gil (acta).
- **Autoridad del gerente:** no está declarada. Sin ella, no hay desviación aprobada.
- **Comité:** Comité de Crédito, sin integrantes ni reglas de decisión.

### Contra el plan
- Hay una sola línea base (v1, aprobada el 2026-06-06), con cierre el 2026-12-21. No hay replanificaciones ni solicitudes de cambio.
- El cronograma v1 está fechado en junio, pero trae avances de hitos de julio a octubre. Alguien lo editó sin versión nueva. Esos porcentajes son declaración, no evidencia.
- **Avance:** el informe declara 37 %; con 3 de 5 hitos marcados cumplidos, el plan respalda entre 60 % y 80 %, una diferencia de 23 puntos.

### Hitos vencidos sin evidencia
| Hito | Fecha | Días |
|---|---|---|
| Diseño funcional aprobado | 2026-07-23 | 92 |
| Ambiente de pruebas certificado | 2026-08-30 | 54 |

Ambos figuran como cumplidos en el cronograma y no hay un solo documento que lo pruebe.

### Dinero
| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 9.500.000.000 | 7.487.113.499 (78,8 %) | 5.254.568.526 (55,3 %) | 9.790.767.231 (3,1 % sobre lo aprobado) | 2.012.886.501 |

- **Origen de las cifras:** todas, salvo el aprobado, salen del informe. No hay soporte contable.
- **Contrato CT-222 (Soluciones Solidarias):** 2 entregables, 0 aceptados. El licenciamiento del módulo, comprometido para el 2026-08-24, sigue pendiente (60 días).
- **Factura FV-1222:** por 1.064.377.272 COP, del 2026-09-10. El contrato exige un acta de recibo firmada para facturar, y la carpeta no tiene ninguna de un entregable del contrato.

### Lo que se dijo y nadie registró
- **Dependencias:** el acta dice "ninguna declarada". El informe nombra la dependencia del proveedor del core y un ajuste de reglamento que pidió el Consejo antes del piloto. Ninguna tiene dueño ni fecha.
- **Compromisos vencidos (minuta del 2026-10-23):**
  - Jorge Medina, "punto 20", para el 2026-10-14: 9 días.
  - Elena Duarte, "punto 11", para el 2026-10-18: 5 días.
  - No se sabe qué son esos puntos.
- **Atraso del proveedor:** no está como riesgo ni incidencia en ningún documento.

### Contradicho
1. **"Verde":** el informe lo declara, pero el contrato muestra licenciamiento atrasado y la factura no tiene acta de recibo. Además hay 2 hitos cumplidos sin evidencia.
2. **"Dependencias: ninguna":** el acta lo dice y el informe lo desmiente.
3. **Avance de 37 %:** el cronograma muestra 3 de 5 hitos al 100 %.

### Sin sustento
Los 8 puntos son:
1. Diseño funcional cumplido.
2. Ambiente de pruebas cumplido.
3. Avance de 37 %.
4. Comprometido.
5. Ejecutado.
6. Proyección al cierre.
7. El ajuste del plan de pruebas con seguridad.
8. El pedido del Consejo sobre el reglamento.

### Lo que esta carpeta no permite saber
- **Quién autoriza qué:** sin eso no se puede evaluar la proyección sobre lo aprobado ni un cambio de fechas.
- **Si la factura FV-1222 procede:** falta el acta de recibo del entregable contractual. Tampoco sé si ya se pagó.
- **Si el piloto del 2026-11-13 es viable:** falta lo del Consejo y el plan de pruebas.
- **Cuánto se gastó de verdad:** no hay soporte contable.
- **Qué pasó desde el 2026-10-07:** no hay informe más reciente.

No recomiendo detener, continuar ni reestructurar; eso lo decide quien tiene la facultad. Puedo preparar el punto de comité con la lista de lo que falta, o llevarle las 3 contradicciones a Sandra Gil como preguntas, una por una.

La corrida quedó registrada como `2026-10-23-health-check-1`, con el texto completo en `estado/corridas/salida-health-check.md`.