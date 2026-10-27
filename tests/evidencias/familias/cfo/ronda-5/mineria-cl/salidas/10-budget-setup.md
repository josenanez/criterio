# /criterio-budget:budget-setup finanzas/76089001-4-minera-atacama-norte

## Listo — Minera Atacama Norte · presupuesto 2026

**Lo que miré:**
- 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30).
- Contabilidad de 2026-01 a 2026-09 (9 periodos).
- 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`.
- Nació del traslado del acta 05 (2026-06-28): 1.800.000 de Publicidad a Eventos.
- La v1 la aprueba el acta 01 del 2026-01-20.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 (versión 0.10.0, términos 1.2). Los mostré tal cual antes de registrarlos. El comprobante está en `.criterio/terminos/`.

**Lo que hay que atender (corte 2026-09, versión 2)**
1. **Operaciones · Transporte:** ejecutado 21.735.000,00 contra 18.900.000,00 aprobado al corte. Son 2.835.000,00 de más (+15,0 %), por encima del umbral de 10 %.
2. **Administración · Mantenimiento:** ejecutado más comprometido es el 96,0 % de lo aprobado en el año, por encima del umbral de 95 %. Quedan 570.000,00 disponibles.

Las demás líneas están 3,0 % por debajo de lo aprobado al corte; Nómina está en 0,00 %.

**Compromiso abierto del acta 06:** Administración revisa el contrato de vigilancia antes del próximo comité.

**Preguntas que no se respondieron** (la sesión era sin interfaz, así que tomé lo que dicen los documentos):
- No encontré responsables de área en los documentos.
- No hay fecha de comité futura, así que `committee_dates` quedó vacío.
- No dejé el archivo `_CRITERIO_FINANZAS.txt` en la carpeta: nadie podía autorizarlo.

**Dónde quedó todo**
- Configuración: `.criterio/presupuesto/76089001-4-minera-atacama-norte/config.json`.
- Reporte completo: `estado-finanzas/76089001-4-minera-atacama-norte/presupuesto/2026/reporte-variance-report.md`. Tiene la tabla por área y línea con aprobado, al corte, ejecutado, comprometido, disponible, desviación y citas.
- Lo que te mostré, tal cual: `estado-finanzas/76089001-4-minera-atacama-norte/corridas/salida-budget-setup.md`. La corrida quedó registrada como `2026-10-06-budget-setup-1`.

Las fichas PMO están en `estado-pmo/records` (existe `PRY-310.json`), y el presupuesto de PRY-310 ya se cruza con el de Tecnología.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.