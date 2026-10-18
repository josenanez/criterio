# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Cooperativa (instalación de prueba)

La instalación quedó lista y probé el barrido con tres proyectos. Nadie respondió preguntas: en cada una tomé el valor sugerido.

- **Qué miré:** 67 documentos en 13 proyectos (PRY-199 a PRY-211). Hay .md, .docx, .pdf, .csv, .xlsx, .json y .txt. El más reciente es del 2026-10-17 y ninguno quedó ilegible.
- **Rol y cadencia:** PMO del portafolio. Informe en presentación (`pptx`), dos días antes de un comité semanal. Supuse el primer comité el 2026-10-24, porque ninguna carpeta lo declara.
- **Términos:** versión 1.1, aceptada a nombre de José Francisco Ñáñez el 2026-10-17. El sí y el nombre vinieron en la instrucción de la prueba, y mostré el texto antes de registrarlo. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.4.0-2026-10-17.md` y `.pdf`. El SHA-256 del .md empieza por `96015115a67f6c94…`.
- **Dónde queda cada cosa:** la configuración en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes irán a `reportes/`, que todavía no existe.

### Qué encontré en los tres proyectos

Tomé los tres con documentación más reciente: PRY-202, PRY-209 y PRY-199. Esto es lo que levantó `compute`:

- **PRY-202 (Core cooperativo):** declara verde con 55 % de avance, y cuatro señales lo contradicen.
  - El cronograma tiene 3 de 4 hitos cerrados, que sustentan entre 75 % y 100 %.
  - El hito «Integración con el core cooperativo» figura cerrado sin ningún acta de recibo.
  - El propio informe proyecta 24,8 % sobre el presupuesto aprobado.
  - Hay un compromiso vencido hace 7 días (Natalia Ospina, «Entregar el punto 23»).
- **PRY-209 (Convenios de libranza):** declara amarillo, y el informe no menciona los compromisos.
  - Hay 5 compromisos vencidos; el más antiguo lleva 16 días.
  - Hay 3 compromisos reprogramados varias veces; «Cerrar la prueba 2» va en 6 reprogramaciones.
  - Hay 4 compromisos sin fecha.
  - Costo y plazo están dentro de umbral.
- **PRY-199 (Mobiliario de agencias):** `compute` no levantó señales. Eso no valida el proyecto. Declara 720.000.000 COP ejecutados y no hay ninguna factura en la carpeta.

En PRY-202 el informe también declara más ejecutado (724.509.244 COP) que comprometido (447.707.288 COP). `compute` no lo levantó como señal; lo dejo como pregunta para el gerente.

### Lo que le falta a la carpeta

Ninguna de estas faltas bloquea el análisis:

- **Autoridad del gerente:** ninguna de las tres actas la declara.
- **Fechas de compromiso:** las tablas de comité dicen «por definir» y las notas «la otra semana».
- **Alcance sin nombrar:** las tres actas dicen «Componente 1, 2, 3».
- **Notas sueltas:** hay un `.txt` en la raíz de PRY-209, fuera de `30-reuniones`.

### Lo que sigue

- **Portafolio completo:** faltan 10 proyectos y 41 documentos. El tiempo total no lo medí, así que no doy cifra.
- **Estándar compartido:** no publiqué ningún estándar, porque no hay carpeta compartida indicada.
- **Tiempo de la prueba:** el registro de la corrida mide 109 segundos, pero no sé cuánto fue en reloj hasta el primer resultado.
- **Estado de PRY-209:** `estado/` ya traía trabajo del agente de proyecto sobre PRY-209. No lo toqué.

La salida completa quedó en `estado/corridas/salida-portfolio-setup.md`, y la corrida se registró como `2026-10-17-portfolio-setup-1`.