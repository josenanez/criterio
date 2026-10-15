# /criterio-portfolio:project-history PRY-209

## Historia · PRY-209 Nómina electrónica · 2025-12-02 a 2026-10-15

**Leí:** 10 documentos, del 2025-12-02 al 2026-10-15.
**Trimestres sin un solo documento:** 2026-T1 y 2026-T2. Entre el 2025-12-10 y el 2026-09-08 no hay ninguno.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15). No hizo falta registrarlos de nuevo.

### En una línea
El proyecto se aprobó el 2025-12-02 con cierre en el acta el 2026-07-09. El cronograma v1 de la misma fecha dice 2026-06-20. Luego hay una laguna de nueve meses sin papel. Entre el 2026-10-03 y el 2026-10-15 aparecen juntos CC-01, dos actas de recibo, un cronograma v2 con la salida movida al 2026-07-22 y un informe en Verde con 86 %. De cinco hitos marcados como cerrados, solo dos tienen acta de recibo. Esas actas se firmaron el 2026-10-06 y el 2026-10-11, para hitos fechados el 2026-01-19 y el 2026-04-05.

### Las cuatro cifras
| Replanificaciones | Atraso vs. original | Meses declarando sin sustento | Cambios de gobierno |
|---|---|---|---|
| 1 | 32 días (16.8 %) | No calculable: solo hay una declaración de estado | 0 detectados |

### Replanificación
- **Fecha:** 2026-10-15.
- **Cambio:** la salida pasa del 2026-06-20 al 2026-07-22.
- **Motivo documentado:** ninguno en el cronograma. El informe dice «ventana de cambio del área de operaciones».
- **Aprobación:** ninguna. El script marca los 32 días como no autorizados.
- **CC-01:** pide esos mismos +32 días y sigue pendiente de comité.
- **Antigüedad:** la nueva fecha ya llevaba 85 días vencida al registrarse.

### Desde cuándo lo declarado no se sostiene
No se puede fechar un deslizamiento, porque no hay declaraciones anteriores a la del 2026-10-15. Lo que sí se fecha es la evidencia que falta:

- **Hitos cumplidos sin evidencia:**
  - «Ambiente de pruebas certificado» (vencía 2026-02-26, 231 días).
  - «Piloto con usuarios internos» (2026-05-13, 155 días).
  - «Salida a producción» (2026-07-22, 85 días).
- **Proveedor Redes del Norte:**
  - «Licenciamiento del motor» lleva 255 días pendiente.
  - «Parametrización del tarifario» lleva 151 días pendiente.
  - «Bolsa de horas» figura aceptada sin acta.
- **Factura FV-1154:** se radicó el 2026-09-08 por 105.979.087 COP, sin acta de recibo.

### Lecciones ancladas a un hecho
1. Un hito se recibe cuando se escribe, no cuando ocurre. Hoy solo 2 de 5 hitos tienen respaldo.
2. La línea base v2 se publicó sin aprobación: hay 32 días de atraso y 0 autorizados.
3. La factura FV-1154 se radicó sin el acta de recibo que exige el contrato.

### Lo que no sé
- Qué pasó entre 2025-12-10 y 2026-09-08.
- Si CC-01 llegó al comité del 2026-10-14. La minuta no lo menciona.
- El motivo real de la replanificación.
- Cuál de las dos fechas de cierre originales (2026-07-09 o 2026-06-20) rige.
- Los meses declarando sin sustento. No los calculé porque falta la serie de informes anteriores.

Nada de esto atribuye intención. Puedo llevar la historia al cierre del proyecto o al comité del 2026-10-21, donde CC-01 y la línea base v2 piden decisión.

El texto completo quedó en `estado/corridas/salida-project-history.md`. La corrida quedó registrada como `2026-10-15-project-history-1`.

Algunas cifras de la corrida registrada no corresponden a esta historia. Sale «proyectos: 13» y «hallazgos: 68» porque el script cuenta todo el portafolio, no solo PRY-209. «documentos» quedó en null porque el script no pudo medirlo.

*Pie de rigor: borrador de trabajo a partir de 10 documentos. Cada dato viene del documento citado y la verificación es suya. Las cifras derivadas salen de `portafolio.py compute`, con corte al 2026-10-15.*