# /criterio-risk-appetite:appetite-setup riesgos/98765432000110-cooperativa-controle-sintetica

Severo está configurado para la Cooperativa Controle Sintética y el primer chequeo de límites salió limpio: **nada abierto** en el periodo 2026-10. Hay 4 límites excedidos y cada uno tiene un plan o un exceso aprobado.

**Carpeta:** solo encontré una, `riesgos/98765432000110-cooperativa-controle-sintetica`, con las cinco subcarpetas esperadas. Procesé sus 11 documentos; ninguno estaba fuera de lugar ni ilegible.

**Respuestas que tomé de los documentos** (en esta prueba nadie contestó preguntas):
- **Entidad:** Cooperativa Controle Sintética, CNPJ 98765432000110, Brasil, moneda BRL.
- **Último periodo cerrado:** 2026-10.
- **Plazo para reportar la exposición:** 10 días corridos después del cierre (declaración de apetito, p. 1).
- **Revisión de la declaración por el consejo:** cada 12 meses (declaración de apetito, p. 1).
- **Publicar en Rostrum:** sí; el marco no dice otra cosa.
- **Estado:** queda en `estado-riesgos/98765432000110-cooperativa-controle-sintetica`, fuera de los documentos.
- **Marca `_CRITERIO_RIESGOS.txt`:** no la dejé, porque nadie la autorizó.

**Términos (versión 1.6):** los mostré tal cual y quedaron aceptados por José Francisco Ñáñez con fecha 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-risk-appetite-0.2.0-2026-11-25.md` y en `.pdf`.

**Configuración:** quedó en `.criterio/apetito/98765432000110/config.json` y la validación no encontró problemas.

**Ficha de 2026-10:**
- La declaración la revisó el consejo el 2026-02-26 (`00-marco/declaracao_de_apetite.pdf`, p. 1).
- El acta del comité de riesgos del 2026-11-12 aprueba los excesos de L-04, L-06 y L-07 (`40-actas/ata_comite_riscos_2026-10.pdf`, p. 1).
- Sobre L-03, el acta solo dice que el comité «toma conocimiento» del plan de acción. No lo registré como aprobación; en el reporte figura con plan.

---

# Cada exposición contra su límite · Cooperativa Controle Sintética · periodo 2026-10

**Entidad:** Cooperativa Controle Sintética (98765432000110) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `limit-check`

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
| L-06 | Perdas operacionais sobre o patrimônio | máximo 1 % | 1.1 | sí | aprobado | Operações | 2026-11-08 |
| L-07 | Exposição ao maior banco correspondente | máximo 20 % | 23 | sí | aprobado | Tesouraria | 2026-11-09 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-12 (families/criterio-cro/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj, porque nadie dio un sí explícito a la tarea programada. Para correrlo a mano: `/criterio-risk-appetite:appetite-wake`.

Lo que mostré quedó guardado en `estado-riesgos/98765432000110-cooperativa-controle-sintetica/corridas/salida-appetite-setup.md`, y la corrida se registró como `2026-11-25-appetite-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.