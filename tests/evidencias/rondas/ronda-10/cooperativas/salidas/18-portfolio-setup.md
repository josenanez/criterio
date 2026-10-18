# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Cooperativa

**Miré:** 75 documentos en 13 proyectos (PRY-199 a PRY-211). Los formatos son md 37, pdf 15, csv 10, docx 9, xlsx 2, json 1 y txt 1. El más reciente es del 2026-10-18.
**Eres:** PMO del portafolio, que es la propuesta por defecto cuando hay 13 proyectos.
**Te aviso:** dos días antes del comité semanal. Tomé el 2026-10-25 como próximo comité, es un supuesto mío sin confirmar, así que el informe saldría el 2026-10-23.
**En:** presentación.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-18 para la versión 1.1 (familia 0.5.0). El comprobante quedó en `.criterio/terminos/aceptacion-criterio-portfolio-0.5.0-2026-10-18.md` y `.pdf`. El SHA-256 del `.md` empieza por 9c54c0c51760b166…

Nadie podía responder, así que tomé las respuestas por defecto y no hice preguntas. El estado quedó en `estado/` y los informes irán a `reportes/`. La verificación de la configuración salió sin problemas.

### Probé con tres proyectos

Elegí PRY-201, PRY-202 y PRY-208, los de documentación más reciente. Las fichas están en `estado/records/` y selladas.

| Proyecto | Qué supe | Qué no está |
|---|---|---|
| PRY-201 Apertura de ahorro en línea (13 documentos) | Declara **verde, 91 %**. Presupuesto de 18.000 millones de COP, con proyección 4,3 % por encima. Cierre previsto el 2026-10-04. Tiene `ficha-pm.json` del gerente, que guardé aparte sin mezclarla con mi lectura. | Autoridad del gerente y etapa. Ningún acta prueba los hitos cerrados. |
| PRY-202 Core cooperativo (5 documentos) | Declara **amarillo, 67 %**. Presupuesto de 6.800 millones de COP, con proyección 3,7 % por encima. Cierre previsto el 2026-08-10, ya pasado. | Producto (el acta dice «No aplica»), autoridad y etapa. Solo el primer hito tiene acta de recibo. |
| PRY-208 Motor de crédito (6 documentos) | Declara **amarillo, 48 %**. Presupuesto de 6.800 millones de COP, con proyección 0,6 % por encima. Cierre previsto el 2026-11-22. | Producto («No aplica»), autoridad y etapa. Faltan el acta del hito «Diseño funcional aprobado» y la del piloto, que sigue pendiente. |

### Hallazgos

El cálculo levantó 22 señales. Estas son las principales.

- **PRY-201: el verde no se sostiene** (14 señales).
  - El hito «Integración con el core cooperativo» lleva 14 días vencido (plan del 2026-10-04).
  - Hay 5 compromisos vencidos y 3 reprogramados varias veces. El peor caso es «Enviar el documento 1»: 6 veces, del 2026-09-22 al 2026-12-20.
  - Hay 2 compromisos sin fecha.
  - Dos hitos figuran como cerrados sin acta que lo pruebe.
- **PRY-202:**
  - Declara 67 % con sus 4 hitos cerrados. El plan sostiene 100 %, una brecha de 33 puntos.
  - Tres hitos cerrados no tienen acta. Un compromiso no tiene fecha.
- **PRY-208:**
  - Declara 48 % con 3 de 4 hitos cerrados. El plan sostiene entre 75 % y 100 %, una brecha de 27 puntos.
  - Un hito cerrado no tiene acta. Un compromiso no tiene fecha.
- **Autoridad del gerente:** no está documentada en ninguno de los tres.

### El portafolio completo

Faltan 10 proyectos (PRY-199, PRY-200, PRY-203 a PRY-207 y PRY-209 a PRY-211), unos 50 documentos, en dos lotes seguidos. Estimo de 20 a 30 minutos. Es una estimación a partir de lo que tomaron estos tres, no una medida.

### Lo que le falta a tu carpeta

Ninguno de estos puntos bloquea el análisis.

- Ninguna acta dice hasta dónde llega la autoridad del gerente.
- Los alcances son «Componente 1, 2 y 3» sin descripción, así que no hay contra qué contrastar un cambio de alcance.
- Los hitos se cierran en el cronograma, no en un acta de recibo. En PRY-202 el único recibo llegó 10 meses después de la fecha del plan.
- Las actas de constitución de PRY-201 y PRY-202 tienen 14 y 16 meses sin confirmación posterior de patrocinador, gerente, alcance ni presupuesto.
- PRY-202 y PRY-208 dicen «Producto asociado: No aplica», así que no entran a la vista por producto.
- Las notas del 2026-10-18 de PRY-201 están sueltas en la raíz del proyecto, fuera de `30-reuniones/`. De ahí salió un riesgo que nadie había registrado: el proveedor podría no llegar con el equipo completo.
- PRY-202 reporta ante el «Comité de Educación», un nombre raro para un proyecto de core cooperativo. Conviene confirmarlo.

La corrida quedó registrada como `2026-10-18-portfolio-setup-1`. El texto completo de esta salida está en `estado/corridas/salida-portfolio-setup.md`.

### Antes de seguir

Puedo correr ahora el portafolio completo. Como eres PMO y no hay equipo declarado, no ofrezco publicar el estándar en una carpeta compartida.