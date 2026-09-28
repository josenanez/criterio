# Resumen de las corridas

**3 corrida(s)**, de la del 2026-09-28 a la del 2026-09-28.

Cada día el mismo material se escribe con una disposición distinta y lo esperado no cambia. Una diferencia entre días no es ruido: es una dependencia que no sabíamos que teníamos.

## Día a día

| Día | Disposición | Docs | Tiempo | Aciertos | Falsos + | Falsos − | Precisión | Cobertura | Controles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | referencia | 406 | 3.0 s | 448 | 0 | 0 | 100.0% | 100.0% | ✓ |
| 2 | plana | 463 | 2.9 s | 512 | 0 | 0 | 100.0% | 100.0% | ✓ |
| 3 | revuelta | 515 | 3.3 s | 614 | 0 | 0 | 100.0% | 100.0% | ✓ |

## Qué se sostiene

| | Mínimo | Máximo | Mediana |
|---|---:|---:|---:|
| Precisión | 100.0% | 100.0% | 100.0% |
| Cobertura | 100.0% | 100.0% | 100.0% |
| ms por documento | 6.4 | 7.3 | 6.5 |

**La precisión no se movió entre disposiciones.** Con el material escrito de cuatro formas distintas, el agente reportó lo mismo: el recorrido no depende de cómo esté organizada la carpeta.

## Qué arreglar

Ninguna señal falló en ninguna corrida.

---

Lo que estas corridas **no** miden: la extracción con modelo, documentos que no sean markdown ni CSV, y una organización real. El material es sintético y su estructura se conoce.

