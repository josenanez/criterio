# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos

Nadie respondió preguntas en esta prueba, así que usé los valores sugeridos. La corrida quedó registrada (`2026-10-15-portfolio-setup-2`). Hice una primera corrida con una cifra equivocada y la corregí.

**Miré:** 82 documentos en 13 proyectos. Formatos: .md (37), .docx (16), .pdf (14), .xlsx (9), .csv (4), .json (1), .txt (1). El más reciente es del 2026-10-15.
**Eres:** PMO del portafolio (13 proyectos).
**Te aviso:** dos días antes del comité semanal. Supuse que el próximo es el 2026-10-21, así que el aviso llega el 2026-10-19.
**En:** presentación.
**Términos:** aceptados por José Francisco Ñáñez (2026-10-15) para la versión 0.3.9 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.9-2026-10-15.md` y `.pdf`. SHA-256: .md `f0f8a373c9bdced2…`, .pdf `979c05533bd27dac…`.

La configuración está en `.criterio/portafolio/config.json`. Lo que encuentre irá en `estado/` y los informes en `reportes/`. Si quieres cambiar el comité, su fecha o el formato, dímelo aquí.

### Probé con tres proyectos

Los de documentación más reciente: PRY-209, PRY-205 y PRY-207. El cálculo levantó 26 señales entre los tres.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-209 Nómina electrónica | 10 | Declara verde y 86%. Presupuesto 1.200.000.000 COP, ejecutado 461.927.421. Solicitud de cambio CC-01 pendiente (+32 días, +64.000.000 COP). | Facultad del gerente, fase |
| PRY-205 Prevención de lavado | 5 | Declara rojo y 57%. Presupuesto 9.500.000.000 COP, ejecutado 2.710.944.241. Cierre 2026-12-09. | Facultad del gerente, fase, producto (el acta dice «No aplica») |
| PRY-207 Onboarding PyME | 19 | Declara amarillo y 65%. Presupuesto 6.800.000.000 COP, ejecutado 3.102.676.711. Tiene ficha del gerente, que dejé aparte sin mezclar. | Facultad del gerente, fase |

### Hallazgos

Los levantó el cálculo, no mi lectura.

- **PRY-209, el verde no se sostiene.**
  - Declara 86% y el cálculo da 100% por hitos; la desviación es de 32 días (16,8%).
  - Tres hitos están cerrados sin acta de recibo: Ambiente de pruebas, Piloto y Salida a producción.
  - Dos entregables del proveedor siguen «en curso» con 255 y 151 días de vencidos. La bolsa de horas figura como recibida sin acta.
  - La salida a producción se movió del 2026-06-20 al 2026-07-22 sin autorización: la solicitud CC-01 sigue pendiente de comité.
- **PRY-205, el rojo es coherente.**
  - Va 23 puntos por detrás de su plan.
  - Tres hitos están cerrados sin acta (Diseño funcional, Ambiente de pruebas, Integración con el core).
- **PRY-207, el compromiso que no se cierra.**
  - «Cerrar la prueba 2» lleva 6 reprogramaciones, del 2026-09-23 al 2026-12-07. «Enviar el documento 1» lleva 4.
  - Hay 6 compromisos vencidos sin evidencia, 2 sin fecha y un hito cerrado sin acta. En dos de los vencidos alguien dijo en comité que ya había entregado, pero no hay acta.
  - Hay una diferencia sobre la fecha de cierre: la ficha del gerente dice 2027-11-03 y el cálculo de la PMO sale de la última fecha del cronograma, 2027-08-10. Esa fecha es del hito «Integración con el core», no de un cierre, así que conviene preguntarle al gerente cuál está vigente.
  - Se comentó en la reunión del 2026-10-15 que el proveedor podría no llegar con el equipo completo, y nadie lo anotó como riesgo. Quedó en la ficha como riesgo no registrado.

### El portafolio completo

Faltan 10 proyectos (PRY-199 a PRY-204, PRY-206, PRY-208, PRY-210 y PRY-211), con 48 documentos. Se leerían en 2 lotes, uno tras otro en esta misma conversación, en unos 20 minutos.

### Lo que le falta a tu carpeta

Ninguno de estos puntos bloquea el análisis.
- Los cronogramas dan hitos por cerrados sin su acta de recibo; es lo que más señales levanta.
- Ninguna acta de constitución dice hasta qué monto puede decidir el gerente sin subir a comité.
- Varias actas traen alcance genérico («Componente 1, 2, 3») y «Dependencias: ninguna declarada».
- Varios proyectos con actas de 2025 (PRY-203, PRY-206, PRY-208) tienen pocos documentos de seguimiento.
- En PRY-207 hay una nota de reunión suelta en la raíz del proyecto, fuera de `30-reuniones/`.

¿Corro el portafolio completo? Como eres PMO, también puedo publicar el estándar en una carpeta compartida para que los gerentes usen los mismos criterios.