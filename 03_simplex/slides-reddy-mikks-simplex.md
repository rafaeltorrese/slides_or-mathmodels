---
marp: true
title: "slides-reddy-mikks-simplex"
header: 'Algoritmo Simplex'
footer: 'Método Simplex'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Algoritmo Simplex</p>

# Ejemplo Reddy Mikks


Reddy Mikks produce pinturas para interiores y exteriores con dos materias primas, $M_1$ y $M_2$. La tabla siguiente proporciona los datos básicos del problema, la utilidad está dada en \$1,000 por tonelada.


| Materia Prima | Pintura para interiores | Pintura para exteriores | Disponibilidad diaria máxima (toneladas) |
|---------------|-------------------------|-------------------------|------------------------------------------|
| $M1$          | 6                       | 4                       | 24                                       |
| $M2$          | 1                       | 2                       | 6                                        |
| Utilidad      | 5                       | 4                       |                                          |

---


- Una encuesta de mercado indica que la demanda diaria de pintura para interiores no puede exceder la de pintura para exteriores en más de una tonelada. 
- Asimismo, que la demanda diaria máxima de pintura para interiores es de dos toneladas. Reddy Mikks se propone determinar la (mejor) combinación óptima de pinturas para interiores y exteriores que maximice la utilidad diaria total.

#### Modelo

$$\max Z = 5x_1 + 4x_2$$

<center>subject to</center>
  
$$
\begin{align*}
6x_1 + 4x_2  &\leq 24\\
x_1 + 2x_2  &\leq 6\\
-x_1 + x_2  &\leq 1\\
x_2  &\leq 2\\[2mm]
x_1, x_2  &\geq 0
\end{align*}
$$

## Forma Estándar

$$\max Z = 5x_1 + 4x_2 + 0S_1 + 0S_2 + 0S_3 + 0S_4$$

<br>
  
$$
\begin{align*}
6x_1 + 4x_2 & + S_1 &   &       &   &      &   &     & = &\, 24\\
x_1 + 2x_2  &       & + & S_2   &   &      &   &     & = &\, 6\\
-x_1 + x_2  &       &   &       & + &  S_3 &   &     & = &\, 1\\
x_2         &       &   &       &   &      & + & S_4 & = &\, 2
\end{align*}
$$

<br>

$$x_1, x_2, S_1, S_2, S_3, S_4  \geq 0$$


Tenemos 

$$_6C_4 = \frac{30}{2} = 15$$ 

soluciones básicas


## Método Analítico

Las soluciones están disponibles en el siguiente archivo: <a href="https://docs.google.com/spreadsheets/d/1qJzrwWjYqAQBkCWNtAmCBN9Q5Ymp36oqd6Yj7_i5cDc/edit?usp=sharing" target="_blank" alt="analytical method"> reddy-mikks-analytical</a>

#### Soluciones Factibles

| ID | 1  | 2  | 3  | 4  |
|----|----|----|----|----|
| 1  | x1 | x2 | s1 | s2 |
| 2  | x1 | x2 | s1 | s3 |
| 3  | x1 | x2 | s3 | s4 |
| 4  | x1 | s2 | s3 | s4 |
| 5  | x2 | s1 | s2 | s4 |
| 6  | s1 | s2 | s3 | s4 |


---


#### Soluciones Infactibles

| ID | 1  | 2  | 3  | 4  |
|----|----|----|----|----|
| 7  | x1 | x2 | s1 | s4 |
| 8  | x1 | x2 | s2 | s3 |
| 9  | x1 | x2 | s2 | s4 |
| 10 | x1 | s1 | s2 | s4 |
| 11 | x1 | s1 | s3 | s4 |
| 12 | x2 | s1 | s2 | s3 |
| 13 | x2 | s1 | s3 | s4 |
| 14 | x2 | s2 | s3 | s4 |

----

#### Sin Solución 

El siguiente sistema no se puede resolver porque son <a href="https://math.libretexts.org/Bookshelves/Linear_Algebra/Fundamentals_of_Matrix_Algebra_(Hartman)/01%3A_Systems_of_Linear_Equations/1.04%3A_Existence_and_Uniqueness_of_Solutions" target="_blank" alt="Unique solutions">rectas paralelas</a>



| ID | 1  | 2  | 3  | 4  |
|----|----|----|----|----|
| 15 | **x1** | **s1** | **s2** | **s3** |

