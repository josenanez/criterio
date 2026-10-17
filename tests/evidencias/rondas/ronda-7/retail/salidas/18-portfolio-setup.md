# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio retail

**Miré:** 80 documentos en 13 proyectos (PRY-199 a PRY-211). Formatos: .md, .docx, .pdf, .xlsx, .csv, .json y .txt, todos legibles. El más reciente es del 2026-10-17.
**Eres:** PMO del portafolio (la respuesta sugerida, porque hay varios proyectos).
**Te aviso:** cada semana, dos días antes del comité. Las carpetas traen actas de «comité semanal», así que tomé semanal. No tengo la fecha del próximo comité.
**En:** página HTML. La respuesta sugerida era presentación, pero es el único formato que la configuración reconoce hoy. Si prefieres presentación o PDF, dímelo y lo cambio.
**Términos:** aceptados para la versión 0.3.13 (términos 1.1) por José Francisco Ñáñez, 2026-10-17. Comprobante en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.13-2026-10-17.md` y `.pdf`. SHA-256 `6d4b67767ea3a1ea…`

No hice ninguna pregunta: la sesión era sin interfaz y tomé la respuesta sugerida en cada una. La configuración está en `.criterio/portafolio/config.json` y la verificación dio ok. Lo que se vaya encontrando va en `estado/` y los informes irán en `reportes/`.

### Probé con tres proyectos

Tomé los tres con documentación del 2026-10-17: PRY-202, PRY-204 y PRY-211. Leí 30 documentos y dejé las fichas en `estado/records/`. `compute` levantó 37 señales.

| Proyecto | Qué declara | Qué levantó `compute` |
|---|---|---|
| PRY-202 Centro de distribución norte | Rojo, 26% | Declara 26% y el cronograma sustenta entre 67% y 100%. Dos hitos figuran cerrados sin acta. La proyección supera el presupuesto en 26,2%. |
| PRY-204 Cajas de autopago | Verde, 58% | El verde queda contradicho por cuatro señales. Los 4 hitos figuran cumplidos y el cierre del 2026-08-26 ya pasó. Dos hitos (integración con el ERP y piloto) no tienen acta. La proyección supera lo aprobado en 10,8%. Un compromiso venció el 2026-10-13 y otro no tiene fecha. |
| PRY-211 Pronóstico de demanda | Verde, 49% | El verde queda contradicho por ocho señales (ver abajo). |

En PRY-211 las ocho señales son:
- Tres hitos cerrados sin acta.
- La proyección supera lo aprobado en 26,9%.
- Siete compromisos vencidos.
- Cinco compromisos reprogramados tres veces o más. El de Javier Hoyos va en seis, del 2026-09-09 al 2026-12-03.
- Dos compromisos de Laura Vélez sin fecha.
- Cuatro entregables de proveedor atrasados.
- CT-842 está facturado 422.462.954 COP por encima de lo recibido.
- CT-565 está facturado por 723.840.453 COP sin ningún entregable recibido.

La ficha que el gerente de PRY-211 publicó (`ficha-pm.json`) quedó aparte, entera, en `pm_record`. No la mezclé con mi lectura.

### El portafolio completo

Faltan 10 proyectos y 50 documentos, en un lote, uno tras otro. Las tres fichas tomaron unos 171 segundos de corrida según el script. No lo extrapolo: PRY-211 fue 20 de los 30 documentos leídos y los pendientes traen de 2 a 7 cada uno.

### Lo que le falta a tu carpeta

Nada de esto bloquea el análisis:
- **Facultad del gerente:** ningún proyecto declara qué puede decidir sin subir a comité.
- **Actas de recibo:** hay hitos «cerrado» sin acta en 202, 204 y 211.
- **Cronogramas v2:** 204 y 211 dicen que reprogramaron el despliegue y solo existe la v1.
- **Alcances:** dicen «Componente 1, 2 y 3» sin nombre, y las exclusiones son «lo que otro proyecto cubre».
- **Dependencias:** las tres actas leídas dicen «Ninguna declarada».
- **Riesgo sin dueño:** las notas del 2026-10-17 de PRY-211 mencionan un riesgo del proveedor que nadie anotó.

### Dos correcciones

- La nota de la corrida registrada dice que no medí el tiempo. El script sí lo midió: 171 s. Dejé corregido el texto en `estado/corridas/salida-portfolio-setup.md`, pero la nota ya registrada la dejé como está para no duplicar la corrida.
- Cambié de carpeta con `cd` dos veces por descuido, contra la regla de no usarlo. Volví a la raíz de la sesión las dos veces y no afectó ningún resultado.

### Qué sigue

¿Corro el portafolio completo? Si tienes gerentes con equipo propio, puedo publicar el estándar en una carpeta compartida para que usen los mismos criterios; hoy no lo hice.

Corrida registrada: `2026-10-17-portfolio-setup-1`.