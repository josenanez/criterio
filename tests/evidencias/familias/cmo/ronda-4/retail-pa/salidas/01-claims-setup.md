# /criterio-claims:claims-setup mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos

Lucía quedó configurada para Almacenes del Canal Sintéticos (155634567-2-2020) con el periodo 2026-10. En la primera revisión de afirmaciones salen dos sin soporte y dos comparaciones con la competencia que no dicen su fuente ni su fecha en la pieza.

**Lo que quedó listo**
- **Configuración:** `.criterio/piezas/155634567-2-2020/config.json`. Las tolerancias son las de la política: 5 % sobre el presupuesto y 2 % de diferencia con la plataforma. El estado se guarda en `estado-mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos` y lo que encuentre se publica en Rostrum.
- **Términos 1.6:** José Francisco Ñáñez los aceptó con fecha 2026-11-25. El comprobante está en `.criterio/terminos/aceptacion-criterio-claims-1.1.0-2026-11-25.md` y `.pdf`.
- **Marca:** el archivo `_CRITERIO_MERCADEO.txt` quedó en la carpeta de la entidad.

**Respuestas que tomé sin preguntar (no había nadie para responder)**
- La carpeta era la única que apareció.
- El país, PA, lo saqué del formato de la identificación fiscal. La moneda, USD, la supuse por ser Panamá: ningún documento la dice, así que conviene confirmarla.
- El periodo, 2026-10, sale de los comparativos y del informe de resultados.

Procesé las 10 piezas, las crucé contra los 7 soportes y procesé las bases de las 3 promociones.

| # | Pieza | Qué falta |
|---|---|---|
| 1 | P-03 | «9 de cada 10 clientes nos recomiendan.» no tiene soporte en la carpeta |
| 2 | P-12 | «Atención en menos de 5 minutos en todas las sucursales.» no tiene soporte en la carpeta |
| 3 | P-02 | «El precio más bajo del mercado en la canasta básica.» es una comparación y la pieza no dice su fuente ni su fecha |
| 4 | P-22 | «Más barato que cualquier otra cadena en útiles escolares.» es una comparación y la pieza no dice su fuente ni su fecha |

Las otras seis afirmaciones tienen un soporte que trata de lo mismo; si ese soporte basta lo decide legal. El reporte completo está en `estado-mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos/piezas/2026-10/reporte-claim-check.md`.

El cálculo del periodo encontró 12 señales en total. Las 8 que esta revisión no cubre son:
- dos piezas publicadas sin aprobación;
- dos piezas pagadas a influenciadores sin identificarse como publicidad;
- dos bases de contactos sin autorización para mercadeo;
- dos promociones a las que les faltan condiciones.

Esas las revisan `/criterio-claims:approval-check` y `/criterio-claims:promo-check`.

**Sin tarea diaria:** no creé la revisión automática porque eso exige un sí explícito. Se corre a mano con `/criterio-claims:claims-wake`.

**Corrida registrada:** quedó como `2026-11-25-claims-setup-1`. El archivo de salida de esa corrida remite al reporte en vez de copiarlo entero, aunque el comando pide copiarlo tal cual.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.