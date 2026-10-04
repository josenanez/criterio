# Corrida · 2026-09-30-portfolio-wake-1

**Agente:** Vera (portafolio) · **Comando:** `/criterio-portfolio:portfolio-wake`

**Inicio:** 2026-09-30T07:03:03 · **Fin:** 2026-09-30T07:03:26 · **Duración:** 23 s

> Esta corrida no dejó cifras medidas por `corrida`: lo que hay es lo que el agente mostró. Si el comando debía correr los scripts y no lo hizo, eso es un hallazgo de la prueba.

## Lo que el agente mostró

No hay estado de portafolio configurado. El comando `/portfolio-wake` necesita que primero se haya corrido `/portfolio-setup`, que es el que:

1. Crea la carpeta de estado (`.criterio/state/...`)
2. Configura la cadencia (diaria, semanal, etc.)
3. Registra la aceptación de los términos de uso

Sin esa configuración, no hay cadencia contra la cual calcular qué toca hoy, ni carpeta de documentos indexada, ni estado previo.

¿Quieres que corra `/portfolio-setup` para dejar el agente listo?
