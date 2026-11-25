# /criterio-data-governance:governance-setup datos/rcc200101cd2-retail-control-de-datos-sintetico

Soy Custodia. Pongo cada dato del catálogo al lado de quien responde por él, de su clasificación y de su plazo; no asigno dueños ni borro nada.

**Carpeta:** encontré una sola, `datos/rcc200101cd2-retail-control-de-datos-sintetico`, con las cuatro carpetas esperadas (`00-referencia/`, `10-catalogo/`, `20-informes/`, `30-calidad/`). Tomé el sí. Tiene 11 documentos; ninguno está fuera de lugar y todos se pudieron abrir.

**Preguntas y la respuesta que tomé de los documentos:**
1. Entidad, identificación fiscal y país: Retail Control de Datos Sintético, RFC RCC200101CD2, México (MXN). Salen del nombre de la carpeta y de la política de datos.
2. Periodo: 2026-11.
3. ¿Publico en Rostrum? Sí, porque la política de datos no dice otra cosa.
4. Dónde guardo lo que encuentro: `estado-datos/rcc200101cd2-retail-control-de-datos-sintetico`.
5. Términos (versión 1.6, del 2026-11-16):
   > Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

   Los aceptó José Francisco Ñáñez el 2026-11-25.
6. ¿Dejo la marca `_CRITERIO_DATOS.txt` en la carpeta de datos? Sí.

**Quedó listo:**
- **Configuración:** `.criterio/gobierno/RCC200101CD2/config.json`
- **Comprobante de aceptación:** `.criterio/terminos/aceptacion-criterio-data-governance-0.1.0-2026-11-25.md` y su versión `.pdf`
- **Marca:** quedó en la carpeta de datos.

**Ficha 2026-11:** procesé `00-referencia/` y `20-informes/`. Pasé a la ficha 2 políticas con su fecha de revisión, 4 plazos de conservación y 4 términos del informe de junta de octubre.

Los cinco conjuntos del catálogo tienen dueño y clasificación. Los plazos de conservación se revisan con `retention-check` y los términos contra el glosario con `glossary-check`.

# Cada conjunto con su dueño · Retail Control de Datos Sintético · periodo 2026-11

**Entidad:** Retail Control de Datos Sintético (RCC200101CD2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.1.0 · **Comando:** `catalog-check`

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

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. No programé la tarea diaria porque nadie dio un sí explícito. Se corre a mano con `/criterio-data-governance:governance-wake`.

La corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.