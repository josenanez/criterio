# /criterio-project:pm-setup documentos/proyectos/PRY-203-reposición-automática

## Listo — PRY-203 · Reposición automática

La configuración, la aceptación de términos y la ficha del proyecto quedaron escritas, y el cálculo salió sin problemas. Como esta sesión no tenía interfaz, tomé la respuesta sugerida en las cuatro preguntas y no hice ninguna.

**Lo que miré:** leí los 16 documentos de la carpeta, todos legibles. Hay 6 actas de comité semanal y unas notas del 2026-10-17 sueltas en la raíz; la última reunión es esa.
**Quién y cuándo:** la gerente es Laura Vélez y el patrocinador Carlos Peña, según el acta de constitución. El Comité de Expansión se reúne cada sábado. Las notas del 17 dicen que la próxima reunión es en dos semanas, así que anoté el 2026-10-31.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.4.0 (términos 1.1), el 2026-10-17. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-project-0.4.0-2026-10-17.md` y `.pdf`. La huella SHA-256 del `.md` empieza por `99704ec1070b83866591a7862f9b2f16…`.
**Lo que escribí:** la configuración en `.criterio/proyecto/PRY-203/config.json` y la ficha en `estado/PRY-203-reposición-automática/records/PRY-203.json`. No la sellé, como pide el comando.

### Compromisos: 26 en total
Hay 4 cumplidos con acta y 22 abiertos. De los abiertos, 8 están vencidos, 3 no tienen fecha y 11 tienen fecha por delante.

**Reprogramados 3 o más veces**

| Quién | Qué | Fecha vigente | Veces movido |
|---|---|---|---|
| Natalia Ospina | Enviar el documento 1 | 2026-12-18 | 6 (la primera promesa fue 2026-09-28) |
| Laura Vélez | Cerrar la prueba 2 | 2026-11-24 | 5 (la primera fue 2026-09-18) |
| Jorge Medina | Revisar el anexo 11 | 2026-11-20 | 3 (la primera fue 2026-10-01) |

Ninguna minuta sola muestra esto; sale de leerlas en orden.

**Vencidos sin acta**
- Carlos Peña, Validar el ambiente 4: 22 días.
- Liliana Torres, Confirmar la fecha 15: 18 días.
- Laura Vélez, Cerrar la prueba 10: 14 días.
- Ricardo Salas, Enviar el documento 17: 11 días.
- Natalia Ospina, Revisar el anexo 3: 7 días.
- María Restrepo, Aprobar el diseño 13: 6 días.
- Camilo Beltrán, Actualizar la matriz 14: 6 días.
- Elena Duarte, Entregar el punto 16: 2 días.

Carlos Peña, Natalia Ospina y Camilo Beltrán dijeron en la reunión que ya lo habían entregado, pero no hay acta, así que no los di por cerrados.

**Sin fecha** (nadie los fechó, por eso no aparecen como vencidos):
- Jorge Medina, Confirmar la fecha 7.
- Gustavo Neira, Validar el ambiente 12.
- Laura Vélez, Mandar el ajuste del presupuesto («la otra semana»).

### Otras señales
- **Estado declarado:** el informe del 2026-10-15 dice verde, 92 %. El cálculo no lo sustenta: quedan 7 tipos de señal sin explicar. El estado lo declaras tú; esto es contra qué.
- **Plazo:** el hito «Despliegue en la cadena» vencía el 2026-10-09 y sigue en curso, con 8 días de atraso.
- **Hitos sin acta:** 4 de 5 hitos figuran cerrados en el cronograma, pero ninguna acta de recibo los prueba.
- **Costo:** la proyección al cierre es 19,4 % mayor que el presupuesto aprobado.
- **Proveedor (contrato CT-338):** 3 de 4 entregables siguen pendientes y vencidos. El «Soporte del primer trimestre» figura recibido en el contrato, pero sin acta. La factura FV-1338 supera en 22.377.121 COP lo aceptado.
- **Riesgo sin anotar:** en la reunión del 17 se dijo que el proveedor podría no llegar con el equipo completo. Lo dejé en la ficha como riesgo, sin dueño.

### Qué le falta a tu carpeta
- Actas de recibo de los 4 hitos cerrados y del «Soporte del primer trimestre».
- Un cronograma posterior al v1 de 2025-07-06. Hoy no se ve ninguna replanificación, aunque el cierre ya pasó.
- La facultad del gerente: hasta qué monto y qué cambio decide sin subir a comité. No está en el acta.
- La etapa del proyecto, que ningún documento declara.
- Las notas del 17, que están en la raíz de la carpeta y no en `30-reuniones` con el nombre `AAAA-MM-DD-comite-semanal.md`.

**Cuándo vuelvo:** cada sábado, el día de tu comité; la próxima vez, el 2026-10-31.

La corrida quedó registrada como `2026-10-17-pm-setup-1`. La salida completa está en `estado/PRY-203-reposición-automática/corridas/salida-pm-setup.md`.