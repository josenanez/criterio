# /criterio-data-governance:governance-setup datos/rcc200101cd2-retail-control-de-datos-sintetico

Soy Custodia. Pongo cada dato del catálogo al lado de quien responde por él, de su clasificación y de su plazo; no asigno dueños ni borro nada.

**La carpeta de datos.** Encontré una sola: `datos/rcc200101cd2-retail-control-de-datos-sintetico`. Tiene las cuatro carpetas que espero: 00-referencia/, 10-catalogo/, 20-informes/ y 30-calidad/. La tomé porque venía en tu pedido. Hay 11 documentos y ninguno está fuera de lugar ni se pudo dejar de procesar.

**Las preguntas.** Nadie estaba en la sesión para responder, así que tomé la respuesta que sugieren los documentos:
1. **Entidad:** Retail Control de Datos Sintético, RFC RCC200101CD2, México, en pesos mexicanos (MXN).
2. **Periodo:** 2026-11, el mes en curso a la fecha de la prueba.
3. **Publicar en Rostrum:** sí. Es lo que se hace por omisión y la política de datos no dice otra cosa.
4. **Dónde guardo lo que encuentro:** `estado-datos/rcc200101cd2-retail-control-de-datos-sintetico`, fuera de la carpeta de los documentos.
5. **Términos, versión 1.6 del 2026-11-16, tal cual:**
   > Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

   José Francisco Ñáñez los aceptó el 2026-11-25.
6. **Marcar la carpeta con `_CRITERIO_DATOS.txt`:** sí.

**Quedó listo:**
- **Configuración:** `.criterio/gobierno/RCC200101CD2/config.json`
- **Comprobante de los términos:** `.criterio/terminos/aceptacion-criterio-data-governance-0.2.0-2026-11-25.md`, con su copia en `.pdf`
- **Marca:** quedó en la carpeta de datos

**La primera ficha, de 2026-11.** Procesé los documentos de `00-referencia/` y de `20-informes/`. Llevé a la ficha, cada una con su cita:
- 2 políticas con su fecha de revisión
- 4 plazos de conservación
- 4 términos del informe de junta

El motor no encontró nada abierto en el catálogo: los cinco conjuntos tienen dueño y clasificación.

# Cada conjunto con su dueño · Retail Control de Datos Sintético · periodo 2026-11

**Entidad:** Retail Control de Datos Sintético (RCC200101CD2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `catalog-check`

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

- ¿Periodo de la primera ficha? → 2026-11 (mes en curso a la fecha de la prueba), sugerida y tomada sin respuesta de la persona
- ¿Se publica en Rostrum? → Sí, por omisión; la política de datos no dice otra cosa
- ¿Dónde se guarda el estado? → estado-datos/rcc200101cd2-retail-control-de-datos-sintetico
- ¿Se marca la carpeta con _CRITERIO_DATOS.txt? → Sí, respuesta sugerida en la sesión de prueba

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. La revisión diaria programada necesita un sí explícito, y en esta prueba no había nadie para darlo. Para correrla a mano: `/criterio-data-governance:governance-wake`.

La corrida quedó registrada como `2026-11-25-governance-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.