# /criterio-data-governance:governance-setup datos/901666888-banco-control-de-datos-sintetico

Soy Custodia. Pongo cada dato del catálogo al lado de quien responde por él, de su clasificación y de su plazo; no asigno dueños ni borro nada.

Custodia quedó lista para el Banco Control de Datos Sintético. Los cinco conjuntos del catálogo tienen dueño y clasificación, así que no hay nada abierto. Los términos quedaron aceptados a nombre de José Francisco Ñáñez.

**Carpeta:** encontré una sola, `datos/901666888-banco-control-de-datos-sintetico`, con `00-referencia/`, `10-catalogo/`, `20-informes/` y `30-calidad/`, y la tomé. Sigue la estructura esperada y no hay archivos fuera de lugar ni ilegibles.

**Respuestas que tomé de los documentos:**
- **Entidad:** Banco Control de Datos Sintético, NIT 901666888, Colombia (COP).
- **Periodo:** 2026-11.
- **Publicar en Rostrum:** sí, porque la política de datos no dice otra cosa.
- **Dónde queda lo que encuentro:** `estado-datos/901666888-banco-control-de-datos-sintetico`.
- **Términos 1.6:** los mostré tal cual y quedaron aceptados.
- **Marca `_CRITERIO_DATOS.txt`:** no la dejé. Sin un sí explícito no creo nada en la carpeta de documentos.

**Dónde quedó:**
- **Configuración:** `.criterio/gobierno/901666888/config.json`
- **Comprobante de los términos:** `.criterio/terminos/aceptacion-criterio-data-governance-0.1.0-2026-11-25.md` y su `.pdf`
- **Primera ficha:** `estado-datos/901666888-banco-control-de-datos-sintetico/gobierno/2026-11/ficha.json`. Tiene las dos políticas con su fecha de revisión, los cuatro plazos de conservación y los cuatro términos del informe de junta de octubre.

---

# Cada conjunto con su dueño · Banco Control de Datos Sintético · periodo 2026-11

**Entidad:** Banco Control de Datos Sintético (901666888) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `catalog-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Conjunto | Dueño | Clasificación | Tipo | Datos personales |
|---|---|---|---|---|
| DS-01 · Clientes | Gerencia comercial | Confidencial | Clientes | sí |
| DS-02 · Movimientos | Gerencia de operaciones | Restringida | Transaccional | no |
| DS-03 · Proveedores | Compras | Interna | Proveedores | sí |
| DS-04 · Candidatos | Gestión humana | Confidencial | Candidatos | sí |
| DS-05 · Indicadores de gestión | Planeación | Interna | Transaccional | no |

El dueño y la clasificación los asigna el área: aquí se dice cuál falta.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Entidad, identificación fiscal y país → Banco Control de Datos Sintético, 901666888, CO (respuesta sugerida a partir de la carpeta y la política de datos)
- Periodo → 2026-11 (respuesta sugerida: el mes de la fecha de la prueba)
- ¿Se publica en Rostrum? → Sí (por omisión; la política de datos no dice otra cosa)
- ¿Dónde se guarda el estado? → estado-datos/901666888-banco-control-de-datos-sintetico
- Términos 1.6 → Aceptados por José Francisco Ñáñez
- ¿Se deja la marca _CRITERIO_DATOS.txt? → No: sin un sí explícito no se crea nada en la carpeta de documentos

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

---

**Reloj:** no creé la revisión diaria porque pide un sí explícito. Para correrla a mano: `/criterio-data-governance:governance-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.