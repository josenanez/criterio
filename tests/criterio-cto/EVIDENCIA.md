# criterio-cto · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada vez,
byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el generador al
sembrar cada defecto; el motor no la ve. Los nombres, las empresas y los documentos son inventados.

## Las entidades

| Carpeta del material | País | Industria | Señales esperadas |
|---|---|---|---:|
| `banca-co` | Colombia | banca | 36 |
| `retail-mx` | México | retail | 36 |
| `tecnologia-cl` | Chile | tecnología | 24 |
| `control-co` | Colombia | banca | 0 |
| `control-mx` | México | retail | 0 |

Cada una trae su carpeta de tecnología al 25 de noviembre de 2026, con octubre como el periodo que se evalúa:
la política de cambios y de niveles de servicio en PDF y el catálogo de servicios en Excel; la exportación de
cambios y el registro de despliegues en Excel, con las actas del comité de cambios en PDF; los incidentes, los
problemas y la disponibilidad de octubre en Excel; el inventario de activos y las licencias en Excel, con las
actas del comité de arquitectura en PDF; el contrato de cada proveedor en PDF, con su cumplimiento y sus
facturas en Excel; y la factura y el presupuesto de la nube en Excel.

## Lo que se siembra, y la señal que tiene que levantar

La lista exacta está en la clave de cada entidad, en `esperado`. Las tres entidades sembradas traen las doce
señales: el banco y el retail, cada una tres veces, y la de software, dos. Cada repetición va en su propia
fila —otro cambio, otro activo, otro proveedor—, y la tabla dice la primera. Así la familia nace con más de
73 señales sembradas, la muestra que pide el piso del 95 % sin fallas (decisión 0020).

| Agente | Lo que se siembra | Señal |
|---|---|---|
| Fausto | La migración del servidor de archivos implementada el 6 de octubre sin aprobación: el acta la deja pendiente de más información | `change_without_approval` |
| Fausto | El reinicio de emergencia del clúster de base de datos, el 3 de octubre, sin revisión | `emergency_change_without_review` |
| Fausto | La actualización del sistema de nómina, aprobada y revertida, sin revisión | `failed_change_without_review` |
| Fausto | El despliegue del motor de reglas en producción, sin un cambio que lo autorice | `deployment_without_change` |
| Fausto | Un incidente mayor de pagos, resuelto el 4 de octubre, sin registro de problema | `major_incident_without_problem` |
| Fausto | Pagos en línea con 99,4 % de disponibilidad y un nivel acordado de 99,9 % | `service_below_level` |
| Domingo | El servidor de integración, sin dueño | `asset_without_owner` |
| Domingo | El servidor de la base de datos de clientes, sin soporte desde el 31 de diciembre de 2025 y sin excepción | `asset_out_of_support` |
| Domingo | 46 licencias de diseño gráfico en uso y 40 compradas | `license_shortfall` |
| Domingo | 190 de 600 licencias de videoconferencia sin uso, con una tolerancia del 15 % | `license_unused` |
| Domingo | Nube Andina con 99,7 % de disponibilidad y 99,95 % pactado, sin el crédito del 10 % en su factura | `vendor_breach_without_credit` |
| Domingo | La cuenta de analítica de la nube, 36 sobre un presupuesto de 30, con una tolerancia del 5 % | `cloud_over_budget` |

Las repeticiones: un cambio aprobado en la sesión siguiente a su implementación y otro sin aprobación; un
parche de emergencia revisado fuera del plazo y una reversión de emergencia sin revisión; dos cambios fallidos
más sin revisión; un despliegue con un cambio que no está en la exportación y otro sin cambio; un incidente
mayor con su problema sin causa y otro sin problema; dos servicios más por debajo de su nivel; dos activos más
sin dueño; un activo con la excepción vencida y otro sin excepción; dos programas más con menos licencias que
uso y dos con licencias sin uso; dos proveedores más sin su crédito; y dos cuentas más de la nube por encima de
su presupuesto.

## Lo que se parece a un defecto y no lo es

En todas las entidades, y sin nada más en las de control: un cambio aprobado el mismo día en que se implementó,
un cambio estándar sin aprobación por cambio, uno de emergencia revisado el último día del plazo, uno revertido
con su revisión, un despliegue sin cambio en el ambiente de pruebas, un incidente mayor resuelto hace menos días
que el plazo de la política, un servicio que da exactamente su nivel, un activo sin soporte con su excepción
vigente, uno sin soporte que no está en producción, una licencia con tantas en uso como compradas, un proveedor
que incumplió con su crédito en la factura y una cuenta de la nube por encima de su presupuesto dentro de la
tolerancia. Ninguno puede levantar una señal.

## Lo que el material no prueba

- **La extracción.** El evaluador escribe la ficha con la extracción correcta, de la clave. Que el agente
  procese las actas, las excepciones y los contratos, y los registre bien, lo prueba la ronda con los agentes,
  que viene en la 0.2.0. Cada aprobación, revisión, excepción y nivel de servicio se califica por separado,
  campo por campo.
- **Las exportaciones reales** de ServiceNow, Jira Service Management, Flexera o la facturación de AWS, Azure y
  Google Cloud: el material usa tablas con columnas en español; el setup mapea las de cualquier exportación.
- **La norma de la tecnología y de la nube fuera de Colombia**: está por verificar, y no sostiene ninguna señal.
- **El juicio del área**: si un cambio debió aprobarse, si un activo merece una excepción y qué dice un contrato.
