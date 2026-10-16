# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Cooperativa

**Miré:** 76 documentos en 13 proyectos (md, docx, pdf, xlsx, csv, json, txt). El más reciente es del 2026-10-16.
**Eres:** PMO del portafolio. No había nadie a quien preguntar, así que tomé el valor sugerido.
**Te aviso:** dos días antes del comité del 2026-10-30. Lo supuse quincenal porque no se indicó comité.
**En:** presentación.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-16 (versión 0.3.12, términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.12-2026-10-16.md` y `.pdf`. El SHA-256 del .md empieza con 08da686bb7c9acf4…
**Dónde queda:** la configuración en `.criterio/portafolio/config.json`. Lo que voy encontrando va en `estado/` y los informes irán en `reportes/`.

### Probé con tres proyectos

Probé con los tres de documentación más reciente: PRY-207, PRY-208 y PRY-210. Los tres reportan verde, y en los tres el cálculo contradice ese verde.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-207 Microcrédito rural | 4 | Gerente Carlos Peña. Presupuesto de 3.300 M COP. Declara verde y 61%. Tres hitos declarados cerrados. | Acta de recibo de los tres hitos; facultad del gerente; fase. |
| PRY-208 Motor de crédito | 8 | Gerente Rubén Cárdenas. Presupuesto de 18.000 M COP. Declara verde y 67%. El cronograma v3 mueve el piloto al 2027-06-05. Dos solicitudes de cambio pendientes de comité. | Acta de recibo de diseño funcional y de ambiente de pruebas; cronograma v2; facultad del gerente; fase. |
| PRY-210 Corresponsales rurales | 19 | Gerente Liliana Torres. Presupuesto de 9.500 M COP. Declara verde y 47%. Leí 26 compromisos de reunión. El gerente publicó `ficha-pm.json`; la guardé aparte, sin fusionarla. | Acta de recibo de los cuatro hitos; facultad del gerente; fase. |

Los hallazgos son los que levantó el cálculo:

- **PRY-207:**
  - Tres hitos aparecen cerrados sin ninguna acta de recibo que lo pruebe.
  - Declara 61% y los hitos cerrados sostienen 100%.
- **PRY-208:**
  - El piloto se movió 161 días (48,3% sobre la línea base original) sin ninguna solicitud de cambio aprobada.
  - Hay dos hitos cerrados sin acta. La integración con el core sí tiene acta, del 2026-10-15.
  - Laura Vélez tiene vencido «Entregar el punto 16» desde el 2026-10-12.
- **PRY-210:**
  - El hito «Diseño funcional aprobado» venció el 2026-10-10 y sigue en curso.
  - Hay tres compromisos vencidos; el peor es «Enviar el documento 9», de Óscar Ramírez, con 24 días.
  - «Enviar el documento 1», de Andrés Lozano, se reprogramó 5 veces. «Cerrar la prueba 2», de Javier Hoyos, 4 veces.
  - Cuatro compromisos no tienen fecha.
  - Declara 47% y el cronograma sostiene entre 0 y 25%.

En total son 23 señales, con el verde contradicho en los tres proyectos.

### El portafolio completo

Faltan 10 proyectos (PRY-199 a PRY-206, PRY-209 y PRY-211) y 60 documentos, en 2 lotes. Calculo de 30 a 45 minutos con lo que vi.

### Lo que le falta a tu carpeta

Ninguno de estos puntos bloquea el análisis:

- **Actas de recibo de hitos:** faltan en PRY-207 y PRY-208.
- **Cronogramas intermedios:** PRY-208 no tiene el v2. PRY-207 solo tiene el v1 y su cierre del 2026-05-10 ya pasó sin documento posterior.
- **Facultad del gerente:** ninguna de las tres actas dice hasta qué monto o cambio puede decidir sin subir a comité.
- **Fase y producto:** la fase no aparece en ningún documento. En PRY-208 y PRY-210 el producto dice «No aplica».
- **Compromisos sin fecha:** en PRY-210 varios quedaron en «por definir» o «la otra semana».

### Sigue

Puedo correr el portafolio completo. También puedo publicar el estándar en una carpeta compartida para que los gerentes usen los mismos criterios.

La salida quedó en `estado/corridas/salida-portfolio-setup.md` y la corrida se registró como `2026-10-16-portfolio-setup-1`. Fueron 0 preguntas y 146 segundos de cómputo medido.