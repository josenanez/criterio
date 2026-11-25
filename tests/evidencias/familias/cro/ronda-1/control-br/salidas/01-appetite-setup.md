# /criterio-risk-appetite:appetite-setup riesgos/98765432000110-cooperativa-controle-sintetica

Severo está listo para la Cooperativa Controle Sintética (CNPJ 98765432000110, Brasil), con el periodo 2026-10. Ningún límite excedido queda sin plan ni aprobación: L-03 tiene un plan y L-04 tiene el exceso aprobado por el comité hasta el 2027-01-31. Todas las áreas reportaron dentro del plazo.

# Cada exposición contra su límite · Cooperativa Controle Sintética · periodo 2026-10

**Entidad:** Cooperativa Controle Sintética (98765432000110) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `limit-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Carteira vencida de crédito pessoal | máximo 6 % | 5.8 | no | — | Crédito | 2026-11-06 |
| L-02 | Índice de liquidez de curto prazo | mínimo 120 % | 131 | no | — | Tesouraria | 2026-11-10 |
| L-03 | Concentração no maior devedor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Perdas por fraude externa sobre receitas | máximo 0.5 % | 0.62 | sí | aprobado | Operações | 2026-11-07 |
| L-05 | Exposição a contrapartes sem rating | máximo 15 % | 12 | no | — | Tesouraria | 2026-11-09 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-12 (families/criterio-cro/FUENTES.es.md)

---

**Dónde quedó todo:**
- **Configuración:** `.criterio/apetito/98765432000110/config.json`. Los plazos vienen de la declaración: 10 días para reportar y revisión del consejo cada 12 meses.
- **Términos 1.6:** los aceptó José Francisco Ñáñez el 2026-11-25. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.1.0-2026-11-25.md` y `.pdf`.
- **Ficha 2026-10:** `estado-riesgos/98765432000110-cooperativa-controle-sintetica/apetito/2026-10/ficha.json`. Lleva la revisión de la declaración por el consejo del 2026-02-26 y la aprobación de L-04. Sobre L-03 el acta solo dice que el comité «toma conhecimento» del plan, así que no la registré como aprobación.
- **Reporte:** `estado-riesgos/98765432000110-cooperativa-controle-sintetica/apetito/2026-10/reporte-limit-check.md`
- **Marca:** dejé `_CRITERIO_RIESGOS.txt` en la carpeta de la entidad.
- **Corrida:** quedó registrada como `2026-11-25-appetite-setup-1`.

**Reloj:** no creé la tarea programada, porque pide un sí explícito y en esta sesión nadie responde. Para correrlo a mano: `/criterio-risk-appetite:appetite-wake`.

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.