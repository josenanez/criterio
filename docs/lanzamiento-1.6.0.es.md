# Criterio · catálogo 1.6.0 · 30 de octubre de 2026

Entra la familia **CISO · La seguridad de la información**, en su 0.1.0 de laboratorio: Alexis, Guillermo y Amparo, ordenados por las seis funciones del NIST Cybersecurity Framework 2.0. Código abierto bajo Apache 2.0.

**El número del catálogo solo ordena las entradas del registro de versiones.** La versión de cada familia es la suya.

## Qué trae

| | |
|---|---|
| **Alexis · el gobierno y los controles** | La declaración de aplicabilidad contra la evidencia de cada control —el que no tiene ninguna, el que la tiene vencida, el que no tiene responsable—, las revisiones de acceso y las evaluaciones de terceros críticos que vencieron, y las aceptaciones de riesgo que pasaron su fecha |
| **Guillermo · las vulnerabilidades** | Cada hallazgo del escáner contra el plazo de su severidad en la política, el catálogo KEV de CISA (F-06), las excepciones vencidas, los cierres que ningún escaneo prueba y los activos que ningún escaneo cubre. Cualquier exportación en CSV o Excel, con su mapeo; la severidad desde el CVSS v4.0 cuando el escáner solo da el puntaje (F-05) |
| **Amparo · la respuesta y la recuperación** | Cada incidente contra el plazo de contención de su severidad, cada notificación de la matriz —al supervisor, a la autoridad de datos, a los clientes— contra la que se hizo, la revisión posterior, y las pruebas de continuidad, de recuperación y de restauración contra su calendario |
| **Los plazos son de la organización** | Salen de su política, su matriz y sus registros, con su cita. Lo único externo es la fecha que trae el catálogo KEV |
| **Lo que nunca se abre** | Credenciales, llaves y respaldos quedan fuera por omisión, y cada reporte dice cuáles excluyó. Lo de vulnerabilidades no se publica en Rostrum salvo que la configuración lo diga |
| **CISO 0.1.0** | El motor, probado contra material sintético de banca, retail, salud y tecnología con dos entidades de control: 100 de 100 señales y ninguna de más. **De laboratorio**: la ronda con los tres agentes, en la 0.2.0 |

## Las versiones en la 1.6.0

| Familia | Versión | Calidad | Lanzamiento |
|---|---|---|---|
| PMO · Vera, Samuel y Alba | 1.0.0 | Estable | Semana del 19 de octubre |
| CFO · Clara, Tomás y Áurea | 1.0.0 | Estable | Semana del 26 de octubre |
| CLO · Fidel y Constanza | 1.1.0 | Estable | Sin lanzar |
| EA · Ofelia | 1.0.0 | Estable | Semana del 26 de octubre |
| CCO · Augusto y Valeria | 0.3.0 | Estable | Sin lanzar |
| CISO · Alexis, Guillermo y Amparo | **0.1.0** | De laboratorio | Sin lanzar |
| Rostrum | 1.0.0 | — | — |

En esta entrada se libera la CISO.

## Para instalarla

```
/plugin install criterio-security@criterio
/plugin install criterio-vulnerability@criterio
/plugin install criterio-resilience@criterio
```

Cada agente pide aceptar los términos de su versión y deja su comprobante en `.criterio/terminos/`.
