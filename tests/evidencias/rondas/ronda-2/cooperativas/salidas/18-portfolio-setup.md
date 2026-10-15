# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Cooperativa

**Miré:** 71 documentos en 13 proyectos. Formatos: .md 31, .pdf 14, .docx 11, .xlsx 9, .csv 4, .json 1, .txt 1. El más reciente es del 2026-10-15.
**Eres:** PMO del portafolio. Es lo sugerido porque hay varios proyectos.
**Te aviso:** dos días antes del comité. Tomé lo sugerido: comité semanal, el próximo el 2026-10-22, así que el informe llega el 2026-10-20.
**En:** presentación, que es lo sugerido.
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-15 para la versión 0.3.8 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.8-2026-10-15.md` y `.pdf`. SHA-256: 906ca52cb3296d17…

La configuración está en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes irán a `reportes/`. No hice ninguna pregunta: tomé la respuesta sugerida en cada una, como pediste.

### Probé con tres proyectos
Fueron PRY-201, PRY-203 y PRY-210, los de documentación más reciente. Leí 19 documentos y el cálculo levantó 25 señales.

| Proyecto | Qué supe | Qué no está |
|---|---|---|
| PRY-201 Apertura de ahorro en línea | Declara **verde, 47 %** (corte 2026-09-24). Aprobado 1.200 M COP, comprometido 428 M, ejecutado 295 M. Contrato CT-683 con Soluciones Solidarias. | Autoridad del gerente, fase |
| PRY-203 Aportes sociales en línea | Declara **rojo, 34 %** (corte 2026-10-14). Aprobado 4.200 M, comprometido 2.705 M, ejecutado 1.996 M. Cierre comprometido hoy, 2026-10-15. Su gerente publicó una ficha propia, que guardé aparte. | Autoridad, fase |
| PRY-210 Corresponsales rurales | Declara **rojo, 35 %** (corte 2026-10-06). Proyección al cierre 4.219 M contra 4.200 M aprobados. Tiene dos ampliaciones de alcance autorizadas: CC-01 (+76 días, 152 M) y CC-02 (+101 días, 202 M). | Producto («No aplica»), autoridad, fase, quién autorizó los cambios |

### Hallazgos
**PRY-201 (11 señales): el verde no se sostiene.**
- Declara 47 % de avance, pero el cronograma tiene los 5 hitos cerrados, y ninguno tiene acta de recibo.
- Dos entregables del proveedor están vencidos y sin recibo: el licenciamiento, desde el 2026-02-12, y la bolsa de horas, desde el 2026-05-11.
- Hay una factura de 121.861.832 COP radicada el 2026-09-06 con ambos entregables sin recibo.
- Carlos Peña tenía "Entregar el punto 12" para el 2026-09-27 y está vencido hace 18 días.

**PRY-203 (8 señales):**
- Declara 34 % con los 4 hitos cerrados, sin acta para ninguno.
- La fecha de cierre no coincide: el cronograma dice 2026-09-03 y la ficha del gerente dice 2026-10-15.
- Un compromiso de Carlos Peña venció el 2026-10-11, y otro de Laura Vélez ("la otra semana") no tiene fecha.
- En las notas del 2026-10-15 se comentó que el proveedor podría no llegar con el equipo completo. Nadie lo anotó como riesgo y quedó sin dueño.

**PRY-210 (6 señales):**
- Lleva 177 días (74,1 %) de desviación contra la línea base original.
- CC-02 no tiene línea base nueva.
- Declara 35 % de avance, y el plan sustenta entre 67 % y 100 %.
- Los dos hitos cerrados no tienen acta, y un compromiso de Rubén Cárdenas está vencido desde el 2026-10-07.

Ninguno de los tres define la autoridad del gerente.

### El portafolio completo
Faltan 10 proyectos y 52 documentos: PRY-199, 200, 202, 204 al 209 y 211. Calculo entre 25 y 35 minutos, en un solo lote de diez, uno tras otro. Es una estimación mía: la corrida de hoy tardó 104 segundos en total.

### Lo que le falta a tu carpeta
Ninguno de estos puntos bloquea nada:
- No hay actas de recibo en estos tres proyectos, así que los hitos "cerrados" no se pueden probar. PRY-199, 200 y 202 sí traen alguna.
- Las actas de constitución no dicen hasta dónde puede decidir el gerente sin subir a comité.
- El alcance de las actas dice "Componente 1, 2, 3", sin nada concreto contra qué medir.
- Las notas de reunión de PRY-203 están sueltas en la raíz del proyecto, no en `30-reuniones/`.
- PRY-210 no dice quién autorizó los cambios, solo "el comité".

### Qué sigue
¿Corro el portafolio completo? Si tienes equipo de gerentes de proyecto, también puedo publicar el estándar en una carpeta compartida para que usen los mismos criterios.

Lo que mostré arriba quedó en `estado/corridas/salida-portfolio-setup.md`. La corrida quedó registrada como `2026-10-15-portfolio-setup-1`.