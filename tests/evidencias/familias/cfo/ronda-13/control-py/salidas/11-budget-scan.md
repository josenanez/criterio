# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior; las tres actas de `40-actas` se leyeron y ya estaban en la ficha. No apareció ninguna señal.

# Qué cambió en el presupuesto · Comercial Control del Paraguay (sintética) · presupuesto 2026, corte 2026-09

**Entidad:** Comercial Control del Paraguay (sintética) (88733016-9) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.2.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

(El motor no devolvió resultados en esta corrida: 0 señales, 0 documentos sin procesar.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad y el año presupuestal? → Comercial Control del Paraguay (sintética), RUC 88733016-9, presupuesto 2026, corte 2026-09 (tomado de la carpeta)
- ¿Cuál es la versión aprobada y su acta? → Rige la v2 (la más reciente de 10-aprobado/); nace del acta 05 de traslado (2026-06-28) sobre la v1 aprobada por el acta 01 (2026-01-20)
- ¿Áreas y responsables? → Administración, Comercial, Tecnología, Operaciones y Personal, tomadas del presupuesto; responsables no indicados en los documentos
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días
- ¿Fechas del comité de presupuesto? → No encontradas en los documentos; el acta 06 es del 2026-09-10 y no fija la siguiente
- ¿Dónde están las fichas PMO? → estado-pmo/records (existe PRY-310.json)
- ¿Dónde se guarda el estado? → estado-finanzas/88733016-9-comercial-control-del-paraguay-sintetica, compartido con Clara y fuera de la carpeta de documentos

## Fuentes

- Sin documentos citados.

---
Corrida registrada: `2026-10-06-budget-scan-1`.

Dos observaciones:
- El texto de arriba, "El motor no devolvió resultados en esta corrida…", lo añadí yo. El reporte del motor traía la sección "El resultado" vacía, y en `corridas/salida-budget-scan.md` queda sin esa línea.
- El reporte dice "Sin documentos citados" en Fuentes, aunque la ficha cita las tres actas y el correo de Administración. Eso es de cómo lo genera el motor, y no lo toqué.

Los términos ya estaban vigentes (aceptados por José Francisco Ñáñez el 2026-10-06), así que no hizo falta registrarlos de nuevo.