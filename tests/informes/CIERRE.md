# Cierre de la prueba longitudinal de cinco días

Cinco corridas, del día 1 (2026-09-01) al día 5 (2026-09-29), una semana de trabajo por
día, sobre 51 proyectos y 66 productos. El material crece de 462 a 657 documentos
(593 `.md`, 64 `.csv` al corte del día 5).

## 1 · La fiabilidad se sostuvo entre las cuatro disposiciones

Precisión 100.0% y cobertura 100.0% los cinco días, con cero falsos positivos y cero
falsos negativos: 455, 530, 590, 634 y 686 aciertos. El material se escribió ordenado
(`referencia`, días 1 y 5), `plana`, `revuelta` y `sin_carpeta`, y lo esperado no cambió.
**No hubo caída entre días, así que no hay dependencia del layout.** El recorrido cuesta
4.8–7.0 ms por documento, mediana 5.8, y una corrida completa 3.0–3.5 s.

Los dos controles negativos declarados —`PRY-199` y `PRD-299`— produjeron cero hallazgos
las cinco veces. Son 2 controles sobre 117 casos: pasaron, y son poco.

## 2 · Ninguna señal falló, y eso no es un aprobado

De cero fallos, cero fueron falsos positivos. La pregunta de cuál señal se arregla
primero no tiene respuesta en estos términos, así que lo que hay que arreglar no es una
señal que se equivocó sino **tres que no dejaron evidencia**, y el defecto de las tres
está en la capa del material —en `simulador.py`—, no en el código, ni en la extracción,
ni en la clave de respuestas:

- **`commitment_rescheduled` nunca se ejercitó.** Es la única de las 23 señales que la
  clave deduce que no tuvo un solo caso esperado en los cinco días. El umbral son 3
  reprogramaciones —cuatro fechas en el mismo compromiso— y con 45% semanal de
  reprogramar *alguno* de los abiertos, una ventana de cinco semanas no lo alcanza. Su
  100% es vacío: no se midió.
- **`governance_change` y `contradiction` no tienen material plantado.** Están en
  `SENALES_DE_EVIDENCIA` y en el código (`portafolio.py:525`), pero `solo_modelo` está
  vacío a propósito: viven en el corpus de dieciocho casos, no en esta organización de
  ciento quince. La capa del modelo se midió en cero casos.
- **La familia `vendor_*` se contó cinco veces y se probó una.** 12 + 20 + 7 + 4 = 43
  hallazgos, idénticos en los cinco días, porque `semana_proyecto` no toca
  `p["proveedores"]`: ningún acta de recibo nueva, ninguna factura nueva. Cinco días
  dieron un día de evidencia para el 6% de los hallazgos.

## 3 · El rastro entre días sí se siguió, y es lo único que estas corridas aportan

`milestone_met_without_evidence` baja 116 → 100 → 87 → 71 → 63: **53 hitos se cerraron
con acta en cuatro semanas y el agente dejó de reportar cada uno, con 0 falsos positivos.**
Nada se volvió a reportar después de cerrado. `silent` aparece el día 2 con 6 proyectos
—el umbral son 15 días, y el día 1 no tiene pasado— y baja a 4, 2 y 2 cuando vuelven a
producir documentos: el proyecto que se calló apareció, y desapareció al volver.
`rebaseline_unauthorized` sube 4 → 5 → 8 → 10 y `variance_time` 8 → 10 → 14 → 17.

**15 de las 25 señales no existen el día 1**: `silent`, `variance_cost`, `variance_time`,
`milestone_overdue`, `commitment_overdue`, `commitment_undated`, `declaration_stale`,
`budget_committed`, `change_without_baseline`, `claim_vs_metric`,
`rebaseline_unauthorized`, `requirement_undecided`, `requirement_without_owner`,
`requirement_without_acceptance` y `requirement_accepted_without_evidence`. Ninguna
corrida suelta las alcanza. La promesa movida por tercera vez es la excepción: la regla
existe —tres reprogramaciones, un hallazgo y no tres— y la ventana no llegó a probarla.

## 4 · La capa de los 37 comandos: 3 probados, 26 sin tocar

De los 37 comandos (17 `criterio-portfolio`, 9 `criterio-project`, 11 `criterio-product`),
**3 dejaron evidencia**: `portfolio-report` (d1, d2), `portfolio-scan` (d1, d2, 2 s) y
`portfolio-setup` (d1). De esos, las cifras las midió la corrida en 1 de 2 casos.

**Los 34 sin entrada en `registro.json` no se probaron.** No son aprobados sin medir: no
corrieron. `criterio-project` va 0 de 9 y `criterio-product` 0 de 11 — dos agentes
completos sin una sola evidencia.

Ocho más dejaron rastro en `.criterio/corridas/` sin que nadie lo registrara como
evidencia —`document-index`, `pm-agenda`, `pm-minutes`, `pm-wake`, `portfolio-wake`,
`product-discovery`, `product-requirements`, `product-wake`—, de corridas del 30 de
septiembre y el 1 de octubre, anteriores a esta prueba. Queda rastro de 11 comandos
distintos en total; **26 de 37 no corrieron nunca, en ninguna forma.**

---

**Qué no miden estas corridas.** La extracción con modelo: la hace
`tests/sintetico/extractor.py` sobre documentos de estructura conocida, sin modelo, así
que lo medido es la aritmética sobre una ficha bien construida. Documentos que no sean
markdown ni CSV. Y una organización real: el material es sintético y lo escribió este
repositorio, aunque la clave de respuestas se deduzca de los hechos con las reglas del
skill y no del código que se mide.
