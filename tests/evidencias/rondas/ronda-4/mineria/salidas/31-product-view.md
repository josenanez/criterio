# /criterio-portfolio:product-view despacho de flota

**Productos al 2026-10-15, consulta «despacho de flota».** Salió de las fichas de `estado/records` (13 proyectos). Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

«Despacho de flota» tiene un solo proyecto, PRY-203 Despacho automático de flota. La vista por producto no aporta nada ahí, así que no armé sección por producto. Esto es lo que dice el cálculo:

- **Señales abiertas (3):**
  - El hito «Ingeniería básica aprobada» figura cumplido, pero no hay evidencia. Vencía el 2026-03-13, hace 216 días.
  - Hay un compromiso sin fecha: Óscar Ramírez, «Entregar el punto 34», en el comité del 2026-10-15.
  - El informe del 2026-10-10 declara **verde** y no reconoce la primera señal.
- **Avance:** declarado 41 %, y el plan sustenta entre 50 % y 75 %. La brecha es de 9,0 puntos, bajo el umbral de 10, así que no es alerta.
- **Dinero (COP):**

  | Concepto | Cifra |
  |---|---|
  | Aprobado | 1.200.000.000 |
  | Comprometido | 731.337.940 (60,9 %) |
  | Ejecutado | 468.897.081 (39,1 %) |
  | Proyección | 1.166.182.042 (−2,8 % frente a lo aprobado) |

  Como es un solo proyecto, la suma está completa.
- **Fecha comprometida del producto:** 2027-03-20, de PRY-203. No hay atraso contra la línea base original ni contra la vigente.
- **Dependencias internas:** ninguna, porque hay un solo proyecto.
- **Datos que faltan:** autoridad y fase. Diez campos de identidad y plan, incluida la cifra aprobada, vienen de un documento del 2025-10-30 y llegan justo al umbral de 12 meses. Conviene confirmarlos.

**Siete proyectos no declaran producto** (nadie responde por el conjunto al que sirven):

| Proyecto | Área dueña |
|---|---|
| PRY-201 Ampliación de la relavera | Mina |
| PRY-202 Planta de tratamiento de agua | Mina |
| PRY-205 Sistema de gestión de seguridad | no declarada en la ficha |
| PRY-206 Red privada LTE en mina | Logística |
| PRY-209 Electrificación de equipos | Seguridad y Salud |
| PRY-210 Programa de relacionamiento comunitario | Tecnología |
| PRY-211 Control de polvo en vías | Geología |

**Pie de rigor:**
- Copié las cifras de la salida de `compute` y no promedié nada.
- Solo leí las fichas, no los documentos originales.
- No sé qué se habló fuera de los documentos.
- «Sin evidencia» en PRY-203 quiere decir que la ficha no trae evidencia marcada (0 fuentes de evidencia, 2 de declaración, 17 sin marcar), no que no exista.
- «Monitoreo de flota» (PRY-200) y «despacho de flota» (PRY-203) son productos distintos en las fichas. Ninguna declara dependencia entre ellos, y no afirmo que se solapen.

Dejé la corrida registrada como `2026-10-15-product-view-1`, con la salida completa en `estado/corridas/salida-product-view.md`. Tardó 26 segundos. El registro cuenta los 51 hallazgos del portafolio, de los cuales 3 son de PRY-203.