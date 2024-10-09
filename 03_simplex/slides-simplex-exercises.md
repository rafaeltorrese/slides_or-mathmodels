---
marp: true
title: "slides-simplex-exercises"
header: 'Ejercicios'
footer: 'Algoritmo Simplex'
author: Rafael Torres Escobar
paginate: true
---



<!-- _paginate: false -->

<p class="outstanding-title">Algoritmo Simplex</p>
<p class="outstanding-subtitle">Ejemplos</p>

# Riser Sports Products

Reiser Sports Products quiere determinar la cantidad de balones de futbol de All-Pro (A) y Universitario (U) a producir **con el ﬁn de maximizar las utilidades** durante el siguiente horizonte de planeación de cuatro semanas. 

Las restricciones que afectan las cantidades de producción son las capacidades de producción en tres departamentos: corte y teñido, costura e inspección y empaque. 


---

- Para el periodo de planeación de cuatro semanas se dispone de 340 horas de corte y teñido, 420 horas de costura y 200 horas de inspección y empaque. 
- Los tiempos requeridos para elaborar un balón A y U en el departamento de corte y teñido son de 12 y 6 horas respectivamente. 
- El departamento de costura requiere 9 horas para un balón A y 6 horas para elaborar un balón U. 
- En la inspección se ocupan 6 horas para cada balón de fútbol. 
- Los balones de futbol All-Pro producen utilidades de \$5 por unidad y los balones Universitarios producen una utilidad de \$4 por unidad. 

Formule un modelo para el problema.

## Modelo

$$\max Z = 5A + 4U$$

<br>

$$
\begin{matrix}
12A &+ &6U &\leq & 340\\
9A &+ &6U &\leq & 420\\
6A &+ &6U &\leq & 200\\
\end{matrix}
$$

<br>

$$A, U \geq 0$$


## Forma Estándar

$$\max Z = 5A + 4U + 0S_1 + 0S_2 + 0S_3$$

<br>

$$
\begin{matrix}
12A &+& 6U &+& S_1 &&&= & 340\\
9A &+& 6U &&+ &S_2&&= & 420\\
6A &+& 6U &&&+  &S_3 &= & 200\\
\end{matrix}
$$

<br>

$$A, U, S_1, S_2, S_3 \geq 0$$


## Tabla Inicial

Puedes consultar la tabla inicial en este enlace: <a href="https://docs.google.com/spreadsheets/d/1I0tZIHKtVm7hAU4rvvx5PTBuVDhjOnZ69GfDMFmYDrc/edit?usp=sharing" target="_blank">Ejemplo del Problema Riser Sports</a>

| max | cj ->   | 5  | 4  |    |    |    |     |
|-----|---------|----|----|----|----|----|----:|
| cb  | basis   | x1 | x2 | s1 | s2 | s3 |   b |
|     |         | 12 | 6  | 1  | 0  | 0  | 340 |
|     |         | 9  | 6  | 0  | 1  | 0  | 420 |
|     |         | 6  | 6  | 0  | 0  | 1  | 200 |
|     | zj      |    |    |    |    |    |     |
|     | cj - zj |    |    |    |    |    |     |


# Problema de la Dieta

En un centro de nutrición de desea obtener la dieta de coste mínimo con unos determinados requisitos vitamínicos para un grupo de niños que van a asistir a campamentos de verano. El especialista estima que la dieta debe contener entre 26 y 32 unidades de vitamina $A$, al menos 25 unidades de vitamina $B$ y 30 de $C$, y, a lo sumo, 14 de vitamina $D$. 

Se desea **construir un modelo de programación lineal** para conocer la cantidad de cada alimento que hay que preparar y que satisfaga los requisitos propuestos **con coste mínimo**.

---

La siguiente tabla nos da el número de unidades de las distintas vitaminas por unidad de alimento consumido para seis alimentos elegidos, denominados $1, 2, 3, 4, 5, 6,$ así como su coste por unidad

<br>

