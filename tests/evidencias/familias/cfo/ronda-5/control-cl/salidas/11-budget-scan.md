# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior (66 documentos). Las tres actas ya estaban en la ficha y el motor no levantó señales.

# Qué cambió en el presupuesto · Comercial Control Andes · presupuesto 2026, corte 2026-09

**Entidad:** Comercial Control Andes (76097001-8) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Contralor · **Comando:** `budget-scan`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad y el año presupuestal? → Comercial Control Andes (76097001-8), presupuesto 2026; respuesta tomada del inventario y de la configuración de finanzas
- ¿Cuál es la versión aprobada y su acta? → Rige la más reciente de 10-aprobado, la v2 del 2026-06-30; el acta 01 (2026-01-20) aprueba la v1 y el acta 05 (2026-06-28) el traslado que origina la v2. No se fijó approved_version
- ¿Cuáles son las áreas y su responsable? → Las que trae el mapeo: Administración, Comercial, Tecnología, Operaciones y Personal. Responsable: no encontrado en los documentos, solo el compromiso del acta 06 señala a Administración
- ¿Cuál es el mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv; prefijo de gasto 51
- ¿Qué umbrales se usan? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida a 45 días (configuración, no norma)
- ¿Hay fechas de comité de presupuesto? → No encontradas; el acta 06 habla del próximo comité sin fecha. Queda vacío
- ¿Dónde están las fichas de proyectos PMO? → estado-pmo/records, con PRY-310.json
- ¿Dónde guardo lo que voy encontrando? → estado-finanzas/76097001-8-comercial-control-andes, fuera de la carpeta de documentos
- ¿Se marca la carpeta raíz con _CRITERIO_FINANZAS.txt? → No se escribió nada dentro de los documentos: la sesión de prueba no tiene a nadie que lo autorice

## Fuentes

- Sin documentos citados.

---
Corrida registrada como `2026-10-06-budget-scan-1` (0 hallazgos). Los términos ya estaban vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06), así que no hizo falta registrarlos de nuevo.