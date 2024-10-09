---
marp: true
title: "slides-simplex-examples"
header: 'Ejemplos'
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

## Solución Óptima

| $\max Z$ | $cj \to$    | 5     | 4     | 0     | 0     | 0     |            |
|----------|-------------|-------|-------|-------|-------|-------|------------|
| $C_b$    | basis       | $x_1$ | $x_2$ | $S_1$ | $S_2$ | $S_3$ | $b$        |
| 5        | $x_1$       | 1.00  | 0.00  | 0.17  | 0.00  | -0.17 | 23.33      |
| 0        | $S_2$       | 0.00  | 0.00  | -0.50 | 1.00  | -0.50 | 150.00     |
| 4        | $x_2$       | 0.00  | 1.00  | -0.17 | 0.00  | 0.33  | 10.00      |
|          | $z_j$       | 5.00  | 4.00  | 0.17  | 0.00  | 0.50  | **156.67** |
|          | $c_j - z_j$ | 0.00  | 0.00  | -0.17 | 0.00  | -0.50 | Optimal    |


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

$$\min Z = 10x_1 + 14x_2 + 12x_3 + 18x_4 + 20x_5 + 16x_6 + 0\left(\sum_{j=1}^{5} S_j \right) $$

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

$$x_1, x_2, x_3, x_4,x_5,x_6, S_1, S_2, S_3,S_4, S_5,  \geq 0$$

## Tabla Inicial Simplex

Consulta la tabla inicial en el siguiente enlace <a href="https://docs.google.com/spreadsheets/d/1hqa2FUHXCM1ocQmGhX2ZmfK4J-vDXtDqanE62OsKjEY/edit?usp=sharing" target="_blank">Problema de la Dieta</a>


| Min   | $c_j$ -->   | 10    | 14    | 12    | 18    | 20    | 16    |       |       |       |       |       |     |
|-------|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-----|
| $C_b$ | basis       | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | $x_6$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | $s_5$ | $b$ |
|       |             | 1     | 1     | 0     | 3     | 2     | 1     | -1    | 0     | 0     | 0     | 0     | 26  |
|       |             | 1     | 1     | 0     | 3     | 2     | 1     | 0     | 1     | 0     | 0     | 0     | 32  |
|       |             | 1     | 2     | 1     | 1     | 1     | 0     | 0     | 0     | -1    | 0     | 0     | 25  |
|       |             | 0     | 1     | 2     | 0     | 2     | 2     | 0     | 0     | 0     | -1    | 0     | 30  |
|       |             | 1     | 0     | 0     | 1     | 0     | 1     | 0     | 0     | 0     | 0     | 1     | 14  |
|       | $z_j$       |       |       |       |       |       |       |       |       |       |       |       | ?   |
|       | $c_j - z_j$ |       |       |       |       |       |       |       |       |       |       |       |     |


## Solución Óptima (Método Penalización)

| $\min Z$ | $c_j  \to$  | 10      | 14      | 12      | 18      | 20      | 16      | 0       | 0      | 0       | 0       | 0      | 1000     | 1000     | 1000     |              |
|----------|-------------|---------|---------|---------|---------|---------|---------|---------|--------|---------|---------|--------|----------|----------|----------|--------------|
| $C_b$    | basis       | $x_1$   | $x_2$   | $x_3$   | $x_4$   | $x_5$   | $x_6$   | $s_1$   | $s_2$  | $s_3$   | $s_4$   | $s_5$  | $A_1$    | $A_3$    | $A_4$    | $b$          |
| 20       | $x_5$       | 0.1667  | 0.0000  | 0.0000  | 1.1667  | 1.0000  | 0.8333  | -0.5000 | 0.0000 | 0.3333  | -0.1667 | 0.0000 | 0.5000   | -0.3333  | 0.1667   | 9.6667       |
| 0        | $s_2$       | 0.0000  | 0.0000  | 0.0000  | 0.0000  | 0.0000  | 0.0000  | 1.0000  | 1.0000 | 0.0000  | 0.0000  | 0.0000 | -1.0000  | 0.0000   | 0.0000   | 6.0000       |
| 14       | $x_2$       | 0.6667  | 1.0000  | 0.0000  | 0.6667  | 0.0000  | -0.6667 | 0.0000  | 0.0000 | -0.6667 | 0.3333  | 0.0000 | 0.0000   | 0.6667   | -0.3333  | 6.6667       |
| 12       | $x_3$       | -0.5000 | 0.0000  | 1.0000  | -1.5000 | 0.0000  | 0.5000  | 0.5000  | 0.0000 | 0.0000  | -0.5000 | 0.0000 | -0.5000  | 0.0000   | 0.5000   | 2.0000       |
| 0        | $s_5$       | 1.0000  | 0.0000  | 0.0000  | 1.0000  | 0.0000  | 1.0000  | 0.0000  | 0.0000 | 0.0000  | 0.0000  | 1.0000 | 0.0000   | 0.0000   | 0.0000   | 14.0000      |
|          | $zj$        | 6.6667  | 14.0000 | 12.0000 | 14.6667 | 20.0000 | 13.3333 | -4.0000 | 0.0000 | -2.6667 | -4.6667 | 0.0000 | 4.0000   | 2.6667   | 4.6667   | **310.6667** |
|          | $c_j - z_j$ | 3.3333  | 0.0000  | 0.0000  | 3.3333  | 0.0000  | 2.6667  | 4.0000  | 0.0000 | 2.6667  | 4.6667  | 0.0000 | 996.0000 | 997.3333 | 995.3333 | Optimal      |


