---
marp: true
title: "model-diet"
header: 'Construcción de Modelos'
footer: 'Introducción a la Programación Lineal'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>

# Problema de la Dieta

En un centro de nutrición de desea obtener la dieta de coste mínimo con unos determinados requisitos vitamínicos para un grupo de niños que van a asistir a campamentos de verano. El especialista estima que la dieta debe contener entre 26 y 32 unidades de vitamina $A$, al menos 25 unidades de vitamina $B$ y 30 de $C$, y, a lo sumo, 14 de vitamina $D$. 

Se desea **construir un modelo de programación lineal** para conocer la cantidad de cada alimento que hay que preparar y que satisfaga los requisitos propuestos **con coste mínimo**.

---

La siguiente tabla nos da el número de unidades de las distintas vitaminas por unidad de alimento consumido para seis alimentos elegidos, denominados $1, 2, 3, 4, 5, 6,$ así como su coste por unidad

<br>

| Alimentos | $A$ | $B$ | $C$ | $D$| costo \$ / unidad |
|-----------|---|---|---|---|-------------------|
| 1         | 1 | 1 | 0 | 1 | 10                |
| 2         | 1 | 2 | 1 | 0 | 14                |
| 3         | 0 | 1 | 2 | 0 | 12                |
| 4         | 3 | 1 | 0 | 1 | 18                |
| 5         | 2 | 1 | 2 | 0 | 20                |
| 6         | 1 | 0 | 2 | 1 | 16                |

---

<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>