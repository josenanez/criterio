# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Banco Ejemplo

La instalación quedó hecha, y probé con PRY-203, PRY-209 y PRY-210.

**Qué miré:** 77 documentos en 13 proyectos (PRY-199 a PRY-211), el más reciente del 2026-10-18.

**Configuración**
- **Rol:** PMO del portafolio.
- **Aviso:** dos días antes de cada comité, que tomé semanal. El próximo lo puse el 2026-10-25, es una suposición mía y conviene corregirla si no es esa.
- **Informes:** en presentación.
- **Dónde queda todo:** `.criterio/portafolio/config.json`. Lo que Vera va encontrando va en `estado/` y los informes irán a `reportes/`.
- **Términos:** José Francisco Ñáñez los aceptó para la versión 0.5.0 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.5.0-2026-10-18.md` y `.pdf`, SHA-256 `9c54c0c51760b166…`.
- **Preguntas hechas:** ninguna, tomé las respuestas sugeridas.

**Qué levantó `compute`**
- **PRY-203 Open Banking:** ninguna señal. No tiene cronograma, y su cierre comprometido (2026-08-10) ya pasó.
- **PRY-209 Nómina electrónica (5 señales):**
  - Declara 37 % de avance con los cuatro hitos cerrados, una diferencia de 63 puntos.
  - Tres hitos figuran cerrados sin acta de recibo.
  - La proyección supera el presupuesto aprobado en 20,3 %.
- **PRY-210 Portal de proveedores (9 señales):**
  - **Cronograma:** la salida a producción se movió 102 días (+21,2 %) sin autorización. La solicitud de cambio CC-01 sigue pendiente de presentación al comité.
  - **Hitos:** el Piloto con usuarios internos lleva 8 días vencido y dos hitos cerrados no tienen acta.
  - **Avance y costo:** declara 48 % cuando el plan sostiene entre 60 % y 80 %, y la proyección supera el aprobado en 18,1 %.
  - **Proveedor:** dos entregables de Integra Sistemas llevan 181 y 75 días de atraso.

**El portafolio completo.** Faltan 10 proyectos y 74 documentos, y calculo entre 30 y 40 minutos. Es una estimación mía, no la medí.

**Lo que le falta a tu carpeta**
- Ningún gerente declara su autoridad de decisión.
- En PRY-210 el patrocinador y el gerente son la misma persona.
- Dos compromisos tienen un responsable que no aparece entre los asistentes del acta.
- Dejé sin tocar `estado/PRY-201-core-de-depósitos/`, que pertenece al agente de proyecto.

La corrida quedó registrada como `2026-10-18-portfolio-setup-1`. El texto completo está en `estado/corridas/salida-portfolio-setup.md`.

¿Corro el portafolio completo? No hay equipo declarado, así que no ofrezco publicar un estándar compartido por ahora.