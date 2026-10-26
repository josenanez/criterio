# 0016 · Propuesta: la tesorería, tercer agente de la familia CFO

**Fecha:** 2026-10-23 · **Estado:** propuesta · **Modifica:** 0006

## Contexto

La familia CFO tiene dos agentes: Clara (el cierre y el control) y Tomás (el presupuesto). Le falta
la tesorería: la caja, los bancos, los pagos y la deuda.

**El rol se define desde O*NET**, la clasificación de ocupaciones del Departamento de Trabajo de
los Estados Unidos. O*NET pone a tesoreros y contralores en una misma ocupación, la 11-3031.01
(*Treasurers and Controllers*). De sus 23 tareas, 7 son de tesorería:

- vigilar el flujo de caja y los niveles de reserva;
- evaluar las necesidades de financiamiento y la inversión de los excedentes;
- llevar la relación con los bancos;
- delegar quién recibe, desembolsa y custodia los fondos;
- autorizar los desembolsos según la política;
- recibir el efectivo y hacer los depósitos;
- vigilar y mitigar el riesgo cambiario.

Que sea la misma ocupación que la contraloría es la razón para que vaya **dentro de la familia CFO**
y no como una familia aparte. Comparte con Clara el motor (`finanzas.py`, que ya procesa los
extractos bancarios), la entidad y el periodo. Con un tercer agente, la CFO queda con tres, como la
PMO.

## Decisión propuesta

**Un tercer agente en la familia CFO que contrasta la caja contra su proyección y su política, los
pagos contra quién puede autorizarlos, y la deuda contra lo que exige su contrato.**

| Lo que calcula el código | Cuándo se levanta |
|---|---|
| Caja bajo el mínimo | El saldo de una cuenta o del consolidado queda por debajo del mínimo que fija la política |
| Caja distinta de la proyección | La posición real se aparta de la proyectada más del umbral |
| Pago sin aprobación | Un pago programado no tiene la aprobación que pide la política para su monto |
| Firmante sin facultad | Quien aprueba un pago no tiene la facultad según la matriz de firmas (el mismo patrón de Fidel) |
| Covenant en riesgo | Un indicador de un contrato de deuda, calculado desde los estados que cerró Clara, se acerca a su límite o lo cruza |
| Vencimiento cercano | Una obligación de deuda o una inversión vence dentro de N días |
| Exposición cambiaria sobre el límite | La posición en otra moneda supera el límite de la política |

**Nunca:**

- mueve dinero;
- hace un pago;
- entra a un portal bancario;
- negocia con un banco;
- recomienda una inversión o un financiamiento;
- decide cubrir un riesgo.

## Reglas para la operación real

- **Procesa exportaciones**: los extractos, los reportes del portal bancario y el programa de
  pagos. Nunca usa las credenciales de un banco.
- **Los covenants salen de los estados que Clara ya cerró.** El agente no recalcula la
  contabilidad: toma la ficha del cierre, como Tomás toma la ejecución.
- **El informe no se publica en Rostrum por omisión**, porque trae saldos y cuentas.
- **Primero, la tesorería corporativa.** La de un banco —la gestión de activos y pasivos y la
  liquidez regulatoria— tiene otra norma y otro alcance, y queda para su propia decisión.

## Lo que cuesta hoy

Son cifras de terceros, verificadas contra el texto de quien las publica.

| Cifra | Fuente | Muestra | Estado |
|---|---|---|---|
| **79 %** de las organizaciones sufrió en 2024 un intento de fraude en pagos o un fraude consumado | Association for Financial Professionals, 2025 Payments Fraud and Control Survey, 15 de abril de 2025 ([nota](https://www.financialprofessionals.org/about/learn-more/press-releases/Details/survey-79-percent-of-organizations-were-victims-of-attempted-or-actual-payments-fraud-activity-in-2024)) | 521 profesionales de finanzas corporativas | Verificada |
| **63 %** señala la suplantación por correo corporativo como la principal vía de esos fraudes | La misma | La misma | Verificada |
| **63 %** sufrió fraude con cheques | La misma | La misma | Verificada |

## Decidido

- **El nombre: Áurea**, del latín *aureus*, «de oro»: la caja. Se pronuncia igual en español, inglés
  y portugués. José, 2026-10-26.
- **Es una extensión de la CFO**, no una familia aparte: la oficina del CFO gana un tercer agente.
  José, 2026-10-26.

## Lo que falta decidir

1. Si el primer incremento incluye los covenants de la deuda o empieza con la caja y los pagos.
