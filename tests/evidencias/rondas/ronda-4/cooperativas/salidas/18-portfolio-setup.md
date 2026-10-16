# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Cooperativa

Dejé la instalación hecha y probé con tres proyectos. `compute` levantó 28 señales sobre ellos.

**Miré:** 82 documentos en 13 proyectos. Hay .md (35), .pdf (18), .docx (16), .xlsx (7), .csv (4), .json (1) y .txt (1). El más reciente es del 2026-10-15.
**Eres:** PMO del portafolio. Tomé la respuesta sugerida porque hay varios proyectos.
**Te aviso:** dos días antes del comité del 2026-10-22. Los comités se llaman «semanales», así que tomé esa cadencia.
**En:** presentación, la respuesta sugerida.
**Términos:** aceptados por José Francisco Ñáñez para la versión 0.3.10 (términos 1.1), fecha 2026-10-15. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.10-2026-10-15.md` y `.pdf`. SHA-256: `5a63e87d0ce9d540…`.

No hice preguntas, porque la sesión no tiene interfaz. Cada respuesta salió del valor sugerido. No medí con reloj el tiempo hasta el primer resultado; el script registró 151 segundos de cómputo.

La configuración quedó en `.criterio/portafolio/config.json`. Lo que Vera va encontrando está en `estado`, y los informes irán a `reportes`.

### Probé con tres proyectos
Cuatro proyectos empataban con documentos del 2026-10-15 (PRY-203, 207, 209 y 211). Tomé PRY-203, PRY-207 y PRY-211, que tienen más documentos. Las fichas quedaron en `estado/records/` y selladas.

| Proyecto | Docs | Qué supe | Qué no está |
|---|---|---|---|
| PRY-207 Microcrédito rural | 9 | Gerente Laura Vélez y patrocinador Óscar Ramírez. Presupuesto de 4.200 M COP y cierre comprometido para 2026-05-25. Declara amarillo y 74 %. El contrato CT-315 tiene 3 entregables, 2 recibidos con acta. | Facultad del gerente, etapa |
| PRY-211 Cobranza digital | 7 | Gerente Beatriz Cuéllar y patrocinador Camilo Beltrán. Presupuesto de 9.500 M COP y cierre 2027-06-03. Declara rojo y 44 %. El contrato CT-884 tiene 4 entregables de 513.489.020 COP cada uno. | Facultad del gerente, etapa |
| PRY-203 Aportes sociales | 19 | Gerente Ricardo Salas y patrocinadora Elena Duarte. Presupuesto de 2.400 M COP y cierre 2027-05-30. Declara amarillo y 44 %. La solicitud de cambio CC-01 sigue pendiente. Trae una `ficha-pm.json` del gerente, que guardé aparte en `pm_record`. Tiene 26 compromisos. | Facultad del gerente, etapa, proveedores |

### Hallazgos
Todos salen de `compute`.

**PRY-211**
- **Facturado sin entrega:** hay una factura de 513.489.020 COP contra CT-884, y ninguno de sus 4 entregables tiene acta de recibo. El único acta del proyecto es la del ambiente de pruebas, que es un hito, no un entregable del contrato.
- **Entregables atrasados:** licenciamiento 247 días, bolsa de horas 128 días y parametrización 8 días.
- **Sobrecosto proyectado:** +17,3 % sobre lo aprobado.
- **Avance:** declara 44 % y el plan sustenta entre 60 y 80 %.
- **Hitos sin acta:** Diseño funcional e Integración con el core están cerrados sin acta que lo pruebe.

**PRY-207**
- **Hitos sin acta:** Ambiente de pruebas, Integración con el core, Piloto y Salida a producción figuran cerrados. Llevan entre 170 y 327 días desde su fecha y ninguno tiene acta.
- **Avance:** declara 74 % y el plan supone 100 %.
- **Entregable atrasado:** Parametrización de líneas de crédito, 216 días.
- **Compromiso vencido:** Gustavo Neira, «Entregar el punto 4», para el 2026-10-14.

**PRY-203**
- **Línea base movida sin autorización:** +115 días en la integración con el core, de 2027-03-13 a 2027-07-06. CC-01 sigue sin decidir.
- **Contradicción entre fuentes:** la ficha del gerente dice cierre 2027-05-30 y el cronograma v2 llega a 2027-07-06.
- **Sobrecosto proyectado:** +18,1 %.
- **Hito vencido:** Ambiente de pruebas certificado, 5 días. Diseño funcional figura cerrado sin acta.
- **Compromisos reprogramados:** «Enviar el documento 1» seis veces y «Cerrar la prueba 2» cinco veces.
- **Compromisos vencidos:** Carlos Peña (6 días) y Felipe Arango (10 días).
- **Compromisos sin fecha:** tres.

### El portafolio completo
Quedan 10 proyectos y 47 documentos, en 2 lotes uno tras otro. Calculo entre 20 y 30 minutos de conversación, a partir de esta prueba; es una estimación, no una medición.

### Lo que le falta a tu carpeta
Ninguno de estos es bloqueante.
- Las tres actas de constitución no dicen hasta qué monto puede decidir el gerente sin subir a comité.
- Hay seis hitos cerrados en el cronograma sin acta de recibo: cuatro en PRY-207 y dos en PRY-211. Si las actas existen, no están en la carpeta.
- Los cronogramas de PRY-207 y PRY-211 siguen en la versión 1, aunque el cierre de PRY-207 pasó hace casi cinco meses.
- Las notas del 2026-10-15 de PRY-203 están sueltas en la raíz, no en `30-reuniones`. Traen una fecha ambigua («11/12/2026», que leí como 11 de diciembre) y una relativa («la otra semana»).
- Ninguno de los tres proyectos declara una etapa.

La carpeta `estado/PRY-203-aportes-sociales-en-línea/` viene de una sesión anterior del gerente de ese proyecto. No la toqué.

Sigue: correr el portafolio completo. Como PMO con equipo, también puedes publicar el estándar en una carpeta compartida para que los gerentes usen los mismos criterios.

La salida completa quedó en `estado/corridas/salida-portfolio-setup.md`, y la corrida se registró como `2026-10-15-portfolio-setup-1`.