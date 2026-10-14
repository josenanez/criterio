# /criterio-portfolio:portfolio-scan 

Terminé el barrido: leí 45 de los 69 documentos y escribí las fichas de 10 proyectos. Los otros 24 no habían cambiado por hash y no los abrí.

**Documentos y proyectos**
- **Documentos:** 69 en la carpeta, 45 leídos, 24 sin cambio y 0 ilegibles. Era un lote único de 10 proyectos, uno tras otro, y no quedó nada diferido.
- **Proyectos:** hay 13 con ficha. Las fichas nuevas son PRY-199, 200, 201, 202, 204, 205, 206, 209, 210 y 211. PRY-203, 207 y 208 quedaron como estaban.
- **Sellado y registro:** sellé las 10 fichas con los hashes que calculó el script (los 45 documentos leídos quedaron registrados en `documents_seen`). Después corrí `snapshot` y `corrida`.
- **Términos:** la configuración ya traía los términos v1.0 aceptados por José Francisco Ñáñez el 2026-10-14, y coinciden con la versión de `TERMS.md`.

**Señales del script**
Dio 39 hallazgos en todo el portafolio. Estos son los que más pesan:
- **PRY-210:** CC-01 aprobó +91 días y +182.000.000 COP, pero no dice qué comité la autorizó y ningún acta de comité la recoge. Además, el cronograma v2 mueve las pruebas a 2027-12-17, después del cierre del acta (2027-11-09), y el presupuesto sigue en 9.500.000.000.
- **PRY-206:** la factura FV-1353 es de 177.240.348 COP, y los tres entregables del contrato suman 167.002.149. Solo hay dos actas de recibo, y la segunda es posterior a la factura.
- **PRY-211:** la factura FV-1263 es de 1.143.205.796 COP. El contrato da por recibido el Licenciamiento del software, pero no hay acta de recibo. La Bolsa de horas ya debía haberse entregado (vencía el 2026-09-09).
- **PRY-205:** la fecha de cierre pasó (2026-08-01), con 72% de avance y estado verde.
- **PRY-200:** reporta ejecutado por encima de lo comprometido.
- **PRY-209:** proyecta 18.540.943.448 COP sobre 18.000.000.000 aprobados.
- **Hitos:** 16 hitos figuran como cerrados sin acta que lo pruebe en todo el portafolio, contando los de las fichas que no toqué.
- **Compromisos vencidos:** 3, uno de ellos en PRY-210 (punto 35, vencía el 2026-10-09).

**Campos sin dato**
- **Todas las fichas:** la autoridad del gerente y la fase no aparecen en ninguna de las 10 actas.
- **Sin cronograma:** PRY-201, 204 y 205 no tienen hitos.
- **Facturado:** no hay dato en PRY-199.

**Nada movido y un aviso**
- **Movidos:** nada. No existe la carpeta `entrada/`.
- **Pendiente de clasificar:** en PRY-208, la `ficha-pm.json` cita sus documentos con rutas relativas a la carpeta del proyecto, y por eso 12 campos aparecen como cita que no resuelve. Los documentos sí existen. Lo dejé sin tocar porque esa ficha es del gerente.

Todo está en `estado/portafolio/corridas/salida-portfolio-scan.md`.

Si quieres seguir, puedo generar el informe consolidado con `/criterio-portfolio:portfolio-report`.