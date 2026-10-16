# /criterio-project:pm-setup documentos/proyectos/PRY-205-sistema-de-gestión-de-seguridad

## Listo: PRY-205, Sistema de gestión de seguridad

Samuel quedó configurado para PRY-205 y leyó las siete reuniones en orden, de la más vieja a la más nueva. Salen 26 compromisos: 6 cerrados con acta de recibo y 20 abiertos.

Como la sesión era sin interfaz, tomé la respuesta sugerida en las preguntas:
- **Gerente:** Paula Céspedes, según el acta de constitución.
- **Reunión de seguimiento:** el comité semanal de los viernes. Las notas del 16 de octubre dicen «próxima reunión en dos semanas», así que dejé la próxima el 2026-10-30.
- **Estado:** guardado en `estado/PRY-205-sistema-de-gestión-de-seguridad`.
- **Términos:** registrados a nombre de José Francisco Ñáñez, fecha 2026-10-16, para la versión 1.1. El comprobante está en `.criterio/terminos/aceptacion-criterio-project-0.3.12-2026-10-16.md` y `.pdf`. La huella SHA-256 del `.md` empieza por c5ca81ee804ae819.

**Lo que salió de las reuniones**
- **Reprogramados:** Elena Duarte movió «Enviar el documento 1» 6 veces; la promesa original era el 2026-09-30 y la vigente es el 2026-12-20. Laura Vélez movió «Cerrar la prueba 2» 5 veces; la original era el 2026-10-02 y la vigente es el 2026-12-13. Ninguna minuta sola lo muestra.
- **Vencidos sin evidencia (7):**
  - Gustavo Neira: anexo 3, 13 días; fecha 7, 14 días.
  - Mauricio Pérez: diseño 5, 2 días; ambiente 12, 4 días.
  - Paula Céspedes: matriz 6, 18 días.
  - Sandra Gil: fecha 15, 9 días.
  - Diana Molina: anexo 19, 2 días.
- **Sin fecha (3):** prueba 18 (Carlos Peña), matriz 22 (Rubén Cárdenas) y el ajuste del presupuesto (Laura Vélez, que dijo solo «la otra semana»).
- **Hito sin acta:** «Ingeniería básica aprobada» figura cerrado en el cronograma, pero no hay acta que lo pruebe (129 días desde su fecha).
- **Riesgo que nadie anotó:** el proveedor podría no llegar con el equipo completo para la siguiente fase. Lo dejé en la ficha como no registrado.
- **Estado declarado:** el informe del 11 de octubre dice verde y 58 %. El cálculo lo marca como contradicho por los vencidos, los reprogramados y el hito sin acta. El 58 % sí cabe en lo que sostiene el cronograma, y no hay desviación de costo.

**Qué falta en la carpeta**
- Un cronograma posterior al v1.
- El acta de recibo de ese hito.
- Actas de recibo de lo que Mauricio Pérez (diseño 5) y Ricardo Salas (matriz 14) dicen haber entregado.
- El contrato del proveedor.
- La autoridad del gerente, la etapa y el producto (el acta dice «No aplica»).

**Dos cosas para saber**
- No sellé la ficha, como pide el comando.
- Mi primera lectura del acta de constitución cambió el directorio de trabajo sin querer. Lo devolví a la raíz antes de crear ningún archivo, así que no dejó rastro.

La configuración está en `.criterio/proyecto/PRY-205/config.json` y pasó la verificación sin problemas. Lo mostrado quedó en `estado/PRY-205-sistema-de-gestión-de-seguridad/corridas/salida-pm-setup.md`, y la corrida quedó registrada como `2026-10-16-pm-setup-1`.