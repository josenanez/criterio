# /criterio-portfolio:health-check PRY-210

## Diagnóstico · PRY-210 Portal de proveedores · 2026-10-17

Leí 8 documentos, de 2025-05-21 a 2026-10-17, en formato `.docx` (1), `.md` (6) y `.csv` (1). Pude leerlos todos. El `.docx` lo leí por su conversión a texto en la caché. Ninguna otra carpeta menciona el proyecto. Los términos ya estaban vigentes: v1.1, aceptados por José Francisco Ñáñez el 2026-10-17.

**Dictamen:** de 18 afirmaciones evaluadas, 6 están sostenidas, 9 no tienen sustento y 3 están contradichas.

- **Gobierno:** el acta nombra patrocinador (Camilo Beltrán), gerente (Paula Céspedes) y Comité de Riesgos. No declara la autoridad del gerente. El alcance y las exclusiones son texto de plantilla, y las dependencias dicen "Ninguna declarada".
- **Plan:** el cronograma v1 está fechado 2025-05-21 pero ya trae los 5 hitos en "cerrado". Se editó después de aprobarse, así que no es una línea base de solo agregar. Marca "Salida a producción" cumplida el 2026-01-03. El acta de recibo es del 2026-10-12. El plan nunca se actualizó, y por eso `compute` da desviación 0 días: esa cifra refleja el archivo, no la realidad.
- **Avance:** el informe declara 73 % y el cronograma marca 5 de 5 hitos cerrados (100 %). Son 27 puntos de brecha, y el umbral es 10.
- **Hitos sin evidencia:** cuatro hitos cerrados no tienen ningún documento de respaldo: diseño funcional (461 días), ambiente de pruebas (418), integración (374) y piloto (331).
- **Proveedor (CT-100):** "Licenciamiento del motor" lleva 457 días vencido y "Mesa de ayuda" 313. "Bolsa de horas" figura como recibida pero no tiene acta. La factura de 413.260.638 COP cubre dos entregables y solo hay una acta.
- **Dinero:** el informe declara lo comprometido (1.938.815.478 COP) por debajo de lo ejecutado (2.270.104.627 COP), lo que no cuadra. El disponible real (2.261.184.522 COP) se calcula sobre lo comprometido, así que probablemente está sobrestimado. Ese gasto declarado no tiene documento detrás: solo hay 413.260.638 facturados.
- **Sin registrar:** la aprobación regulatoria que celebra el informe era una dependencia de hecho que el acta no declara. La rotación de un desarrollador clave y los dos riesgos del informe no tienen responsable. La minuta del 2026-10-15 asigna un compromiso a Jorge Medina ("el punto 3", para 2026-11-13) que no se puede verificar: el punto 3 no existe y Jorge Medina no figura entre los asistentes ni en otro documento.

Lo que la carpeta no permite saber:
- Si el proyecto está en producción y medido.
- Cuánto se atrasó de verdad.
- Cuánto dinero se gastó.
- Quién autorizó el atraso.
- Qué pasó entre 2025-11-01 y 2026-08-24, un tramo sin un solo documento.

No recomiendo detener, continuar ni reestructurar, porque eso lo decide quien tiene la facultad. Puedo preparar el punto de comité con lo que falta, o llevar las 3 contradicciones al gerente como preguntas, una por una. Como esta sesión no tiene interfaz, no ejecuté ninguna de las dos.

La corrida quedó registrada como `2026-10-17-health-check-1`, con el caso PRY-210. Duró 87 segundos y la salida completa está en `estado/corridas/salida-health-check.md`.

El registro de la corrida muestra 60 hallazgos en los 13 proyectos, no solo en PRY-210. Esa cuenta sale de `compute`, que mide todo el portafolio, y no cambia el diagnóstico de este proyecto.