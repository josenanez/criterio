# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio de minería

**Miré:** 95 documentos en 13 proyectos (PRY-199 a PRY-211). Los formatos son .md (45), .docx (16), .pdf (14), .xlsx (13), .csv (5), .json (1) y .txt (1). El más reciente es del 2026-10-17.

**Eres:** PMO del portafolio, porque hay varios proyectos.

**Te aviso:** dos días antes del comité. Los comités son semanales y el último fue el 2026-10-16, así que asumí el próximo el 2026-10-23. Esa fecha no está confirmada.

**En:** presentación, por defecto.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.13 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.13-2026-10-17.md` y `.pdf`. Su SHA-256 empieza por `6d4b67767ea3a1ea…`.

Nadie podía responder preguntas, así que tomé la respuesta sugerida en cada una. El estado quedó en `estado/` y los informes irán a `reportes/`. El costo por corrida usa los valores seguros: lotes de diez proyectos, hasta 400 documentos.

### Probé con tres proyectos

Fueron los de documentación más reciente. Las fichas están en `estado/records/`.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-202 Planta de tratamiento de agua | 20 | Gerente Jorge Medina, patrocinadora Laura Vélez. Declara verde y 89%. Cierre 2027-09-20 tras CC-01 (+115 días). Hay 26 compromisos de comité. | Facultad del gerente, fase, y actas de recibo de los dos hitos cerrados y de los entregables del proveedor. |
| PRY-203 Despacho automático de flota | 4 | Gerente Sandra Gil, patrocinadora Liliana Torres. Declara amarillo y 27%. Cierre original 2026-09-17. | Facultad del gerente, fase, y acta de recibo de los cinco hitos. |
| PRY-205 Sistema de gestión de seguridad | 8 | Gerente Diana Molina, patrocinador Ricardo Salas. Declara verde y 23%. Cierre 2027-04-07 (original 2027-01-22). | Facultad del gerente, fase, y acta de recibo de Ingeniería básica. |

### Lo que levantó el cálculo

- **PRY-202:**
  - Declara verde, pero el avance de 89% choca con el cronograma, que sostiene entre 40% y 60%.
  - Los dos hitos cerrados no tienen acta.
  - La desviación en tiempo es de 115 días y la proyección supera lo aprobado en 28,9%.
  - Hay cinco compromisos vencidos, y tres de ellos se dijeron entregados en comité sin acta.
  - «Enviar el documento 1» va en 6 reprogramaciones.
  - Dos compromisos no tienen fecha.
  - El licenciamiento del proveedor lleva 124 días de atraso.
  - La bolsa de horas figura como recibida sin acta, y hay una factura de 63.399.928 COP del 2026-09-02. El contrato exige acta firmada para facturar.
- **PRY-203:** Declara 27%, pero los cinco hitos figuran cerrados, sin una sola acta de recibo. «Entregar el punto 31» salió del comité sin fecha.
- **PRY-205:**
  - Declara verde con 23%, aunque 3 de 4 hitos figuran cerrados.
  - El cronograma v2 movió el cierre 75 días, pero CC-01 sigue pendiente de presentación al comité: 0 días autorizados.
  - Ingeniería básica figura cerrada sin acta.

### El portafolio completo

Faltan 10 proyectos y unos 60 documentos por leer, en dos lotes. Estimo entre 30 y 45 minutos. Es una estimación a partir de estos tres, no una medición. La corrida de este comando tomó 171 segundos.

### Lo que le falta a tu carpeta

Ninguno de estos puntos bloquea nada:
- Las actas no dicen hasta dónde puede decidir el gerente ni en qué fase está el proyecto.
- El alcance es genérico («Componente 1, 2, 3»), así que no se puede contrastar con nada.
- Hay hitos «cerrados» sin acta de recibo en los tres proyectos.
- Las notas del 17-oct de PRY-202 están fuera de `30-reuniones/`. Una fecha viene como «08/12/2026» y la leí día/mes.
- CC-01 de PRY-202 dice «Autorizada por el comité», pero la minuta del 10-oct no la menciona.

Registré la corrida como `2026-10-17-portfolio-setup-1`. Lo mostrado queda completo en `estado/corridas/salida-portfolio-setup.md`.

¿Corro el portafolio completo? Si tienes equipo de gerentes, también puedo publicar el estándar en una carpeta compartida.