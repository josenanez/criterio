# /criterio-portfolio:portfolio-setup documentos/proyectos

Soy Vera, el agente PMO de Criterio. Leo la documentación que ya tienes y digo qué no se sostiene.

Miré `documentos/proyectos`: 13 proyectos, 72 documentos, sin ninguno ilegible. Formatos: .md (36), .docx (14), .pdf (8), .xlsx (7), .csv (5), .json (1), .txt (1). El más reciente es del 2026-10-16.

Nadie respondió preguntas en esta prueba, así que tomé la respuesta sugerida en cada punto:
- **Eres:** PMO del portafolio, porque hay 13 proyectos.
- **Comité:** semanal, porque los archivos se llaman `comite-semanal`. Puse el próximo el 2026-10-21 y el informe llega dos días antes.
- **Formato:** presentación.
- **Dónde guardo lo que encuentro:** `estado/` y `reportes/`, junto a la carpeta de documentos y fuera de `.criterio/`.
- **Costo de una corrida:** lotes de 10 proyectos, uno tras otro, hasta 400 documentos, sin releer lo que no cambió.

## Listo — Portafolio de proyectos

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-16 para la versión 0.3.11 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.11-2026-10-16.md` y `.pdf`. SHA-256: 41a739aec7049af3…

La configuración quedó en `.criterio/portafolio/config.json` y la verificación pasó sin problemas.

### Probé con tres proyectos

Tomé los tres con documentos del 2026-10-16: PRY-208, PRY-201 y PRY-211. Las tres fichas quedaron en `estado/records/` y selladas.

Primero escribí PRY-211 con un error mío. La fecha vigente de los compromisos reprogramados quedó mal, y `compute` los marcó "sin fecha". Corregí las fichas, las resellé y recalculé. Lo que sigue sale del cálculo corregido.

| Proyecto | Documentos leídos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-208 Motor de decisión | 2 de 2 | Gerente Jorge Medina, patrocinador Javier Hoyos, presupuesto aprobado 800 M COP, cierre 2027-07-24. El informe del 2026-10-16 declara **rojo** y 41 %. | Producto (el acta dice «No aplica»), facultad del gerente, etapa, cronograma e hitos. |
| PRY-201 Core de depósitos | 7 de 7 | Gerente Mauricio Pérez, patrocinador Elena Duarte, producto cuenta de ahorros, presupuesto aprobado 4.200 M COP. El informe del 2026-10-12 declara **rojo** y 55 %. CC-01 pide +43 días y +86 M COP, «autorizada por el comité». | Facultad del gerente, etapa, quién autorizó CC-01 y una nueva fecha de cierre que lo respalde. |
| PRY-211 Cobranza digital | 16 de 16 | Gerente Beatriz Cuéllar, patrocinadora Paula Céspedes, producto recaudos, presupuesto aprobado 2.400 M COP. El informe del 2026-10-13 declara **verde** y 89 %. | Facultad del gerente, etapa y acta de recibo de dos hitos declarados cerrados. |

PRY-211 trae `ficha-pm.json`. La conservé entera en `pm_record`, sin mezclarla con mi lectura.

### Lo que `compute` levantó

Fueron 24 señales en los tres proyectos.

**PRY-211: declarado verde, y el cálculo lo contradice.** Es el único verde contradicho (`declared_vs_evidence`).
- **Compromisos vencidos (7):**
  - «Validar el ambiente 4» (Camilo Beltrán): 33 días.
  - «Confirmar la fecha 7» (Sandra Gil): 20 días. Se dijo entregado y no hay acta.
  - «Entregar el punto 16» (Diana Molina): 13 días. Se dijo entregado y no hay acta.
  - «Actualizar la matriz 6» (Felipe Arango): 12 días. Se dijo entregado y no hay acta.
  - «Revisar el anexo 19» (Laura Vélez): 11 días.
  - «Aprobar el diseño 5» (Ricardo Salas): 4 días.
  - «Confirmar la fecha 23» (Felipe Arango): 2 días.
- **Compromisos reprogramados:** «Cerrar la prueba 2» (María Restrepo) se movió 6 veces, de 2026-10-01 a 2026-12-09. «Enviar el documento 1» (Ricardo Salas) se movió 4 veces y ahora está para 2026-11-29.
- **Compromisos sin fecha (3):** «Validar el ambiente 20» (Andrés Lozano), «Entregar el punto 24» (Carlos Peña) y «Mandar el ajuste del presupuesto» (Laura Vélez, notas del 2026-10-16).
- **Hitos declarados cerrados sin acta (2):** «Diseño funcional aprobado» y «Ambiente de pruebas certificado».
- **Costo:** la proyección al cierre es 2.771 M COP contra 2.400 M aprobados, un 15,5 % de más.
- **Fecha de cierre:** el acta dice 2027-03-01 y el cronograma termina el 2026-12-25 (`pm_vs_pmo`). Ningún documento posterior aclara cuál vale.

**PRY-201: declarado rojo, y las señales lo respaldan.**
- **Tiempo:** +43 días, un 11,6 % sobre la línea base original. Pasa el umbral de 10 %.
- **Avance contra plan:** declara 55 %, pero el cronograma tiene sus 4 hitos cerrados, una diferencia de 45 puntos.
- **Hitos cerrados sin acta (3):** «Ambiente de pruebas certificado», «Integración con el core» y «Piloto con usuarios internos». El acta de «Diseño funcional aprobado» es del 2026-10-16, más de un año después de su fecha de línea base.
- **Compromiso sin fecha:** «Entregar el punto 19» (Óscar Ramírez).

**PRY-208:** la proyección al cierre (984 M COP) supera en 23 % el presupuesto aprobado.

### El portafolio completo
Quedan 10 proyectos y 47 documentos, en un solo lote que se lee uno tras otro. Calculo entre 30 y 40 minutos, pero es una estimación mía. Leer estos tres proyectos fue lo que más tomó.

Una aclaración sobre el tiempo: el archivo de salida dice que no medí los minutos hasta el primer resultado. El registro de la corrida sí midió 150 segundos, pero cuentan desde que abrí la corrida, después de configurar y aceptar los términos.

### Lo que le falta a tu carpeta
- **Facultad del gerente:** ninguna de las tres actas la dice. Sin ella no se puede saber si un cambio como CC-01 excede lo que el gerente podía aprobar.
- **Cronogramas:** PRY-205, PRY-207, PRY-208 y PRY-209 no tienen archivo en `10-plan`. Sin hitos no se mide el avance contra plan.
- **Actas de recibo:** casi todos los hitos «cerrados» no traen la suya.
- **Compromisos:** en los comités de PRY-211 hay compromisos «por definir» y entregas dichas en reunión sin acta.
- **Riesgo no registrado:** las notas del 2026-10-16 de PRY-211 dicen que el proveedor podría no llegar con el equipo completo y nadie lo anotó. Lo dejé en la ficha.
- **Autorización de CC-01:** dice «autorizada por el comité» sin nombre ni acta de ese comité.

Siguiente paso: correr el portafolio completo. Si lo quieres, también puedo publicar el estándar en una carpeta compartida para que los gerentes de proyecto usen los mismos criterios.

Corrida registrada como `2026-10-16-portfolio-setup-1`. La salida completa está en `estado/corridas/salida-portfolio-setup.md`.