---
marp: true
title: "model-production-planning"
header: 'Construcción de Modelos'
footer: 'Introducción a la Programación Lineal'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>

# Planificación de la producción

Una empresa produce filtros para monitores de ordenador formados por tres capas, una intermedia de calidad $A$ y otras dos exteriores de calidad $B$ que envuelven a la anterior. Ambas calidades se consiguen con diferentes mezclas de fibra de vidrio y resina de las que el fabricante dispone  por semana de 700 y 900 toneladas ($t$), respectivamente. 

La empresa posee cuatro plantas de producción que utilizan procedimientos de fabricación que difieren en las cantidades e materia prima que utilizan. Las cantidades necesarias de materia prima por operación para cada planta que se pueden llevar a cabo total o parcialmente así como el número de capas producidas de uno y otro tipo, se tienen en la Tabla 1.

---

| Planta | Vidrio | Resina |Producción Tipo $A$ |Producción Tipo $B$ |
|--------|--------|--------|----------|----------|
| 1      | 15     | 19     | 2        | 5        |
| 2      | 14     | 20     | 3        | 7        |
| 3      | 16     | 15     | 5        | 4        |
| 4      | 12     | 18     | 4        | 4        |


Formular un modelo de programación lineal para determinar el número de operaciones a realizar en cada planta de manera que sea máximo el número total de filtros fabricados

---

Para la formulación de la función objetivo hay que tomar en cuenta que para formar un filtro se necesita 1 unidad de $A$ y dos unidades de $B$, por ejemplo, si decidimos ejecutar una operación en cada planta obtendríamos 14 unidades de $A$ y 20 unidades de $B$ y con estas unidades solo se pueden elaborar 10 filtros.


<br>

$$
\begin{align*}
    A = 2(1) + 3(1) + 5(1) + 4(1)  &= 14\\
    B = 5(1) + 7(1) + 4(1) + 4(1)  &= 20\\
\end{align*}
$$

---

$$
\begin{align*}
    Z_A &= \frac{A}{1} = \frac{14}{1} = 14\\[3mm]
    Z_B &= \frac{B}{2} = \frac{20}{2} = 10\\[6mm]
    Z &= \min\{Z_A, Z_B \}\\
    &= \min\{14, 10 \} = 10
\end{align*}
$$

<img src="https://res.cloudinary.com/rafaeltorrese/image/upload/v1708524471/operations-research/02_linear-programming-introduction/05_production-planning.png" class="center" width="1000" height="1000">


---

<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>