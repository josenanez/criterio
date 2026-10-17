# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Portafolio retail

La instalación quedó lista y probé con tres proyectos. No hay informe ni portafolio completo todavía.

**Miré:** 89 documentos en 13 proyectos (PRY-199 a PRY-211). Formatos: .md 46, .docx 13, .xlsx 13, .pdf 10, .csv 5, .json 1, .txt 1. El más reciente es del 2026-10-17.
**Eres:** PMO del portafolio, porque hay varios proyectos.
**Te aviso:** dos días antes del comité del 2026-10-22, o sea el 2026-10-20. Las carpetas llaman "comité semanal" a sus reuniones, así que tomé cadencia semanal. La fecha del 22 es suposición mía; nadie la dijo.
**En:** presentación, que es el valor sugerido.
**Términos:** aceptados para la versión 0.3.13 (términos 1.1) por José Francisco Ñáñez, el 2026-10-17.
- El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.13-2026-10-17.md` y `.pdf`.
- SHA-256 del Markdown: 6d4b67767ea3a1ea…
- Registré el sí que venía en el argumento del comando.

**Dónde queda todo:**
- Configuración: `.criterio/portafolio/config.json`.
- Lo que voy encontrando: `estado/`.
- Informes: `reportes/`.

No hice ninguna pregunta, porque no había nadie que respondiera. La corrida mide 117 segundos, pero no medí los minutos hasta el primer resultado.

### Probé con tres proyectos

Cuatro proyectos empatan con documentación del 2026-10-17. Tomé PRY-200, PRY-204 y PRY-205.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-200 Tienda en línea | 14 | Gerente Rubén Cárdenas, patrocinador Jorge Medina. Declara **rojo, 69%**. Presupuesto 9.500 M COP, ejecutado 5.111 M, proyección 8.761 M. Cierre comprometido 2026-09-07. Extraje 26 compromisos de los comités y las notas. | Autoridad del gerente y fase. Ningún hito tiene acta de recibo. Un riesgo (el proveedor podría no llegar con el equipo completo) solo está en las notas y nadie lo registró. |
| PRY-204 Cajas de autopago | 3 | Gerente Liliana Torres, patrocinadora Natalia Ospina. Declara **amarillo, 41%**. Presupuesto 18.000 M, proyección 17.572 M. Cierre comprometido 2026-10-04. CC-01 pide +35 días y +70 M, y figura "autorizada por el comité". | No hay cronograma, hitos, actas de comité ni autoridad del gerente. El informe dice que el despliegue se reprogramó, pero ningún documento da la fecha nueva. |
| PRY-205 Pago con QR en caja | 6 | Gerente Jorge Medina, patrocinadora Liliana Torres. Declara **amarillo, 30%**. Presupuesto 1.200 M, proyección 1.466 M. El cronograma v2 mueve el cierre del 2026-09-15 al 2026-12-31. CC-01 pide +107 días y +214 M, y sigue pendiente de comité. | Autoridad del gerente y fase. Ningún hito tiene acta de recibo. |

### Lo que levantó el cálculo

El cálculo levantó 28 señales. Solo presento estas:

**PRY-200 (21 señales)**
- Los 5 hitos están "cerrado" y no hay un solo acta de recibo (`milestone_met_without_evidence`). El último, Despliegue en la cadena, vencía el 2026-09-07, hace 40 días.
- Declara 69% de avance con 5 de 5 hitos cerrados, una brecha de 31 puntos (`progress_vs_plan`).
- 9 compromisos vencidos (`commitment_overdue`). Por ejemplo, Natalia Ospina dice que ya entregó "Aprobar el diseño 5", venció el 2026-09-30 y no presentó acta.
- 3 compromisos reprogramados muchas veces (`commitment_rescheduled`):
  - "Enviar el documento 1" (Beatriz Cuéllar): 6 veces, del 2026-09-28 al 2026-12-19.
  - "Cerrar la prueba 2" (Óscar Ramírez): 5 veces.
  - "Revisar el anexo 3" (Camilo Beltrán): 3 veces.
- 3 compromisos sin fecha (`commitment_undated`): "Cerrar la prueba 10", "Revisar el anexo 11" y "Mandar el ajuste del presupuesto".

**PRY-204 (1 señal)**
- CC-01 figura autorizada y la línea base no se movió (`change_without_baseline`). Ningún documento trae la fecha nueva.

**PRY-205 (6 señales)**
- El cronograma v2 mueve el cierre 107 días y el cambio que lo justifica está pendiente de comité (`rebaseline_unauthorized`).
- El atraso es de 107 días contra la original, 51,7 % (`variance_time`).
- La proyección supera lo aprobado en 22,2 % (`variance_cost`).
- Declara 30% con 3 de 3 hitos cerrados, una brecha de 70 puntos (`progress_vs_plan`).
- Dos hitos "cerrado" sin acta (`milestone_met_without_evidence`): Diseño de la experiencia aprobado y Ambiente de pruebas certificado.

Los tres proyectos tienen la autoridad del gerente sin documentar. La ficha que publicó el gerente de PRY-200 (`ficha-pm.json`) no contradice mi lectura.

### El portafolio completo
Faltan 10 proyectos (PRY-199, 201, 202, 203 y 206 a 211) y 66 documentos, en dos lotes uno tras otro. Calculo entre 30 y 40 minutos de lectura. Es una estimación mía, no una medida.

### Lo que le falta a tu carpeta
Ninguno de estos puntos bloquea nada:
- **Autoridad del gerente:** ninguna acta trae hasta qué monto o cambio decide sin subir a comité. Sin eso no puedo decir si un cambio la excede.
- **Alcance:** las actas lo describen como "Componente 1, 2, 3". Sin alcance real no hay contra qué medir un cambio de alcance.
- **Reuniones y cronograma:** PRY-204 no tiene cronograma. PRY-203, PRY-204, PRY-206 y PRY-209 no tienen carpeta de reuniones.
- **Actas de recibo:** los hitos se marcan cerrados sin acta en los tres proyectos.
- **Cambios y líneas base:** PRY-204 tiene un cambio autorizado sin línea base nueva. PRY-205 publicó un cronograma v2 antes de que el comité aprobara el cambio.
- **Notas sueltas:** las notas de reunión de PRY-200 del 2026-10-17 están en la raíz del proyecto, no en `30-reuniones/`.
- **Carpeta ajena:** en `estado/` apareció una carpeta `PRY-200-tienda-en-línea/` que no creé yo y que no usé. Conviene revisar quién la dejó.

¿Corro el portafolio completo? Si tienes equipo de gerentes de proyecto, también puedo publicar el estándar en una carpeta compartida para que usen los mismos criterios.

La corrida quedó registrada en `estado/corridas/2026-10-17-portfolio-setup-1.md`. Esta salida está en `estado/corridas/salida-portfolio-setup.md`.