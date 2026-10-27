# /criterio-assistant:ea-scan 

Procesé la oficina de Gerencia general: escribí 4 ffichas de sesión y 3 de correo. El motor no levantó ninguna señal ni `record_issues`. Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez, así que no hizo falta pedirlos. Todas las llamadas al motor llevaron `--today 2026-10-26`, salvo `convertir`, que no la acepta.

```
# Procesar · Distribuidora Control · al 2026-10-26 · oficina de Gerencia general

**Entidad:** Distribuidora Control · **Fecha de corte:** 2026-10-26 · **Procesado:** 2026-10-26 · **Agente:** Ofelia, versión 0.12.0 · **Comando:** `ea-scan`

## Lo que hay que atender
Nada abierto en lo que procesa este comando.

## El resultado
No se publica en Rostrum: así lo dice la configuración.

## Lo que no se pudo procesar
- `90-borradores/LEEME.txt`: un archivo en 90-borradores/ sin «BORRADOR» en el nombre

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- Sin documentos citados.
```

- **Sin señales:** el reporte sale vacío, aunque las fichas sí recogen contenido. El acta de la junta del 2026-09-24 deja un compromiso abierto, el plan de continuidad de Jorge Silva, ahora para el 2026-11-20. También deja una decisión pendiente sobre el proveedor del centro de datos, con oferta vigente hasta el 2026-12-18.
- **Cumplido con evidencia:** el informe de cartera de Camilo Prieto quedó como cumplido, porque el informe de gestión de esa sesión dice que lo presentó el 2026-10-14.
- **Sin ficha de correo:** las dos respuestas de la oficina (al cliente y al supervisor) están guardadas y no llevan ficha. Los otros tres correos sí la tienen, y el motor no marca ninguno como pendiente.
- **Notas sin acta:** las notas del comité de gerencia del 2026-09-21 y del 2026-10-19 mencionan que Natalia Rincón revisará los indicadores de servicio para el 2026-11-06. No las pasé a compromisos porque solo vale el acta firmada, y el comité del 2026-10-19 no tiene acta.
- **Archivos que el motor no pudo procesar:** `LEEME.txt` en `90-borradores/` no lleva «BORRADOR» en el nombre. El `.ics` figuró como «formato .ics no reconocido» al convertir, pero `agenda` sí lo procesó, sin cruces ni ambiguos.

La corrida quedó registrada como `2026-10-26-ea-scan-1`, con la salida en `corridas/salida-ea-scan.md`.