# /criterio-roles:profile-map 

Resultado del mapa de los perfiles del periodo 2026-11: un solapamiento (PT-01 y PT-02) y un perfil sin ocupación (PT-04).

**Lo que hay que atender**
- PT-01 · Cajero de tienda y PT-02 · Cajero de autoservicio comparten la ocupación 41-2011.00 y el 67 % de sus requisitos.

**El resultado**
| Perfil | Ocupación |
|---|---|
| PT-01 · Cajero de tienda | 41-2011.00 · Cashiers (synthetic) |
| PT-02 · Cajero de autoservicio | 41-2011.00 · Cashiers (synthetic) |
| PT-03 · Supervisor de tienda | 41-1011.00 · First-Line Supervisors of Retail Sales Workers (synthetic) |
| PT-04 · Almacenista | — |

**Lo que no se pudo procesar:** nada; todo lo que llegó se procesó.

**Las preguntas que hizo el motor**
- ¿Qué código O*NET tiene PT-04? El perfil dice «sin código», así que queda vacío hasta que una persona lo confirme.
- ¿Qué fecha de próxima revisión tiene PT-01? El perfil dice «cada 12 meses», sin fecha, así que se registra sin fecha y rige la política.

**Fuentes:** `10-perfiles/PT-01_cajero-de-tienda.docx`, `10-perfiles/PT-02_cajero-de-autoservicio.docx`; fuentes técnicas F-02 y F-14.

Notas de la corrida:
- Los términos estaban vigentes (versión 1.6), así que no hizo falta registrar una aceptación nueva. No registré el nombre de José Francisco Ñáñez porque el comando no mostró ninguna aceptación pendiente.
- El reporte no trae ninguna ocupación afín sin perfil.
- La corrida quedó registrada como `2026-11-16-profile-map-1`.

Archivos, todos bajo `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos/`:
- `perfiles/2026-11/reporte-profile-map.md`
- `corridas/salida-profile-map.md`