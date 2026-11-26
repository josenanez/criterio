# /criterio-data-governance:governance-setup datos/901666888-banco-control-de-datos-sintetico

Soy Custodia. Pongo cada dato del catálogo al lado de quien responde por él, de su clasificación y de su plazo; no asigno dueños ni borro nada.

**Carpeta:** encontré solo una, `datos/901666888-banco-control-de-datos-sintetico`, que tiene 00-referencia/, 10-catalogo/, 20-informes/ y 30-calidad/. La propongo y sigo con ella. Tiene la estructura esperada: 11 documentos, ninguno fuera de lugar ni ilegible.

**Respuestas que tomé de los documentos:**
- **Entidad:** Banco Control de Datos Sintético, identificación fiscal 901666888, país CO.
- **Periodo:** 2026-11.
- **Publicar en Rostrum:** sí, porque la política de datos no dice otra cosa.
- **Dónde guardo lo que encuentro:** `estado-datos/901666888-banco-control-de-datos-sintetico`.
- **Diferencia que se tolera entre una cifra y su fuente:** 0.5 %, según la política de datos.
- **Archivo `_CRITERIO_DATOS.txt` para reconocer la carpeta:** sí, y ya quedó en ella.

**Términos (versión 1.6):**

> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-data-governance-0.2.0-2026-11-25.md` y en su `.pdf`.

**Configuración:** `.criterio/gobierno/901666888/config.json`.

**Primera ficha (2026-11):** procesé 00-referencia/ y 20-informes/. Llevé a la ficha cada política con su fecha de revisión, cada plazo de conservación y cada término del informe a la junta de octubre.

# Cada conjunto con su dueño · Banco Control de Datos Sintético · periodo 2026-11

**Entidad:** Banco Control de Datos Sintético (901666888) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Custodia, versión 0.2.0 · **Comando:** `catalog-check`

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

**Cuándo vuelvo:** sin reloj. La tarea programada solo se crea con un sí explícito, y en esta sesión nadie puede darlo. Para correrlo a mano: `/criterio-data-governance:governance-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.