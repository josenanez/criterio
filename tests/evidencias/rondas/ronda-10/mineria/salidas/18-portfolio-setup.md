# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de proyectos

La instalación quedó hecha y probé con tres proyectos. Nadie podía responder, así que tomé el valor sugerido en cada pregunta: eres PMO (hay 13 proyectos) y quieres el informe como página (HTML). Estado en `estado/`, informes en `reportes/`. Pongo el comité cada dos semanas con el próximo el 2026-10-29. Esa fecha la supuse, así que corrígela cuando me digas la real.

**Miré:** 80 documentos en 13 proyectos. Los formatos son .md (39), .docx (12), .pdf (12), .xlsx (9), .csv (6), .json (1) y .txt (1). El más reciente es del 2026-10-18.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.5.0 (términos 1.1). Los comprobantes están en `.criterio/terminos/aceptacion-criterio-portfolio-0.5.0-2026-10-18.md` y `.pdf`. El SHA-256 del `.md` empieza con `9c54c0c51760b166…`.

**Configuración:** la verifiqué y no dio problemas.

### Probé con tres proyectos

Tomé los de documentación más reciente. Los hallazgos son los que levantó el cálculo (`compute`).

| Proyecto | Qué supe | Qué no está |
|---|---|---|
| PRY-203 Despacho automático de flota | Presupuesto de 4.200 M COP, cierre el 2027-02-09. Declara verde con 37 %. | Autoridad del gerente, fase, proveedores |
| PRY-208 Trazabilidad del mineral | Presupuesto de 1.200 M COP. El cierre vigente es 2027-02-22; el acta decía 2027-01-27. Declara rojo con 78 %. | Autoridad del gerente, fase, proveedores |
| PRY-211 Control de polvo en vías | Presupuesto de 9.500 M COP, cierre el 2027-02-18. Declara amarillo con 39 %. | Producto («No aplica»), autoridad del gerente, fase, proveedores |

Salieron 9 señales:
- **PRY-203:** declara verde, pero con 2 de 4 hitos cerrados el plan sustenta entre 50 % y 75 %, y declara 37 %. La brecha es de 13 puntos.
- **PRY-208:** dos hitos están cerrados sin acta: ingeniería básica y licencia y permisos. Además, el cronograma v2 movió el cierre 26 días y la solicitud de cambio que lo respalda (CC-01) sigue pendiente de comité.
- **PRY-211:** tres hitos están cerrados sin acta. Declara 39 % cuando el plan sustenta entre 60 % y 80 %, una brecha de 21 puntos.
- **Los tres:** la autoridad del gerente no está declarada.

No releí los compromisos de las reuniones de PRY-203. Están en la ficha que publicó su gerente, que guardé entera.

### El portafolio completo

Faltan 10 proyectos y 65 documentos, en dos lotes uno tras otro. Esta corrida de tres proyectos tomó 73 segundos. Mi estimación para el resto es de unos pocos minutos por proyecto, así que del orden de media hora a una hora.

### Lo que le falta a tu carpeta

- **Autoridad del gerente:** ningún acta la trae, y sin ella el control de cambios no sabe qué puede decidir el gerente sin subir a comité.
- **Actas de recibo:** faltan las de 5 hitos que los cronogramas dan por cerrados. Si existen, súbelas con la fecha en el nombre.
- **PRY-211:** se apoya en un acta de hace 13 meses, sin confirmación posterior de patrocinador, gerente ni presupuesto.
- **Carpeta `estado/`:** ya tenía estado del agente de proyecto para PRY-203. Convive con el del portafolio, pero conviene decidir quién escribe qué.

Dejé la salida completa en `estado/corridas/salida-portfolio-setup.md` y la corrida registrada como `2026-10-18-portfolio-setup-1`. ¿Corro el portafolio completo?