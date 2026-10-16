# /criterio-portfolio:portfolio-setup documentos/proyectos

Dejé la instalación lista y registré la corrida; esto es lo que quedó.

## Listo — Portafolio de proyectos

**Miré:** 77 documentos en 13 proyectos. Formatos: .md (38), .docx (11), .pdf (10), .csv (9), .xlsx (7), .json (1) y .txt (1). El más reciente es del 2026-10-16.
**Eres:** PMO del portafolio. Lo propuse porque hay varios proyectos.
**Te aviso:** dos días antes del comité. No diste fecha de comité, así que propuse un informe semanal.
**En:** presentación (valor sugerido).
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.11 (términos 1.1) el 2026-10-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.11-2026-10-16.md` y `.pdf`. SHA-256: `41a739aec7049af3…`.

La configuración está en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes irán a `reportes/`. No hice ninguna pregunta; en cada punto tomé el valor sugerido.

### Probé con tres proyectos

Tomé los de documentación más reciente: PRY-200, PRY-210 y PRY-202. PRY-202 empata con otros tres proyectos en fecha, así que desempaté por código. Las tres fichas quedaron selladas en `estado/records/`.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-200 Mantenimiento predictivo de camiones | 14 | Gerente Ricardo Salas, presupuesto COP 1.200 M. Declara amarillo y 54%. Tiene 26 compromisos tomados de los comités. | Facultad del gerente y etapa. Ningún acta de recibo para sus 4 hitos "cerrados". |
| PRY-210 Programa de relacionamiento comunitario | 7 | Gerente Laura Vélez, presupuesto COP 3.300 M. Declara verde y 72%. Tiene una solicitud de cambio, CC-01, pendiente. | Facultad del gerente, etapa y producto (el acta dice «No aplica»). |
| PRY-202 Planta de tratamiento de agua | 6 | Gerente Javier Hoyos, presupuesto COP 6.800 M. Declara verde y 35%. | Facultad del gerente, etapa y producto. Sin acta de recibo para 2 de sus 4 hitos. |

**Señales que levantó el cálculo (26 en total):**
- **PRY-200:**
  - 4 hitos declarados cerrados sin acta, de hace entre 69 y 385 días.
  - Declara 54% con los 4 hitos cerrados, una brecha de 46 puntos.
  - 6 compromisos vencidos. Los más viejos son «Validar el ambiente 4» (Sandra Gil) y «Aprobar el diseño 5» (Liliana Torres), con 12 días cada uno.
  - «Enviar el documento 1» (Elena Duarte) se ha reprogramado 6 veces, del 2026-09-19 al 2026-12-12. «Cerrar la prueba 2» (Diana Molina), 5 veces.
  - 2 compromisos sin fecha.
  - La fecha de cierre no coincide entre la ficha del gerente (2026-09-30) y el último hito del cronograma (2026-08-08).
- **PRY-202:** el verde queda contradicho. Declara 35% con los 4 hitos cerrados (65 puntos de brecha), y 2 de esos hitos no tienen acta.
- **PRY-210:** el verde también queda contradicho.
  - El cronograma v2 del 2026-10-14 ya movió 33 días el último hito, del 2027-07-19 al 2027-08-21. Eso es justo lo que pide CC-01, que sigue pendiente de comité, así que hay 33 días movidos y 0 autorizados.
  - Declara 72%, pero solo 1 de 5 hitos está cerrado.

Al sellar, el sistema toma como fecha de cierre la del último hito del cronograma, no la «Cierre» del acta. Por eso PRY-200 y PRY-202 quedaron con cierre 2026-08-08 y 2026-08-29, y sus actas dicen 2026-09-30 y 2026-09-23. Conviene confirmar cuál es la fecha vigente.

### El portafolio completo

Faltan 10 proyectos (PRY-199, 201, 203 a 209 y 211), unos 62 documentos, en dos lotes uno tras otro. Calculo entre 25 y 30 minutos.

### Lo que le falta a tu carpeta

Ninguno bloquea el análisis:
- **Actas de recibo:** hay hitos "cerrados" en el cronograma sin acta que lo pruebe. Es lo que más señales produjo.
- **Facultad del gerente:** ninguna de las tres actas de constitución dice hasta qué monto o cambio puede decidir sin subir a comité.
- **Sin cronograma ni actas:** PRY-206 y PRY-209 no tienen cronograma, y PRY-201 y PRY-205 no tienen actas de reunión.
- **Archivo suelto:** las notas de PRY-200 del 2026-10-16 están fuera de `30-reuniones/`.
- **Cambio de fechas adelantado:** el cronograma v2 de PRY-210 mueve fechas antes de que el comité apruebe CC-01.
- **Carpeta ajena:** `estado/PRY-200-mantenimiento-predictivo-de-camiones/` tiene corridas del agente de proyecto y se creó antes de esta sesión. No la toqué.

La corrida quedó registrada como `2026-10-16-portfolio-setup-1`, con su salida en `estado/corridas/salida-portfolio-setup.md`. Duró 137 segundos medidos.

¿Corro el portafolio completo? Si tienes un equipo de gerentes de proyecto, también puedo publicar el estándar en una carpeta compartida.