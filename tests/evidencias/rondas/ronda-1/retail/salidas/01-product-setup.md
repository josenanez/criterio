# /criterio-product:product-setup documentos/productos/PRD-301

## Listo: Puntos de fidelización (PRD-301)

Hice la instalación sin preguntas, con la respuesta sugerida en cada una. Lo que no está dicho en ninguna parte de tu definición es mucho: nueve vacíos.

**Lo que miré:** 4 documentos, uno de descubrimiento (entrevistas del 2025-10-02). La definición y el caso de negocio son del 2026-07-30. Hay también un acta del comité del 2026-10-14. Pude leer todos los formatos.

**Cómo quedó configurado:**
- **Producto y gerente:** Puntos de fidelización, gerente Mauricio Pérez, tomado del caso de negocio.
- **Quién decide:** el Comité de producto. Ningún documento nombra a una persona con esa autoridad.
- **Dónde guardo lo que encuentro:** `.criterio/producto/PRD-301/estado`, fuera de la carpeta de documentación.
- **Términos:** la versión 1.0 de TERMS la aceptó José Francisco Ñáñez el 2026-10-14.
- **Cifras:** el cálculo del script salió vacío porque el registro de requerimientos aún no se levantó. Por eso no hay porcentajes ni conteos derivados. Las fechas son las de los documentos.

### Qué sostiene lo que afirma tu definición
| Afirmación | Sostenida por |
|---|---|
| «Clientes frecuentes» no tiene puntos de fidelización | Una sola cita, del 2025-10-02: «Lo necesito y hoy no lo tengo» |
| El volumen mensual es 200.866 | Solo el propio caso de negocio, que se cita a sí mismo |
| Habrá retorno en 24 meses | Nada: no hay cifra, método ni fuente |
| El proveedor cumple el tiempo pactado | Un supuesto marcado «verificado» el 2026-05-17, sin la verificación a la vista |

### Lo que no está dicho en ninguna parte
- **La única cita de demanda:** no dice de qué segmento es el cliente, y no nombra los puntos de fidelización. Según las fechas, tiene más de 12 meses, que es el umbral configurado.
- **El 200.866 mensual:** no hay serie medida con su fuente. Nadie está midiendo lo que el negocio afirmó.
- **El retorno:** solo dice «24 meses», sin cifra.
- **La propuesta y el criterio de éxito:** la propuesta dice solo «Propuesta principal», y no hay criterio de éxito en ningún documento.
- **REQ-1010, REQ-1011 y REQ-1012:** no tienen texto, solo el ID.
  - Los tres figuran como aceptados y pedidos por «Cliente entrevistado». La entrevista tiene una sola cita, que no se relaciona con ningún ID.
  - Los tres están aceptados desde antes de la definición (2026-07-30).
- **Quién los construye:** la definición dice «Ninguno declarado» y el comité muestra «—» como proyecto en los tres.
- **«Se mantiene el plan»:** no hay plan en la carpeta.

### Supuestos
Hay uno: «El proveedor cumple el tiempo pactado», declarado el 2026-05-17. No se nombra al proveedor ni el tiempo.

### Qué le falta a tu carpeta
- Las transcripciones completas de las entrevistas.
- La serie del volumen mensual, con su fuente.
- Las decisiones del comité con su motivo.
- El texto de cada requerimiento.

El resultado completo está en `.criterio/producto/PRD-301/estado/corridas/salida-product-setup.md`. La corrida quedó registrada como `2026-10-14-product-setup-1`.

Siguiente paso sugerido: `/product-discovery` sobre las entrevistas, para convertir los temas en requerimientos con la cita de quién los pidió.