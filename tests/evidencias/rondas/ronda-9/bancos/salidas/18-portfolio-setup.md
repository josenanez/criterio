# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos

La configuración está instalada y probé con tres proyectos. Todavía no leí los otros diez.

**Miré:** 71 documentos en 13 proyectos. Los formatos son .md (36), .docx (12), .pdf (10), .xlsx (10), .csv, .json y .txt (1 cada uno). El más reciente es del 2026-10-17.
**Eres:** PMO del portafolio. Lo propuse yo porque hay 13 proyectos.
**Te aviso:** dos días antes del comité semanal. Dejé anotado el 2026-10-24 como próximo comité; es un supuesto mío, porque los documentos muestran comités semanales pero no una fecha fija.
**En:** presentación, que es el valor por defecto.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.4.0, con fecha 2026-10-17. Tomé el sí de tu mensaje de invocación. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.4.0-2026-10-17.md` y `.pdf`. El SHA-256 del .md empieza por `96015115a67f6c94…`.

Decidí sin preguntar, porque no había quién respondiera:
- Los documentos están en `documentos/proyectos`, lo que voy encontrando en `estado` y los informes irán en `reportes`.
- El nombre de la instalación quedó como «Portafolio de proyectos». Lo puedes cambiar cuando quieras.
- Hice 0 preguntas en total.

### Probé con tres proyectos
Tomé los de documentación más reciente. Las fichas están en `estado/records/` y selladas.

| Proyecto | Docs | Qué supe | Qué no está |
|---|---|---|---|
| PRY-200 Originación digital | 16 | Gerente Diana Molina, 18.000 M COP aprobados, cierre 2027-06-04. Declara verde, 36 %. Sigo 26 compromisos de comité. | Autoridad del gerente, etapa, proveedor o contrato. |
| PRY-203 Open Banking | 6 | Gerente Óscar Ramírez, 6.800 M COP, cierre 2027-03-30 (la línea base original decía 2026-12-06). Declara verde, 60 %. | Autoridad, etapa. El documento de CC-01 dice «autorizada por el comité» y no nombra a nadie. |
| PRY-201 Core de depósitos | 5 | Gerente Óscar Ramírez, 1.200 M COP, cierre 2026-11-22. Declara rojo, 29 %. | Autoridad, etapa. |

PRY-200 publicó su propia `ficha-pm.json`. La guardé aparte, sin mezclarla con mi lectura.

### Qué levantó el cálculo (25 señales)
- **PRY-200, declarado verde (16 señales):**
  - El hito «Diseño funcional aprobado» venció hace 12 días.
  - La proyección al cierre está 15,9 % sobre lo aprobado.
  - Hay 8 compromisos vencidos sin acta; el más viejo, 25 días.
  - Hay 3 compromisos sin fecha.
  - «Enviar el documento 1» se reprogramó 6 veces y «Cerrar la prueba 2», 4.
  - El cálculo contradice el verde.
  - En las notas del 2026-10-17 se comentó un riesgo con el proveedor que nadie registró.
- **PRY-203, declarado verde (6 señales):**
  - Lleva 114 días de atraso (46,2 %) contra la línea base original.
  - «Integración con el core» venció hace 12 días.
  - Dos hitos figuran cerrados sin acta de recibo.
  - CC-01 (+114 días, +228 M COP) está autorizada sin línea base nueva.
  - El cálculo contradice el verde.
- **PRY-201, declarado rojo (3 señales):**
  - Declara 29 % de avance, pero su cronograma tiene 3 de 4 hitos cerrados, que sustentan entre 75 y 100 %.
  - Dos de esos hitos cerrados no traen acta.

### El portafolio completo
Faltan 10 proyectos y 44 documentos, en un solo lote y uno tras otro. Calculo unos 20 a 30 minutos. Es una estimación mía a partir de estos tres, no una medida.

### Lo que le falta a tu carpeta
- PRY-208, PRY-209 y PRY-211 no tienen cronograma, así que no hay hitos ni atraso que calcular.
- PRY-202 solo trae acta, cronograma e informe de avance.
- En los tres proyectos que leí, solo uno de los cinco hitos declarados cerrados trae su acta de recibo.
- Ninguna de las tres actas de constitución declara la autoridad del gerente.
- Las actas dicen «Dependencias: ninguna declarada», pero los informes de PRY-200 y PRY-203 listan como riesgo la dependencia del calendario de liberaciones del core.
- `estado/PRY-200-originación-digital/` ya existía, creada por el agente de ese proyecto. La dejé como estaba. Las fichas del portafolio van en `estado/records/`.

Ninguno de estos puntos es bloqueante.

La corrida quedó registrada como `2026-10-17-portfolio-setup-1`, con lo anterior guardado en `estado/corridas/salida-portfolio-setup.md`. Tardó 131 segundos. No medí con reloj los minutos hasta el primer resultado, así que no doy esa cifra.

Puedo correr los 10 proyectos que faltan. Si tienes equipo de gerentes, también puedo publicar el estándar en una carpeta compartida para que usen los mismos criterios.