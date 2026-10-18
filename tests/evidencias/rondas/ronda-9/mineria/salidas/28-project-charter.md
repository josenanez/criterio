# /criterio-portfolio:project-charter PRY-206 revisar

Revisé el acta de constitución de PRY-206 (Red privada LTE en mina), del 2026-02-25. Está incompleta y varios de sus campos son texto de plantilla.

Los términos ya estaban vigentes (versión 1.1, aceptados el 2026-10-17 por José Francisco Ñáñez), así que no hubo que pedirlos de nuevo. Leí el acta, el cronograma v1, el informe de avance del 2026-10-15 y la ficha del proyecto.

**Lo que falta y su consecuencia**
- **Autoridad del gerente:** no está en ningún documento. Todo cambio, por pequeño que sea, tiene que subir al Comité de Seguridad. Con 487.051.150 COP ya comprometidos de 1.200.000.000, esto pasa a diario.
- **Supuestos, restricciones, quién mide el éxito y cadencia del comité:** no están.
- **Alcance, exclusiones y criterio de éxito:** son de plantilla. El alcance dice «Componente 1, 2, 3» y las exclusiones dicen «Lo que otro proyecto cubre», sin nombrar nada. «En producción y medido» no dice qué se mide ni con qué umbral. Por eso no se puede verificar que el primer ensayo de disponibilidad «no alcanzó lo pactado»: el acta no recoge qué se pactó.
- **Objetivo de negocio:** describe la solución («Entregar red privada LTE en mina para Logística»), no un resultado medible.
- **Dependencias:** el acta dice «ninguna», pero el informe muestra una con operaciones, por la ventana de parada de planta.
- **Cubiertos:** patrocinador (Natalia Ospina) y gerente (Óscar Ramírez), ambos con nombre de persona.

**Qué no pude confirmar**
- El hito «Ingeniería básica aprobada» figura cerrado en el cronograma, pero no hay documento de aprobación en la carpeta.
- No sé si el permiso ambiental que menciona el informe es el mismo del hito «Licencia y permisos obtenidos».
- Si el comité acordó algo de palabra (autoridad, umbrales), no consta y no lo sé.

Lo que no está, lo dejé como pendiente de definir, sin completarlo.

**Siguientes pasos que ofrezco**
- Llevar la definición de la autoridad del gerente al comité con `/steering-pack`.
- Pasar la ventana de parada de planta, el acceso a la mina y la dependencia con operaciones al registro RAID con `/raid-log`.

La corrida quedó registrada como `2026-10-17-project-charter-1`, con 30 segundos medidos. La salida completa está en `estado/corridas/salida-project-charter.md`.