<br>

El sistema es el siguiente, observar la última fila del sistema

| x1 | s1 | s2 | s3 | b  |
|----:|----|----|----|----:|
| 6  | 0  | 0  | 0  | 24 |
| 1  | 0  | 0  | 0  | 6  |
| -1 | 0  | 0  | 0  | 1  |
| **0**  | **0**  | **0**  | **0**  | **2**  |


## Método Gráfico

- Usar <a href="https://www.geogebra.org/calculator/w8kc6wjp" target="_blank" alt="graphical method">geogebra</a>
- Graficar todas las desigualdades como ecuaciones.

```
eq1: 6x + 4y  = 24
eq2: x + 2y  = 6
eq3: -x + y  = 1
eq4: y  = 2
```

```
z1: 5x + 4y = 10
z2: 5x + 4y = 17
```

# Método Simplex (Revisado)

#### Tabla inicial simplex

| max | cj      | 5  | 4  | 0  | 0  | 0  | 0  |          |
|-----|---------|----|----|----|----|----|----|----------|
| cb  | basis   | x1 | x2 | s1 | s2 | s3 | s4 | solution |
| 0   | **s1**      | 6  | 4  | 0  | 0  | 0  | 0  | **24**       |
| 0   | **s2**      | 1  | 2  | 0  | 0  | 0  | 0  | **6**        |
| 0   | **s3**      | -1 | 1  | 0  | 0  | 0  | 0  | **1**        |
| 0   | **s4**      | 0  | 1  | 0  | 0  | 0  | 0  | **2**        |
|     | zj      | 0  | 0  | 0  | 0  | 0  | 0  | **0**        |
|     | cj - zj | 5  | 4  | 0  | 0  | 0  | 0  |          |

El algoritmo está disponible en la siguiente hoja de cálculo: <a href="https://docs.google.com/spreadsheets/d/17LrgphmAe6lc9VRwEU9RsYAy1yUO86HrLEWlmnSuuIA/edit?usp=sharing" target="_blank" alt="simplex">reddy-mikks-simplex</a>

<a href="" target="_blank" alt=""></a>

## Iteración 01

| max | cj      | 5     | 4     | 0      | 0     | 0     | 0     |          |
|-----|---------|-------|-------|--------|-------|-------|-------|----------|
| cb  | basis   | x1    | x2    | s1     | s2    | s3    | s4    | solution |
| 5   | **x1**      | 1.000 | 0.667 | 0.167  | 0.000 | 0.000 | 0.000 | **4.000**    |
| 0   | **s2**      | 0.000 | 1.333 | -0.167 | 1.000 | 0.000 | 0.000 | **2.000**    |
| 0   | **s3**      | 0.000 | 1.667 | 0.167  | 0.000 | 1.000 | 0.000 | **5.000**    |
| 0   | **s4**      | 0.000 | 1.000 | 0.000  | 0.000 | 0.000 | 1.000 | **2.000**    |
|     | zj      | 5.000 | 3.333 | 0.833  | 0.000 | 0.000 | 0.000 | **20**       |
|     | cj - zj | 0.000 | 0.667 | -0.833 | 0.000 | 0.000 | 0.000 | --       |


## Iteración 02


| max | cj      | 5     | 4     | 0      | 0      | 0     | 0     |          |
|-----|---------|-------|-------|--------|--------|-------|-------|----------|
| cb  | basis   | x1    | x2    | s1     | s2     | s3    | s4    | solution |
| 5   | **x1**      | 1.000 | 0.000 | 0.250  | -0.500 | 0.000 | 0.000 | **3.000**    |
| 4   | **x2**      | 0.000 | 1.000 | -0.125 | 0.750  | 0.000 | 0.000 | **1.500**    |
| 0   | **s3**      | 0.000 | 0.000 | 0.375  | -1.250 | 1.000 | 0.000 | **2.500**    |
| 0   | **s4**      | 0.000 | 0.000 | 0.125  | -0.750 | 0.000 | 1.000 | **0.500**    |
|     | zj      | 5.000 | 4.000 | 0.750  | 0.500  | 0.000 | 0.000 | **21**       |
|     | cj - zj | 0.000 | 0.000 | -0.750 | -0.500 | 0.000 | 0.000 | **Optimal**  |


---

<p class="outstanding-title">Algoritmo Simplex</p>
