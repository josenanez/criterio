# /criterio-budget:budget-setup finanzas/89090314-minera-del-motagua

Terminé la instalación y dejé la corrida registrada. Esto es lo que quedó.

## Listo — Minera del Motagua · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2 (`presupuesto-2026-v2-2026-06-30.csv`), la más reciente de `10-aprobado/`. El acta 01 (2026-01-20) aprueba la v1. El acta 05 (2026-06-28) traslada 75,000.00 de Comercial · Publicidad a Comercial · Eventos.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.0.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-1.0.0-2026-10-06.md` y en el `.pdf` con el mismo nombre.

**Preguntas:** nadie podía responder, así que tomé lo sugerido por los documentos.
- **Versión:** la v2, por ser la más reciente.
- **Umbrales:** 10 %, 95 % y 45 días, los de `config.example.json`. Son configuración, no norma.
- **Fechas del comité:** ningún documento da la del próximo comité, así que quedó vacía.
- **Fichas PMO:** `estado-pmo/records`, donde está `PRY-310.json`.
- **Estado:** `estado-finanzas/89090314-minera-del-motagua`.

No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie podía autorizarlo en esta prueba.

**Ejecución contra lo aprobado, al corte 2026-09:** el reporte completo está en `estado-finanzas/89090314-minera-del-motagua/presupuesto/2026/reporte-variance-report.md`. Siete de las ocho líneas van 3.00 % por debajo de lo aprobado al corte. Nómina va en 0.00 %, es decir, justo en lo aprobado.

Algunas líneas del reporte:

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación |
|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 900,000.00 | 675,000.00 | 654,750.00 | 22,500.00 | 222,750.00 | -20,250.00 |
| Comercial | Publicidad | 1,125,000.00 | 862,500.00 | 836,625.00 | 26,250.00 | 262,125.00 | -25,875.00 |
| Personal | Nómina | 6,000,000.00 | 4,500,000.00 | 4,500,000.00 | 150,000.00 | 1,350,000.00 | 0.00 |

**Cinco señales abiertas.** El reporte de variance no las lista, pero el cálculo las levantó:
- **Operaciones · Transporte:** cambió 120,000.00 entre la v1 y la v2 sin acta que lo apruebe.
- **Tecnología · Licencias:** cambió -120,000.00 entre la v1 y la v2 sin acta que lo apruebe.
- **Comercial · Eventos y Publicidad:** la proyección del área usa la versión 1 y la aprobada es la 2.
- **Operaciones · Transporte:** su proyección es del 2026-07-15, hace 83 días.

**Compromiso del comité:** el acta 06 (2026-09-10) encarga a Administración revisar el contrato de vigilancia antes del próximo comité. Quedó en la ficha como abierto, sin evidencia.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La salida completa quedó en `estado-finanzas/89090314-minera-del-motagua/corridas/salida-budget-setup.md`, y la configuración en `.criterio/presupuesto/89090314/config.json`.