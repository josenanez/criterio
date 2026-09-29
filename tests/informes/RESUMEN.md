# Resumen de las corridas

**5 corrida(s)**, de la del 2026-09-01 a la del 2026-09-29.

Cada día el mismo material se escribe con una disposición distinta y lo esperado no cambia. Una diferencia entre días no es ruido: es una dependencia que no sabíamos que teníamos.

## Día a día

| Día | Disposición | Docs | Tiempo | Aciertos | Falsos + | Falsos − | Precisión | Cobertura | Controles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | referencia | 462 | 3.2 s | 455 | 0 | 0 | 100.0% | 100.0% | ✓ |
| 2 | plana | 528 | 3.0 s | 530 | 0 | 0 | 100.0% | 100.0% | ✓ |
| 3 | revuelta | 577 | 3.5 s | 590 | 0 | 0 | 100.0% | 100.0% | ✓ |
| 4 | sin_carpeta | 622 | 3.0 s | 634 | 0 | 0 | 100.0% | 100.0% | ✓ |
| 5 | referencia | 657 | 3.4 s | 686 | 0 | 0 | 100.0% | 100.0% | ✓ |

## Qué se sostiene

| | Mínimo | Máximo | Mediana |
|---|---:|---:|---:|
| Precisión | 100.0% | 100.0% | 100.0% |
| Cobertura | 100.0% | 100.0% | 100.0% |
| ms por documento | 4.8 | 7.0 | 5.8 |

**La precisión no se movió entre disposiciones.** Con el material escrito de cuatro formas distintas, el agente reportó lo mismo: el recorrido no depende de cómo esté organizada la carpeta.

## Qué arreglar

Ninguna señal falló en ninguna corrida.

---

Lo que estas corridas **no** miden: la extracción con modelo, documentos que no sean markdown ni CSV, y una organización real. El material es sintético y su estructura se conoce.

