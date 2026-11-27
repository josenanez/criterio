# /criterio-claims:claim-check 

Los términos 1.6 están vigentes y no hubo que registrar la aceptación otra vez. En la primera corrida usé el periodo 2026-11 y el reporte salió vacío, porque las afirmaciones están en la ficha de 2026-10. Corrí de nuevo con 2026-10, que es el periodo de las piezas, los soportes y el informe. Esa primera corrida dejó un reporte vacío en `piezas/2026-11/`.

Cuatro de las diez afirmaciones requieren atención:

- **Sin soporte en la carpeta:**
  - P-03: «9 de cada 10 clientes nos recomiendan.»
  - P-12: «Atención en menos de 5 minutos en todas las sucursales.»
- **Comparativas que no citan fuente ni fecha:**
  - P-02: «El precio más bajo del mercado en la canasta básica.»
  - P-22: «Más barato que cualquier otra cadena en útiles escolares.»

  Las dos tienen un comparativo en `20-soportes/`, pero la pieza no cita su fuente ni su fecha.

Las otras seis afirmaciones tienen un soporte en la carpeta. Si ese soporte basta lo decide legal.

El reporte completo está en `estado-mercadeo/cms210415xy3-consumo-maya-sintetico/piezas/2026-10/reporte-claim-check.md`. La salida que te mostré quedó en `corridas/salida-claim-check.md`. La corrida se registró como `2026-11-25-claim-check-1`, con 12 hallazgos.

El motor contó 12 hallazgos porque suma los de otros comandos que no se piden aquí: aprobaciones, bases de contactos y promociones.