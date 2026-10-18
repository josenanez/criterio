# /criterio-portfolio:product-view puntos de fidelización

**«Puntos de fidelización» tiene un solo proyecto, PRY-201 Programa de fidelización.** La vista por producto no aporta nada distinto a la del proyecto, así que no armé sección de producto. Salen de las fichas de `estado/`, recalculadas con `compute` al 2026-10-18. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré de nuevo.

- **Fecha:** 2027-01-01, sin replanificaciones.
- **Dinero:** las cuatro cifras están completas.

| Aprobado | Comprometido | Ejecutado | Proyección |
|---|---|---|---|
| 3.300.000.000 COP | 2.647.230.813 COP (80,2 %) | 860.644.236 COP (26,1 %) | 4.046.399.504 COP (22,6 % sobre lo aprobado) |

**Lo que hay que ver en PRY-201 (9 alertas):**
- **Estado declarado:** el informe del 2026-10-17 dice verde y 86 % de avance. El plan sustenta entre 60 y 80 %. Ese informe no reconoce cuatro de las señales abiertas: hitos, costo, entregables tardíos del proveedor y facturación.
- **Hitos sin evidencia:** tres hitos están declarados cumplidos sin evidencia.
  - «Diseño de la experiencia aprobado» (153 días de vencido).
  - «Ambiente de pruebas certificado» (96 días).
  - «Integración con el ERP» (39 días).
- **Costo:** la proyección supera lo aprobado en 22,6 %, contra un umbral de 10 %.
- **Proveedor Tecnología para Tiendas Ltda.:**
  - Dos «Bolsa de horas de desarrollo» están pendientes: CT-144 con 53 días de atraso y CT-836 con 1.
  - «Licenciamiento de la plataforma» (CT-836) está aceptado sin evidencia.
  - Se facturaron 419.283.282 COP contra 311.826.194 COP aceptados, una diferencia de 107.457.088 COP.
- **Fichas:** la ficha no trae autoridad ni fase.

Tampoco hay dependencias internas, porque el producto tiene un solo proyecto, ni dependencias declaradas en la ficha de PRY-201.

**Proyectos sin producto declarado.** Son un hallazgo de gobierno: nadie puede responder por el conjunto al que sirven.

| Proyecto | Área dueña |
|---|---|
| PRY-202 Centro de distribución norte | Abastecimiento |
| PRY-203 Reposición automática | Comercial |
| PRY-206 Precios dinámicos | Comercio electrónico |
| PRY-209 Migración del ERP | Mercadeo |
| PRY-210 Etiquetas electrónicas de precio | Comercio electrónico |
| PRY-211 Pronóstico de demanda | Finanzas |

No sé si alguno de esos seis sirve a este producto. Por ejemplo, PRY-201 tiene el hito «Integración con el ERP» y existe PRY-209 Migración del ERP, pero las fichas no los relacionan y no lo supuse. Es una pregunta para las áreas dueñas.

El resultado está en `estado/corridas/salida-product-view.md` y la corrida quedó registrada como `2026-10-18-product-view-1`. Tardó 27 segundos sobre 13 proyectos.

Este es un borrador hecho solo con las fichas. La verificación contra los documentos es de la PMO.