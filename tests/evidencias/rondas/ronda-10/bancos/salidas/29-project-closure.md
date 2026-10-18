# /criterio-portfolio:project-closure PRY-202

El cierre de PRY-202 está hecho y la corrida quedó registrada como `2026-10-18-project-closure-1`. El proyecto no se puede cerrar por cumplimiento, y no archivé la carpeta.

Salió de la ficha `estado/records/PRY-202.json` y de los seis documentos del proyecto. Las cifras vienen de `portafolio.py compute` con corte 2026-10-18. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no hizo falta registrarlos otra vez.

## Cierre — PRY-202 Migración a la nube — 2026-10-18

Nadie ha declarado el cierre en los documentos, y lo que hay no sostiene que el proyecto esté terminado. El informe del 2026-10-11 lo reporta en amarillo con 51 % de avance, cuando el cronograma ya vencía por completo el 2026-09-25. Este es un cierre preliminar, no un acta firmable.

### Contra lo comprometido
- **Criterio de éxito:** "Migración a la nube en producción y medido" (acta, 2025-12-06). No dice qué se mide, con qué umbral ni quién.
- **Se cumplió:** no se puede determinar. Ningún documento muestra la migración en producción ni una medición.

| Entregable comprometido | Estado | Evidencia |
|---|---|---|
| Alcance: Componentes 1, 2 y 3 | El acta no dice qué es cada uno | Ninguna |
| Diseño funcional aprobado (2026-02-10) | Declarado cumplido | Sin evidencia (250 días) |
| Ambiente de pruebas certificado (2026-04-08) | Declarado cumplido | Sin evidencia (193 días) |
| Integración con el core (2026-06-04) | Declarado cumplido | Sin evidencia (136 días) |
| Piloto con usuarios internos (2026-07-30) | Declarado cumplido | Sin evidencia (80 días) |
| Salida a producción (2026-09-25) | Declarado cumplido | Sin evidencia (23 días) |
| CT-812 Licenciamiento del motor (2026-03-04) | Pendiente, 228 días de atraso | Ninguna |
| CT-812 Bolsa de horas (2026-05-21) | Aceptado | Sin acta de recibo |
| CT-812 Parametrización del tarifario (2026-08-07) | Aceptado | Acta de recibo del 2026-08-20 |

Los cinco hitos figuran como cumplidos, pero el avance declarado es 51 %. El plan soportaría 100 %, y la brecha es de 49 puntos.

### Fuera de alcance final
Solo consta "lo que otro proyecto cubre", sin nombrar el proyecto, decidido en el acta del 2025-12-06. No hay solicitudes de cambio. Con el alcance descrito como "Componente 1, 2, 3", no se puede comprobar si se entregó todo ni si se recortó algo.

### Números finales
| | Original | Vigente | Final |
|---|---|---|---|
| Fecha de cierre | 2026-09-25 | 2026-09-25 | Sin dato |
| Presupuesto aprobado | 3.300.000.000 COP | 3.300.000.000 COP | Ejecutado 1.587.108.579 (48,1 %); comprometido 1.661.270.154 (50,3 %) |

- **Proyección al cierre:** 3.241.959.414 COP, es decir −1,8 % frente al aprobado.
- **Disponible real:** 1.638.729.846 COP.
- **Replanificaciones:** 0, con una sola versión de línea base. Los 0 días de desviación significan que nadie movió el plan, no que se haya cumplido: la fecha de cierre pasó hace 23 días.
- **Origen de las cifras de dinero:** son declaradas en el informe de avance, sin verificar contra contabilidad.

### RAID al cierre
- **Materializado:** el equipo perdió dos semanas por la rotación de un desarrollador clave, sin fecha precisa.
- **No materializados:** sin dato.
- **Abiertos, ninguno con doliente nombrado:**
  - Concentración del conocimiento en una sola persona.
  - Licenciamiento del motor, vencido 228 días.
  - Redes del Norte facturó 614.970.173 COP el 2026-10-01 y lo aceptado suma 534.681.656. La diferencia es de 80.288.517 COP.
  - Bolsa de horas aceptada sin acta de recibo.

Lo que queda abierto sin doliente no está cerrado.

### Lecciones
Solo entran las que tienen un hecho documentado detrás.

| Qué pasó | Cuándo | Efecto | Qué haríamos distinto |
|---|---|---|---|
| El licenciamiento (CT-812) vencía el 2026-03-04 y sigue pendiente | 2026-03-04 a 2026-10-18 | 228 días de atraso | La causa no consta en ningún documento. Un entregable vencido tanto tiempo, con otros dos aceptados detrás, debió escalarse. |
| Se facturó más de lo aceptado | 2026-10-01 | 80.288.517 COP sin aceptación que los respalde | Condicionar cada pago a un acta de recibo. |
| Cinco hitos "cumplidos" sin evidencia, con avance en 51 % | 2026-02-10 a 2026-09-25 | La fecha de cierre pasó sin que nadie lo notara | Marcar un hito como cumplido solo con el documento que lo prueba. |
| Rotación de un desarrollador clave | Sin fecha precisa | Dos semanas perdidas | Sin dato sobre fecha ni sobre el hito afectado. |

### Sin dato
- Si la migración está en producción y cualquier medición del criterio de éxito.
- Qué son los Componentes 1, 2 y 3, y si el alcance se entregó.
- Evidencia de los cinco hitos y del acta de recibo de la bolsa de horas.
- Qué proyecto cubre lo que quedó fuera de alcance.
- Fecha real de cierre y gasto verificado contra contabilidad.
- Doliente de cada punto abierto, y el producto asociado y la fase, que la ficha marca como no encontrados.
- Causa del atraso del licenciamiento.

### Después
Ofrezco mover la carpeta a `archivo/` y congelar la ficha, pero no lo hice. El cierre no está declarado y hay puntos abiertos sin doliente. Archivar sacaría el proyecto del barrido diario con cuatro señales sin explicar. Sugiero que el comité decida si cierra el proyecto por decisión, no por cumplimiento, o si se replanifica.

Lo mostrado aquí está guardado tal cual en `estado/corridas/salida-project-closure.md`.