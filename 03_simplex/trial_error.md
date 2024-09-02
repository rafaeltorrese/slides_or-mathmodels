---
marp: true
title: "trial-error-technique"
header: 'Método de Prueba y Error'
footer: 'Método Simplex'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Introducción al Método Simplex</p>


# Método de Pruba y Error

Una compañía de petróleos produce en sus refinerías gasóleo ($G$), gasolina sin plomo ($P$) y gasolina súper ($S$) a partir de dos tipos de crudos,$C_1$ y $C_2$. Las refinerías están dotadas de dos tipos de tecnologías.

La tecnología nueva $T_n$ utiliza en cada sesión de destilación 7 unidades de $C_1$ y 12 de $C_2$, para producir 8 unidades de $G$, 6 de $P$ y 5 de $S$. Con la tecnología antigua $T_a$, se obtienen en cada destilación 10 unidades de $G$, 7 de $P$ y 4 de $S$, con un gasto de 10 unidades de $C_1$ y 8 de $C_2$.

---

Estudios de demanda permiten estimar que para el próximo mes se deben producir al menos 900 unidades de $G$, 300 de $P$ y entre 800 y 1700 de $S$. La disponibilidad de crudo $C_1$ es de 1400 unidades y de $C_2$ de 2000 unidades.

Los beneficios por unidad producida son

| Gasolina    | $G$ | $P$ | $S$ |
|:------------|:---:|:---:|:---:|
| Beneficio/u |  4  |  6  |  7  |


  La compañía desea conocer **cómo utilizar ambos procesos de destilación**, que se pueden realizar total o parcialmente, y los crudos para que el **beneficio sea el máximo**.

# Modelo

- $x_1$: número de destilaciones con $T_n$ 
- $x_2$: número de destilaciones con $T_a$


<br>

$$\max Z = 103x_1 + 110x_2$$

<center>sujeto a </center>

$$
\begin{align*}
    7x_1 + 10x_2 &\leq 1400\\
    12x_1 + 8x_2 &\leq 2000\\
    8x_1 + 10x_2 &\geq 900\\
    6x_1 + 7x_2 &\geq 300\\
    5x_1 + 4x_2 &\leq 1700\\
    5x_1 + 4x_2 &\geq 300\\[5mm]
    x_1, x_2 &\geq 0
\end{align*}
$$

## Formato Estándar de un Model PL

$$\max Z = 103x_1 + 110x_2 + 0S_1 + 0S_2 + \ldots + 0S_6$$

<br>
<center>sujeto a </center>

$$
\begin{align*}
    7x_1 + 10x_2 + S_1   & = 1400\\
    12x_1 + 8x_2 + S_2 & = 2000\\
    8x_1 + 10x_2 - S_3 & = 900\\
    6x_1 + 7x_2 - S_4 & = 300\\
    5x_1 + 4x_2 + S_5 & = 1700\\
    5x_1 + 4x_2 - S_6 & = 300\\[5mm]
    x_1, x_2, S_1, S_2, S_3, S_4, S_5, S_6  &\geq 0
\end{align*}
$$


---

### Calculando el número de soluciones básicas

- $n$: número de variables
- $m$: número de ecuaciones (restricciones)
- El númer de soluciones básicas es:

$$_mC_n = \frac{n!}{m! (n - m)!} = \frac{!}{m! (n - m)!}$$

Para el ejemplo que estamos resolviendo tenemos un total de 

$$_mC_n = \frac{8!}{6! 2!} = \frac{8 \cdot 7 \cdot 6!}{6! \cdot 2!} = \frac{8 \cdot 7}{2 \cdot 1} = 4 \cdot 7 = 28$$

28 soluciones básicas.


---

### Generar sistemas de ecuaciones lineales

Para este ejemplo se generarán 28 sistemas de ecuaciones lineales


|    | 1  | 2  | 3  | 4  | 5  | 6  |
|----|----|----|----|----|----|----|
| 1  | x1 | x2 | s1 | s2 | s3 | s4 |
| 2  | x1 | x2 | s1 | s2 | s3 | s5 |
| 3  | x1 | x2 | s1 | s2 | s3 | s6 |
| 4  | x1 | x2 | s1 | s2 | s4 | s5 |
| 5  | x1 | x2 | s1 | s2 | s4 | s6 |
| 6  | x1 | x2 | s1 | s2 | s5 | s6 |
| 7  | x1 | x2 | s1 | s3 | s4 | s5 |


----

|    | 1  | 2  | 3  | 4  | 5  | 6  |
|----|----|----|----|----|----|----|
| 8  | x1 | x2 | s1 | s3 | s4 | s6 |
| 9  | x1 | x2 | s1 | s3 | s5 | s6 |
| 10 | x1 | x2 | s1 | s4 | s5 | s6 |
| 11 | x1 | x2 | s2 | s3 | s4 | s5 |
| 12 | x1 | x2 | s2 | s3 | s4 | s6 |
| 13 | x1 | x2 | s2 | s3 | s5 | s6 |
| 14 | x1 | x2 | s2 | s4 | s5 | s6 |


---


|    | 1  | 2  | 3  | 4  | 5  | 6  |
|----|----|----|----|----|----|----|
| 15 | x1 | x2 | s3 | s4 | s5 | s6 |
| 16 | x1 | s1 | s2 | s3 | s4 | s5 |
| 17 | x1 | s1 | s2 | s3 | s4 | s6 |
| 18 | x1 | s1 | s2 | s3 | s5 | s6 |
| 19 | x1 | s1 | s2 | s4 | s5 | s6 |
| 20 | x1 | s1 | s3 | s4 | s5 | s6 |
| 21 | x1 | s2 | s3 | s4 | s5 | s6 |

---


|    | 1  | 2  | 3  | 4  | 5  | 6  |
|----|----|----|----|----|----|----|
| 22 | x2 | s1 | s2 | s3 | s4 | s5 |
| 23 | x2 | s1 | s2 | s3 | s4 | s6 |
| 24 | x2 | s1 | s2 | s3 | s5 | s6 |
| 25 | x2 | s1 | s2 | s4 | s5 | s6 |
| 26 | x2 | s1 | s3 | s4 | s5 | s6 |
| 27 | x2 | s2 | s3 | s4 | s5 | s6 |
| 28 | s1 | s2 | s3 | s4 | s5 | s6 |


---


<!-- _paginate: skip -->

<p class="outstanding-title">Introducción al Método Simplex</p>