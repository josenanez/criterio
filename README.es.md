# Criterio

**Plugins que leen la documentación que una organización ya tiene, y dicen qué muestra de verdad.**

[English](README.md) · [Términos de uso](TERMS.es.md) · [Descargo](DISCLAIMER.es.md) · [Cómo aportar](CONTRIBUTING.es.md)

---

Casi toda herramienta de trabajo ayuda a producir un documento más. El problema de una organización real rara vez es que falte una plantilla: es que **nadie ha leído juntos** los cientos de documentos que ya existen.

Criterio los lee, guarda lo que encontró con una cita por cada dato, y en la corrida siguiente dice qué cambió.

> **Esto produce borradores de trabajo, no decisiones, y aquí nadie ha certificado nada.** Toda salida debe verificarla alguien competente antes de actuar. Lea [TERMS.es.md](TERMS.es.md) antes de instalar. Usar estos plugins implica aceptar esos términos.

---

## Qué existe hoy

| Plugin | Estado | Qué hace |
|---|---|---|
| `criterio-pmo` | **6 skills, 10 comandos** | Portafolio de proyectos: lee una carpeta de documentación, mantiene una ficha por proyecto, y reporta qué cambió, qué se contradice, qué lleva semanas en silencio y qué no sustenta ningún documento |
| `criterio-legal` | Declarado, sin construir | Revisión de contratos con criterio de derecho civil |
| `criterio-finance` | Declarado, sin construir | Cierre mensual y reportes |

---

## Cómo funciona

Dos principios lo sostienen todo.

**El modelo extrae; el script calcula.** Leer una fecha es lectura. Restar días, proyectar desviación y sumar ejecutado contra comprometido es aritmética, y la aritmética va en código, donde es determinística y se puede probar.

**Todo dato lleva su cita o declara que no está.** "No está dicho en ninguna parte" es un hallazgo válido y esperado. Sin trazabilidad no se defiende nada ante un comité.

La espina es una **ficha por sujeto** — en `criterio-pmo`, una por proyecto — que todos los comandos leen y escriben. Ningún comando lee documentos crudos por su cuenta. Eso permite consolidar cuarenta proyectos sin volver a leerlos, calcular en vez de opinar, y comparar una corrida contra la anterior.

---

## Instalación

Criterio es un marketplace de plugins. Se agrega una vez y los plugins vienen con él.

**Claude Cowork**

1. Abra **Personalizar** (abajo a la izquierda)
2. **Explorar plugins** → **Personal** → **+**
3. **Agregar marketplace desde GitHub**
4. Escriba `josenanez-company/criterio`

**Claude Code**

```
claude plugins marketplace add josenanez-company/criterio
```

En la primera corrida el plugin muestra los términos y no produce un análisis completo hasta que la aceptación quede registrada en su archivo local. Es deliberado: ver [docs/acceptance.md](docs/acceptance.md).

---

## Cómo verificar que esto sirve

Cada plugin lleva su propio `ACCEPTANCE.md`: qué significa "funciona" para él y el umbral que debe alcanzar. Nada se publica hasta que sus criterios pasen sobre el material sintético de `tests/`, y el resultado de esa corrida se publica con la versión.

```
python3 scripts/validate_plugins.py
```

---

## Licencia

Apache 2.0. Ver [LICENSE](LICENSE) y [NOTICE](NOTICE).

---

Mantenido por [José Francisco Ñáñez](https://josenanez.com).