## Solución Factible (Fase 1)

| **$\min W$** | $c_j  \to$  | 0       | 0      | 0      | 0       | 0      | 0       | 0       | 0      | 0       | 0       | 0      | **1**   | **1**   | **1**   |         |
|--------------|-------------|---------|--------|--------|---------|--------|---------|---------|--------|---------|---------|--------|---------|---------|---------|---------|
| $C_b$        | basis       | $x_1$   | $x_2$  | $x_3$  | $x_4$   | $x_5$  | $x_6$   | $s_1$   | $s_2$  | $s_3$   | $s_4$   | $s_5$  | $A_1$   | $A_3$   | $A_4$   | $b$     |
| 0            | $x_5$       | 0.1667  | 0.0000 | 0.0000 | 1.1667  | 1.0000 | 0.8333  | -0.5000 | 0.0000 | 0.3333  | -0.1667 | 0.0000 | 0.5000  | -0.3333 | 0.1667  | 9.6667  |
| 0            | $s_2$       | 0.0000  | 0.0000 | 0.0000 | 0.0000  | 0.0000 | 0.0000  | 1.0000  | 1.0000 | 0.0000  | 0.0000  | 0.0000 | -1.0000 | 0.0000  | 0.0000  | 6.0000  |
| 0            | $x_2$       | 0.6667  | 1.0000 | 0.0000 | 0.6667  | 0.0000 | -0.6667 | 0.0000  | 0.0000 | -0.6667 | 0.3333  | 0.0000 | 0.0000  | 0.6667  | -0.3333 | 6.6667  |
| 0            | $x_3$       | -0.5000 | 0.0000 | 1.0000 | -1.5000 | 0.0000 | 0.5000  | 0.5000  | 0.0000 | 0.0000  | -0.5000 | 0.0000 | -0.5000 | 0.0000  | 0.5000  | 2.0000  |
| 0            | $s_5$       | 1.0000  | 0.0000 | 0.0000 | 1.0000  | 0.0000 | 1.0000  | 0.0000  | 0.0000 | 0.0000  | 0.0000  | 1.0000 | 0.0000  | 0.0000  | 0.0000  | 14.0000 |
|              | $zj$        | 0.0000  | 0.0000 | 0.0000 | 0.0000  | 0.0000 | 0.0000  | 0.0000  | 0.0000 | 0.0000  | 0.0000  | 0.0000 | 0.0000  | 0.0000  | 0.0000  | **0**   |
|              | $c_j - z_j$ | 0.0000  | 0.0000 | 0.0000 | 0.0000  | 0.0000 | 0.0000  | 0.0000  | 0.0000 | 0.0000  | 0.0000  | 0.0000 | 1.0000  | 1.0000  | 1.0000  | Optimal |



## Solución óptima (Fase 2)

| **$\min Z$** | $c_j  \to$  | 10     | 14     | 12     | 18     | 20     | 16     | 0      | 0     | 0      | 0      | 0     | **1000** | **1000** | **1000** |             |
|--------------|-------------|--------|--------|--------|--------|--------|--------|--------|-------|--------|--------|-------|----------|----------|----------|-------------|
| $C_b$        | basis       | $x_1$  | $x_2$  | $x_3$  | $x_4$  | $x_5$  | $x_6$  | $s_1$  | $s_2$ | $s_3$  | $s_4$  | $s_5$ | $A_1$    | $A_3$    | $A_4$    | $b$         |
| 20           | $x_5$       | 0.167  | 0.000  | 0.000  | 1.167  | 1.000  | 0.833  | -0.500 | 0.000 | 0.333  | -0.167 | 0.000 | 0.500    | -0.333   | 0.167    | 9.667       |
| 0            | $s_2$       | 0.000  | 0.000  | 0.000  | 0.000  | 0.000  | 0.000  | 1.000  | 1.000 | 0.000  | 0.000  | 0.000 | -1.000   | 0.000    | 0.000    | 6.000       |
| 14           | $x_2$       | 0.667  | 1.000  | 0.000  | 0.667  | 0.000  | -0.667 | 0.000  | 0.000 | -0.667 | 0.333  | 0.000 | 0.000    | 0.667    | -0.333   | 6.667       |
| 12           | $x_3$       | -0.500 | 0.000  | 1.000  | -1.500 | 0.000  | 0.500  | 0.500  | 0.000 | 0.000  | -0.500 | 0.000 | -0.500   | 0.000    | 0.500    | 2.000       |
| 0            | $s_5$       | 1.000  | 0.000  | 0.000  | 1.000  | 0.000  | 1.000  | 0.000  | 0.000 | 0.000  | 0.000  | 1.000 | 0.000    | 0.000    | 0.000    | 14.000      |
|              | $zj$        | 6.667  | 14.000 | 12.000 | 14.667 | 20.000 | 13.333 | -4.000 | 0.000 | -2.667 | -4.667 | 0.000 | 4.000    | 2.667    | 4.667    | **310.667** |
|              | $c_j - z_j$ | 3.333  | 0.000  | 0.000  | 3.333  | 0.000  | 2.667  | 4.000  | 0.000 | 2.667  | 4.667  | 0.000 | 996.000  | 997.333  | 995.333  | Optimal     |


---

<!-- _paginate: hold -->
<p class="outstanding-title">Algoritmo Simplex</p>
<p class="outstanding-subtitle">Ejemplos</p>