| Alimentos | $A$ | $B$ | $C$ | $D$ | costo \$ / unidad |
|-----------|-----|-----|-----|-----|-------------------|
| 1         | 1   | 1   | 0   | 1   | 10                |
| 2         | 1   | 2   | 1   | 0   | 14                |
| 3         | 0   | 1   | 2   | 0   | 12                |
| 4         | 3   | 1   | 0   | 1   | 18                |
| 5         | 2   | 1   | 2   | 0   | 20                |
| 6         | 1   | 0   | 2   | 1   | 16                |

## Modelo

$$\min Z = 10x_1 + 14x_2 + 12x_3 + 18x_4 + 20x_5 + 16x_6$$

<br>
sujeto a
<br>

$$
\begin{align*}
1x_1 + 1x_2 + 0x_3 + 3x_4 + 2x_5 + 1x_6 \geq 26\\
1x_1 + 1x_2 + 0x_3 + 3x_4 + 2x_5 + 1x_6 \leq 32\\
1x_1 + 2x_2 + 1x_3 + 1x_4 + 1x_5 + 0x_6 \geq 25\\
0x_1 + 1x_2 + 2x_3 + 0x_4 + 2x_5 + 2x_6 \geq 30\\
1x_1 + 0x_2 + 0x_3 + 1x_4 + 0x_5 + 1x_6 \leq 14
\end{align*}
$$

<br>

$$x_1, x_2, x_3, x_4,x_5,x_6 \geq 0$$


## forma estándar

$$\min Z = 10x_1 + 14x_2 + 12x_3 + 18x_4 + 20x_5 + 16x_6 + 0\left(\sum_{j=1}^{6} S_j \right) $$

sujeto a

<br>

$$
\begin{matrix}
1x_1 + 1x_2 + 0x_3 + 3x_4 + 2x_5 + 1x_6 & - S_1  &&&&& = 26\\
1x_1 + 1x_2 + 0x_3 + 3x_4 + 2x_5 + 1x_6 &&+ S_2  &&&&  = 32\\
1x_1 + 2x_2 + 1x_3 + 1x_4 + 1x_5 + 0x_6 &&&- S_3 &&&   = 25\\
0x_1 + 1x_2 + 2x_3 + 0x_4 + 2x_5 + 2x_6 &&&&- S_4  && = 30\\
1x_1 + 0x_2 + 0x_3 + 1x_4 + 0x_5 + 1x_6 &&&&&+ S_5  & = 14
\end{matrix}
$$

<br>

$$x_1, x_2, x_3, x_4,x_5,x_6, S_1, S_2, S_3,S_4, S_5, S_6,  \geq 0$$

## Tabla Inicial Simplex

Consulta la tabla inicial en el siguiente enlace <a href="https://docs.google.com/spreadsheets/d/1hqa2FUHXCM1ocQmGhX2ZmfK4J-vDXtDqanE62OsKjEY/edit?usp=sharing" target="_blank">Problema de la Dieta</a>


| Min | cj -->  | 10 | 14 | 12 | 18 | 20 | 16 |    |    |    |    |    |    |
|-----|---------|----|----|----|----|----|----|----|----|----|----|----|----|
| cb  | basis   | x1 | x2 | x3 | x4 | x5 | x6 | s1 | s2 | s3 | s4 | s5 |    |
|     |         | 1  | 1  | 0  | 3  | 2  | 1  | -1 | 0  | 0  | 0  | 0  | 26 |
|     |         | 1  | 1  | 0  | 3  | 2  | 1  | 0  | 1  | 0  | 0  | 0  | 32 |
|     |         | 1  | 2  | 1  | 1  | 1  | 0  | 0  | 0  | -1 | 0  | 0  | 25 |
|     |         | 0  | 1  | 2  | 0  | 2  | 2  | 0  | 0  | 0  | -1 | 0  | 30 |
|     |         | 1  | 0  | 0  | 1  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 14 |
|     | zj      |    |    |    |    |    |    |    |    |    |    |    |    |
|     | cj - zj | 10 | 14 | 12 | 18 | 20 | 16 | 0  | 0  | 0  | 0  | 0  |    |
|     |         |    |    |    |    |    |    |    |    |    |    |    |    |

---

<!-- _paginate: hold -->
<p class="outstanding-title">Algoritmo Simplex</p>
<p class="outstanding-subtitle">Ejemplos</p>

