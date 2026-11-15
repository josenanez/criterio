# /criterio-compliance:compliance-setup legal/88612904-4-distribuidora-del-ybytyruzu-sintetica

Constanza quedó configurada para Distribuidora del Ybytyruzú Sintética y calculó el primer estado, del periodo 2026-09.

En esta sesión de prueba tomé estas respuestas, sacadas de los documentos y del setup de Fidel:
- **Entidad:** RUC 88612904-4, Paraguay, guaraníes.
- **Periodo:** 2026-09.
- **Canal de denuncias:** 15 días de plazo de respuesta.
- **Normas nuevas:** 30 días para evaluarlas.
- **Fichas de Fidel:** están en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/contratos`. Comprobé que las 6 existen.
- **Términos 1.5:** los aceptó José Francisco Ñáñez el 2026-10-06. El comprobante quedó en `.criterio/terminos/` en Markdown y PDF.
- **Marca `_CRITERIO_LEGAL.txt`:** no la dejé, porque nadie la autorizó.

La configuración está en `.criterio/cumplimiento/88612904-4/config.json` y el motor la validó sin problemas. Registré en la ficha el estado que declara el informe de septiembre: «con observaciones».

El cálculo encontró 5 señales y este reporte muestra las 2 de la matriz. Las otras 3 son un caso del canal fuera de plazo, una norma aplicable sin obligación en la matriz y una revisión de política vencida. Se ven con `/criterio-compliance:reports-cases`, `/criterio-compliance:regulatory-watch` y `/criterio-compliance:policy-review`.

La pregunta sobre la fuente de OB-13 sigue sin respuesta. El reporte la muestra como «None» en lugar de dejarla vacía, y eso hay que corregirlo en el motor.

# Estado del cumplimiento · Distribuidora del Ybytyruzú Sintética · periodo 2026-09

**Entidad:** Distribuidora del Ybytyruzú Sintética (88612904-4) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.6.3 · **Comando:** `compliance-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Osvaldo Ramírez | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

**Estado declarado:** con observaciones (`cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5 («Estado del periodo: con observaciones»; presenta Osvaldo Ramírez, oficial de cumplimiento, línea 3)`) · **Avance con evidencia:** 76,19 % (ponderado por criticidad)

| Id | Obligación | Fuente | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|---|
| OB-06 | Reporte de operaciones del contratista de tecnología | Contrato CTR-4501 OBL-3 | Osvaldo Ramírez | 2026-10-05 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-06_reporte-de-operaciones-del-contratista-d-2026-09.md` |
| OB-01 | Reporte mensual de operaciones al supervisor | N-2026-01 · Resolución sintética 001 de 2026 | Osvaldo Ramírez | 2026-10-10 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-01_reporte-mensual-de-operaciones-al-superv-2026-09.md` |
| OB-03 | Informe trimestral del comité de riesgos | Política P-01 | Fátima Ayala | 2026-10-20 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-03_informe-trimestral-del-comite-de-riesgos-2026-09.md` |
| OB-10 | Declaración mensual de origen de fondos | Política P-04 | Osvaldo Ramírez | 2026-10-25 | cumplida sin evidencia | — |
| OB-04 | Certificación anual de la junta | Estatutos, artículo 40 | Fátima Ayala | 2026-12-31 | en plazo | — |
| OB-02 | Conciliación de la base de clientes vinculados | Política P-02 | Osvaldo Ramírez | 2026-10-07 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-02_conciliacion-de-la-base-de-clientes-vinc-2026-09.md` |
| OB-08 | Actualización de datos de proveedores críticos | Política P-04 | Celeste Villalba | 2026-10-08 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-08_actualizacion-de-datos-de-proveedores-cr-2026-09.md` |
| OB-07 | Revisión semestral de la matriz de riesgos | Política P-01 | Fátima Ayala | 2026-10-30 | cumplida con evidencia | `cumplimiento-2026-07/10-evidencias/OB-07_revision-semestral-de-la-matriz-de-riesg-2026-07.md` |
| OB-05 | Capacitación mensual del personal nuevo | Política P-03 | Celeste Villalba | 2026-10-20 | en plazo | — |
| OB-13 | Reporte de regalos e invitaciones | — | Celeste Villalba | 2026-10-10 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-13_reporte-de-regalos-e-invitaciones-2026-09.md` |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09 (respuesta sugerida por los documentos: es el único periodo con informe en 20-reportes; sesión de prueba sin interfaz)
- ¿Cuál es el plazo de respuesta del canal de denuncias? → 15 días (respuesta sugerida: la fijada en el setup de Fidel; sesión de prueba sin interfaz)
- ¿Cuántos días hay para evaluar una norma nueva? → 30 días (respuesta sugerida: la fijada en el setup de Fidel; sesión de prueba sin interfaz)
- ¿De qué norma, contrato o política sale la obligación OB-13 (Reporte de regalos e invitaciones)? La matriz no trae fuente. → None

## Fuentes

- `00-referencia/matriz-obligaciones.csv`

**Cuándo vuelvo:** no dejé una revisión diaria programada, porque en esta prueba nadie estaba para aprobarla. Para correrla a mano: `/criterio-compliance:compliance-wake`.

Quedó registrada la corrida `2026-10-06-compliance-setup-1`, y lo que se mostró está en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-compliance-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.