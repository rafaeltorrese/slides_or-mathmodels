---
marp: true
title: "model-blending-planning-chemical-factory"
header: 'Construcción de Modelos'
footer: 'Introducción a la Programación Lineal'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>

# Planificación de mezclas en una planta química 



Una planta química fabrica dos productos $A$, $B$ mediante dos procesos I y II. La tabla da los tiempos de producción de $A$ y $B$ en cada proceso y los beneficios (en miles de dólares) por unidod vendida

<br>



|Proceso| $A$ | $B$
|-----|-----|-----
I | 2 | 3
II | 3 | 4
Beneficio/ u | 4 | 10


---

Se dispone de 16 horas de operación del proceso I y de 24 horas del proceso II. La producción de $B$ da, además, un subproducto $C$ (sin coste adicional) que puede venderse a 3000 \$/u. Sin embargo, el sobrante de $C$ debe destruirse con coste 2000 \$/u. Se obtienen 2 unidades de $C$ por cada unidad de $B$ producida. La demanda de $C$ se estima en, a lo sumo, 5 unidades. 

Formular un programa lineal que dé el plan de producción con máximo beneficio.

---

<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>