# /criterio-product:product-wake 

Hoy tocaba la revisión del registro de Gemelo digital (PRD-303). No encontré ninguna señal que haya cruzado un umbral, porque el registro está vacío y no hay un corte anterior con qué comparar.

- **Términos:** los de José Francisco Ñáñez (versión 1.0, 2026-10-14) coinciden con la versión vigente de `TERMS.md`, así que seguí.
- **Registro:** `estado/producto.json` no tiene identidad, problema, éxito, afirmaciones ni supuestos. El cálculo da 0 requerimientos, así que no puedo decir qué está sin decidir, sin verificar o envejecido, y no lo inventé.
- **Documentos sin registrar:** hay cinco en la carpeta del producto y no los leí.
  - La definición y el caso de negocio, del 2025-12-09.
  - Las entrevistas del 2026-08-31.
  - El tablero de métricas del 2026-10-12.
  - El acta del comité de producto del 2026-10-10.
  
  Para cargarlos hay que correr `/product-definition`, `/product-discovery` y `/product-requirements`. Este comando no las lanza solo.
- **Trazas:** ninguna se da por confirmada, porque la carpeta de fichas configurada (`estado/fichas`) no existe. Las fichas de proyecto están en `estado/portafolio/records`. No sustituí la ruta por mi cuenta; si esa es la correcta, hay que cambiar `paths.fichas` en la configuración.

Dejé registrados la revisión, el corte de hoy y la corrida (`2026-10-14-product-wake-1`, 24 segundos). La salida completa quedó en `estado/corridas/salida-product-wake.md`.

Vuelvo el 2026-11-13.