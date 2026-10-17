# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Cooperativa

Instalé el agente sobre `documentos/proyectos`. Probé con tres proyectos, y los tres tienen señales. No hubo preguntas: tomé las respuestas sugeridas y las dije.

**Miré:** 89 documentos en 13 proyectos (PRY-199 a PRY-211). Formatos: .md 38, .docx 17, .pdf 17, .xlsx 8, .csv 7, .json 1, .txt 1. El más reciente es del 2026-10-17.

**Eres:** PMO del portafolio.

**Te aviso:** dos días antes del comité. Puse comité semanal, con el próximo el 2026-10-24, porque ese es el ritmo de las minutas de la carpeta.

**En:** presentación.

**Términos:** aceptados por José Francisco Ñáñez para la versión 0.3.13 (términos 1.1). Los mostré tal cual y tomé el sí y el nombre de tu argumento de esta prueba. El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.13-2026-10-17.md` y `.pdf`. SHA-256: 6d4b67767ea3a1ea…

También tomé por ti estas decisiones: sin destinatarios, y estado e informes junto a tus documentos, en `estado/` y `reportes/`.

### Probé con tres proyectos

Son los de documentación más reciente. Las fichas están en `estado/records/`.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-200 Crédito de libranza digital | 22 | Gerente Rubén Cárdenas y patrocinador Jorge Medina, según el acta de 2025-06-26. Declara **rojo, 28%**. Aprobado 2.400 M COP, comprometido 1.398 M, ejecutado 929 M, proyección 2.645 M. Cierre aprobado: 2026-01-08. Tiene 25 compromisos en 7 reuniones. El gerente publicó su propia ficha; la guardé aparte. | Facultad del gerente, fase |
| PRY-207 Microcrédito rural | 4 | Gerente Paula Céspedes y patrocinador Óscar Ramírez. Declara **amarillo, 37%**. Aprobado 1.200 M, comprometido 531 M, ejecutado 527 M, proyección 1.121 M. Cierre: 2027-09-11. | Facultad del gerente, fase |
| PRY-210 Corresponsales rurales | 4 | Gerente Mauricio Pérez y patrocinador Rubén Cárdenas. Declara **verde, 73%**. Aprobado 3.300 M, comprometido 2.429 M, ejecutado 1.479 M, proyección 3.154 M. Cierre aprobado: 2026-09-06. | Producto (el acta dice «No aplica»), facultad del gerente, fase |

### Lo que levantó el cálculo (19 señales)

**PRY-210: el verde no se sostiene.**
- El cronograma declara cerrados sus 3 hitos, pero no hay ni un acta de recibo.
- Con 3 de 3 hitos cerrados el plan sustenta 100%, y el informe dice 73%.
- La fecha de cierre aprobada, 2026-09-06, ya pasó.

**PRY-200: rojo, y los documentos lo respaldan.**
- Declara 28% contra 4 de 4 hitos cerrados. Dos de esos hitos no tienen acta: Ambiente de pruebas certificado e Integración con el core cooperativo.
- La proyección supera lo aprobado en 10,2 %.
- Hay 4 compromisos vencidos:
  - Paula Céspedes, «Confirmar la fecha 7» (7 días). Dijo que ya lo entregó, pero no hay acta.
  - Felipe Arango, «Enviar el documento 17» (10 días).
  - Laura Vélez, «Cerrar la prueba 18» (9 días).
  - Carlos Peña, «Actualizar la matriz 22» (1 día).
- Dos compromisos no tienen fecha: «Validar el ambiente 12» (Javier Hoyos) y «Mandar el ajuste del presupuesto» (Laura Vélez).
- Dos compromisos se reprogramaron muchas veces: Gustavo Neira, «Enviar el documento 1», 6 veces; Sandra Gil, «Cerrar la prueba 2», 5 veces. Eso es un bloqueo que nadie ha nombrado.

**PRY-207: amarillo con dos señales.** El hito Diseño funcional aprobado venció el 2026-10-05 sin acta. El compromiso de Diana Molina vencía el 2026-10-16, un día antes de la reunión donde quedó registrado.

No levantó cambios de gobierno, contradicciones entre documentos ni proyectos en silencio. Tampoco encontró diferencias entre la ficha del gerente de PRY-200 y mi lectura.

### El portafolio completo

Faltan 10 proyectos (PRY-199, 201 a 206, 208, 209 y 211) y 59 documentos, en 2 lotes uno tras otro. Calculo entre 30 y 45 minutos de conversación; es una estimación, no una medida. La corrida de este ensayo midió 116 segundos, pero solo contando desde que arrancó el cálculo. La siguiente corrida releerá solo lo que cambie.

### Lo que le falta a tu carpeta

Ninguno de estos puntos bloquea nada.
- **Facultad del gerente:** ningún acta dice hasta dónde puede decidir sin subir a comité (3 de 3). Sin eso, el control de cambios no sabe si algo la excede.
- **Datos viejos:** en PRY-200 y PRY-210, patrocinador, gerente, alcance y presupuesto vienen de actas de hace 16 y 17 meses, y nadie los ha reconfirmado.
- **Línea base:** PRY-200 no tiene una nueva, aunque su cierre aprobado fue el 2026-01-08 y sus compromisos llegan a diciembre.
- **Hitos cerrados sin acta de recibo:** 2 en PRY-200 y 3 en PRY-210. Que aparezcan esas actas es lo que más mejoraría el análisis.
- **Alcance:** en los tres proyectos es «Componente 1, 2, 3», sin descripción.
- **Notas de PRY-200:** las del 2026-10-17 están en la raíz del proyecto, fuera de `30-reuniones/`. El compromiso de Gustavo Neira trae la fecha como «04/12/2026» y la leí como 4 de diciembre.
- **Ficha del gerente:** solo PRY-200 tiene una.

### Siguiente paso

¿Corro el portafolio completo? Como eres PMO y tienes equipo, también puedo publicar el estándar en una carpeta compartida para que tus gerentes usen los mismos criterios.

La salida quedó en `estado/corridas/salida-portfolio-setup.md`. La corrida quedó registrada como `2026-10-17-portfolio-setup-1`.