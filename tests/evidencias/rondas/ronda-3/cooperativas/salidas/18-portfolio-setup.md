# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Cooperativa

Vera quedó instalada y probada con tres proyectos. En los tres, el estado "verde" que declara el gerente no lo sostienen los documentos.

**Miré:** 79 documentos en 13 proyectos. Los formatos son .md (38), .docx (12), .pdf (10), .xlsx (10), .csv (7), .json (1) y .txt (1). El más reciente es del 2026-10-15.
**Eres:** PMO del portafolio. Es el valor sugerido, porque hay varios proyectos.
**Te aviso:** dos días antes del comité, que puse el 2026-10-22, cada dos semanas. Son valores sugeridos, porque no dijiste fecha de comité.
**En:** presentación, también valor sugerido. En la configuración quedó como `html`, que es el formato del ejemplo; lo dejé así sin comprobar que sea el que corresponde a "presentación".
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-15, versión 0.3.9 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-portfolio-0.3.9-2026-10-15.md` y `.pdf`. SHA-256: f0f8a373c9bdced2…
**Dónde quedó todo:** la configuración en `.criterio/portafolio/config.json`, lo que voy encontrando en `estado/` y los informes en `reportes/`.

La configuración la escribí a mano, porque `init` solo creó las carpetas del estado. `config` la verificó sin problemas.

### Probé con tres proyectos
Cuatro proyectos empatan con documentos del 2026-10-15 (202, 203, 204 y 206). Tomé los tres primeros por código.

| Proyecto | Documentos | Qué supe | Qué no está |
|---|---|---|---|
| PRY-202 Core cooperativo | 7 | Gerente Camilo Beltrán. Presupuesto de 2.400 M COP, con 1.390 M comprometidos y 876 M ejecutados. Declara verde y 76 %. El cierre del acta era el 2026-04-14. | La facultad del gerente. El producto, que el acta pone como «No aplica». |
| PRY-203 Aportes sociales en línea | 14 | Gerente Óscar Ramírez. Presupuesto de 3.300 M, con 1.340 M ejecutados. Declara verde y 60 %. Tiene una ficha del gerente (`ficha-pm.json`), que guardé aparte. Registré 26 compromisos de seis reuniones. | La facultad del gerente. El estado declarado en la ficha del gerente. |
| PRY-204 Tarjeta débito | 6 | Gerente Ricardo Salas. Presupuesto de 9.500 M, con 86 % comprometido. Declara verde y 74 %. | La facultad del gerente. La fecha del compromiso «Entregar el punto 40», que dice «por definir». |

### Hallazgos
El cálculo levantó 29 señales en los tres proyectos.

**PRY-202**
- El piloto se movió del 2026-03-09 al 2026-07-06, así que el atraso contra la línea base original es de 119 días (41,6 %).
- El cronograma da los 4 hitos por cerrados (100 %) y el informe reporta 76 %.
- Tres hitos están cerrados sin acta de recibo: ambiente de pruebas, integración con el core y piloto. Solo «Diseño funcional aprobado» tiene acta, y es del 2026-10-06, 14 meses después de su fecha.

**PRY-203**
- Los 5 hitos figuran cerrados (100 %) y el informe reporta 60 %.
- Cuatro hitos están cerrados sin acta. Solo «Salida a producción» la tiene, del 2026-10-04, y el informe del 10-13 dice que esa salida se reprogramó.
- Hay 7 compromisos vencidos.
- Cinco personas dijeron en reunión que ya entregaron y no hay acta: Beatriz Cuéllar, Sandra Gil, Diana Molina, María Restrepo y Carlos Peña.
- «Enviar el documento 1» (María Restrepo) lleva 6 reprogramaciones, del 2026-09-21 al 2026-12-12. «Cerrar la prueba 2» (Paula Céspedes) lleva 5.
- Hay 3 compromisos sin fecha.
- En la reunión del 10-15 se comentó que el proveedor podría no llegar con el equipo completo, y nadie lo anotó como riesgo. Lo dejé en la ficha como riesgo sin dueño.

**PRY-204**
- El cronograma v2 (2026-10-15) movió la integración con el core 112 días, pero la solicitud de cambio CC-01 sigue «pendiente de presentación al comité». El plan cambió sin autorización.
- «Diseño funcional aprobado» está cerrado sin acta.
- «Entregar el punto 40» (Carlos Peña) no tiene fecha.

La CC-01 de PRY-202 dice «autorizada por el comité» sin nombrar a nadie. El acta de comité del 2026-10-15 no la menciona. Eso lo noté al leer y no es una señal calculada.

### El portafolio completo
Faltan 10 proyectos (PRY-199 a 201 y 205 a 211) y 76 documentos, en 2 lotes uno tras otro. El registro de la corrida marca 88 segundos de cálculo para los 79 documentos. No tengo una cifra medida de cuánto tarda la lectura de los 76 restantes, pero será bastante más.

### Lo que le falta a tu carpeta
Ninguno de estos puntos bloquea nada.
- Ninguna acta dice hasta dónde puede decidir el gerente. Falta en los tres proyectos, y sin eso el control de cambios no sabe qué excede su facultad.
- Los alcances de las actas son genéricos («Componente 1, 2, 3»), así que no hay con qué contrastar un cambio de alcance.
- Casi no hay actas de recibo. Hay 1 de 4 hitos cerrados en PRY-202, 1 de 5 en PRY-203 y 0 de 1 en PRY-204.
- PRY-203 guarda `2026-10-15-notas-reunion.txt` fuera de `30-reuniones/`.
- PRY-207 y PRY-211 solo tienen acta e informe, sin cronograma ni reuniones.

### Cómo corrió
Hice 0 preguntas, porque era una sesión sin interfaz y tomé los valores sugeridos. No medí los minutos hasta el primer resultado. La corrida quedó registrada con id `2026-10-15-portfolio-setup-1`.

Corregí dos frases de `estado/corridas/salida-portfolio-setup.md` después de registrar la corrida. Una decía que PRY-210 no tenía reuniones recientes, y era falso. La otra daba un tiempo estimado sin base. El texto de arriba es el corregido, pero la copia que guardó la corrida puede traer todavía las frases viejas.

Puedo correr ahora el portafolio completo. Como eres PMO, también puedo publicar el estándar en una carpeta compartida para que los gerentes usen los mismos criterios.