---
marp: true
title: "model-gasoline-production"
header: 'Construcción de Modelos'
footer: 'Introducción a la Programación Lineal'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>


# Producción de gasolinas

Una compañía de petróleos produce tres tipos de gosolinas: Súper, Normal y Euro. Se obtienen por mezcla de tres calidades de crudos ($A$,$B$,$C$) que contienen tres componentes (1,2,3). La participación de estos componentes en la composición de cada crudo se muestra en la Tabla 1 en porcentaje 


Tabla 1: Composición de cada Crudo en Porcentajes
| Crudos | 1  | 2  | 3  |
|--------|----|----|----|
| A      | 8  | 10 | 5  |
| B      | 45 | 30 | 20 |
| C      | 30 | 40 | 25 |


---

y las especificaciones de los tres tipos de gasolina en la Tabla 2 (porcentaje):

Tabla 2: Especificaciones en Porcentajes
|        | 1         | 2         | 3         |
|--------|-----------|-----------|-----------|
| Super  | $\geq$ 60 | $\leq$ 25 | $\geq$ 10 |
| Normal | $\geq$ 50 | $\leq$ 30 | $\leq$ 15 |
| Euro   | $\leq$ 40 | $\geq$ 35 | $\geq$ 20 |

---

Los costes por barril de crudos $A$, $B$ y $C$ son 650, 500 y 450 $, respectívamente. El presupuesto diario de compra es de 50 millones \$; la disponibilidad diaria de crudos $B$ y $C$ se limita, respectivamente, a 3,000 y 7,000 barriles. Ciertos acuerdos obligan a comprar al menos 2,500 barriles de $A$ por día. 

Las demandas de gasolina Súper y Normal son de 2,000 y 2,500 barriles diarios, que deben satisfacerse. La compañía desea **maximizar la producción** de gasolina Euro. Formular un **modelo de programación lineal** que dé respuesta al problema planteado por la compañía.

---

<img src="https://res.cloudinary.com/rafaeltorrese/image/upload/v1708524471/operations-research/02_linear-programming-introduction/03_gasoline-production.png" class="center" width="800" height="800">

---

<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>