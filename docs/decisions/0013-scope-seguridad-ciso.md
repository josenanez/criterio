# 0013 · Propuesta: el alcance se amplía a seguridad de la información (CISO)

**Fecha:** 2026-10-23 · **Estado:** aceptada, con su diseño en la 0023 (2026-10-30) · **Modifica:** 0012

## Contexto

Seguridad es una de las cuatro capacidades «Siguiente» del mapa de la página de Agentes, en el
segundo lugar del orden. El rol no se define desde lo que se nos ocurra, sino desde dos marcos de
referencia:

- **El NIST Cybersecurity Framework 2.0**, publicado el 26 de febrero de 2024, con seis funciones:
  gobernar, identificar, proteger, detectar, responder y recuperar.
- **La ISO/IEC 27001:2022**, cuyos controles se declaran en una declaración de aplicabilidad y se
  sostienen con evidencia.

Cumple las cuatro condiciones de las 0006 y 0009:

- **Trabajo recurrente sobre documentos:** la declaración de aplicabilidad, la matriz de
  controles, los informes de vulnerabilidades, las revisiones de acceso y los informes de
  incidentes.
- **Una brecha entre lo declarado y lo escrito:** el control que se reporta operando y no tiene
  evidencia, o la vulnerabilidad que se da por cerrada sin prueba.
- **Plazos que calcula el código:** los acuerdos de nivel de servicio de cierre y la periodicidad
  de las revisiones.
- **Una persona que decide:** la aceptación de un riesgo es de su dueño.

## Decisión propuesta

**Una familia con un agente que contrasta los controles contra su evidencia y las
vulnerabilidades contra su cierre.** Reutiliza el patrón de Constanza: la matriz contra su
evidencia, con el calendario y el núcleo común.

| Lo que calcula el código | Cuándo se levanta |
|---|---|
| Control sin evidencia | Un control declarado como operando no tiene evidencia del periodo |
| Revisión vencida | Una revisión de acceso, de política o de un tercero pasó su fecha |
| Vulnerabilidad fuera de plazo | Una vulnerabilidad sigue abierta pasado su plazo según su severidad |
| Cierre sin prueba | Una vulnerabilidad aparece cerrada y ningún documento posterior lo sostiene |
| Incidente sin respuesta a tiempo | Un incidente no tiene su respuesta dentro del plazo que fija la política |
| Riesgo aceptado vencido | Una aceptación de riesgo pasó su fecha de revisión |

**Nunca:**

- corre un escaneo;
- toca un sistema;
- acepta un riesgo;
- declara cumplido un control;
- califica la madurez de la organización.

## Reglas para la operación real

- **Procesa informes exportados, nunca sistemas.** No se conecta a escáneres, directorios ni
  consolas.
- **Los secretos no entran.** La configuración excluye por omisión archivos de credenciales,
  llaves y respaldos, y el informe dice qué excluyó.
- **No se publica en Rostrum por omisión.** Un informe de vulnerabilidades abiertas es un mapa
  para un atacante.
- **La norma del país se verifica antes de citarse.** Por ejemplo, la circular de ciberseguridad
  del supervisor financiero de Colombia está por verificar.

## Lo que cuesta hoy

Son cifras de terceros, verificadas contra el texto de quien las publica.

| Cifra | Fuente | Muestra | Estado |
|---|---|---|---|
| **20 %** de las brechas empezó por la explotación de una vulnerabilidad, un 34 % más que el año anterior | Verizon, Data Breach Investigations Report 2025 ([informe](https://www.netaonline.org/sites/default/files/uploads/documents/2025-dbir-data-breach-investigations-report.pdf)) | 22.052 incidentes, de ellos 12.195 brechas confirmadas | Verificada |
| **54 %** de las vulnerabilidades de los dispositivos de borde se corrigió del todo en el año, con una mediana de 32 días | El mismo informe | La misma | Verificada |
| **USD 4,44 millones** cuesta en promedio una brecha de datos, y toma 241 días identificarla y contenerla | IBM con el Ponemon Institute, Cost of a Data Breach Report 2025 ([informe](https://www.bakerdonelson.com/webfiles/Publications/20250822_Cost-of-a-Data-Breach-Report-2025.pdf)) | 600 organizaciones con brechas, de marzo de 2024 a febrero de 2025 | Verificada |

## Lo que falta decidir

1. El nombre del agente.
2. Si se suma a la familia CLO, junto a Constanza, o va como familia propia.
3. Qué marco usa por omisión: NIST CSF 2.0 o ISO/IEC 27001:2022.
