# /criterio-compliance:compliance-setup legal/900000001-distribuidora-control

Constanza quedó instalada sobre Distribuidora Control (900000001, CO). Revisó las 8 obligaciones de la matriz contra su evidencia y no abrió ninguna señal.

**Estado del periodo 2026-09**
- **Declarado:** el informe del 2026-10-05, de Jorge Silva, dice «cumplido».
- **Evidenciado:** el avance con evidencia es 83,33 %, ponderado por criticidad.
- **Con evidencia:** OB-01, OB-02, OB-03, OB-06 y OB-08.
- **Sin evidencia:** OB-05 (vence el 2026-10-20) y OB-04 (vence el 2026-12-31), ambas en plazo.
- **OB-07:** cuenta como cumplida con una evidencia de 2026-07, porque es semestral.
- **Norma nueva:** el boletín del 2026-09-28 trae la Circular sintética 009 de 2026 (N-2026-09), por evaluar. El registro normativo todavía no la tiene. Quedó en la ficha del periodo para que `regulatory-watch` la evalúe.

**Cosas que conviene saber**
- **Dónde quedó la configuración:** en `.criterio/legal/900000001/config.json`, no en `.criterio/cumplimiento/`. El motor reutilizó la de Fidel y no creó una nueva. Le agregué `period: 2026-09` a mano, porque ningún comando lo pone.
- **Términos:** la primera vez no pasé `--today`, y el comprobante salió con fecha 2026-10-22. Lo repetí con 2026-10-06 y quedó a nombre de José Francisco Ñáñez. El comprobante de 2026-10-22 sigue en `.criterio/terminos/`, sin usar.
- **Preguntas:** hice una sola, el periodo. Tomé la respuesta sugerida (2026-09, el del último informe) y la dije en el reporte.
- **Marca `_CRITERIO_LEGAL.txt`:** no la dejé, porque no hay nadie que la autorice en esta sesión.

Los archivos están en `estado-legal/900000001-distribuidora-control/`:
- `cumplimiento/2026-09/reporte-compliance-status.md`: el reporte completo.
- `cumplimiento/2026-09/ficha.json`: la ficha del periodo.
- `corridas/salida-compliance-setup.md`: lo que mostré, tal cual.

La corrida quedó registrada como `2026-10-06-compliance-setup-1`.