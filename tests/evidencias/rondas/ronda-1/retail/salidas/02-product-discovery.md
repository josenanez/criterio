# /criterio-product:product-discovery 

Leí las 4 piezas de PRD-301 y no salió ningún tema. Solo hay una entrevista, con una sola frase, y no pude cruzarla contra el registro porque falta `producto.json`, la ficha del producto.

**Términos:** José Francisco Ñáñez los aceptó (v1.0, 2026-10-14), igual que `TERMS.md`.

**Lo que leí**
- **Cliente:** una entrevista del 2025-10-02 con una cita: *«Lo necesito y hoy no lo tengo.»* No dice qué es «lo», así que no se puede atribuir a puntos de fidelización ni a ningún requerimiento. Queda registrada como dicha una sola vez, sin promoverla ni descartarla.
- **Cifras:** no hay afirmaciones numéricas de entrevistados. El `volumen_mensual` de 200.866 viene del caso de negocio, no de un cliente, y no hay serie medida que lo respalde.
- **Fuentes públicas:** no entró ninguna.
- **Comité del 2026-10-14:** REQ-1010, REQ-1011 y REQ-1012 están aceptados y los tres citan como origen al «Cliente entrevistado». Esa única entrevista no menciona ninguno de ellos.
- **Proyectos:** ninguno de los tres requerimientos tiene proyecto que lo ejecute, y la definición dice «Ninguno declarado».

**Lo que no se hizo**
- **`sellar`:** lo rechazó porque `producto.json` no se escribió en esta corrida, y este comando no la escribe. Los 4 documentos quedan sin sellar, así que la próxima corrida los vuelve a leer.
- **`compute`:** devolvió el producto vacío (0 requerimientos, código «?») por la misma razón, así que no hay cifras recalculadas.
- **Requerimientos:** no creé ninguno.

**Registro de la corrida:** id `2026-10-14-product-discovery-1`, 24 segundos. La salida completa está en `.criterio/producto/PRD-301/estado/corridas/salida-product-discovery.md`.

**Siguiente paso:** correr `/criterio-product:product-setup` o `/criterio-product:product-requirements` para generar la ficha. Después se puede repetir el descubrimiento y cruzar contra los requerimientos.