# /criterio-legal:legal-setup legal/52817460000100-banco-serra-verde

Fidel quedó instalado sobre Banco Serra Verde (CNPJ 52817460000100, Brasil, BRL). Procesé los 6 contratos y no hubo `record_issues`. El calendario señala dos cosas a atender.

**Para atender**
- **CTR-1604, Licenças Digitais:** el informe mensual de agosto venció el 2026-09-05 y no hay evidencia en `40-ejecucion/`. Lleva 31 días de retraso.
- **CTR-1604, Licenças Digitais:** el preaviso de no renovación vence el 2026-11-01, en 26 días, y nadie ha decidido. El contrato se prorroga solo por 12 meses si nadie avisa. La decisión de renovar o terminar es de una persona.

**Próximos vencimientos**
- 2026-11-20: terminación de CTR-1605 y su informe final.
- 2026-12-31: terminación de CTR-1603 y de CTR-1604, con sus informes finales.

**Otras señales**
El cálculo marcó tres más: una firma sin facultad, una garantía faltante y un registro que difiere del contrato. Una de cada una. No las revisé aquí. Salen en `authority-check`, `contract-execution` y `contract-register`.

**Lo que hice**
- **Preguntas:** no hice ninguna, por ser una sesión sin interfaz. Tomé las respuestas de los documentos: avisos a 60 y 30 días, certificado de máximo 30 días (los valores de `config.example.json`) y estado fuera de la carpeta de documentos.
- **Términos:** los mostré tal cual (versión 1.3) y registré la aceptación de José Francisco Ñáñez con fecha 2026-10-06. No dejé la marca `_CRITERIO_LEGAL.txt` porque la raíz vino dada en el argumento y no hubo quien autorizara.
- **Fecha:** pasé `--today 2026-10-06` en cada llamada del motor que la acepta. El calendario sale con corte a esa fecha.

**Archivos**
- Configuración: `.criterio/legal/52817460000100/config.json`
- Fichas: `estado-legal/52817460000100-banco-serra-verde/contratos/CTR-1601.json` a `CTR-1606.json`
- Calendario: `estado-legal/52817460000100-banco-serra-verde/contratos/reporte-obligations-calendar.md`
- Corrida registrada como `2026-10-06-legal-setup-1`, con la salida en `estado-legal/52817460000100-banco-serra-verde/corridas/salida-legal-setup.md`