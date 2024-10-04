---
marp: true
title: "slides-simplex-two-phase"
header: "Método de Dos Fases"
footer: "Método Simplex"
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Método Simplex</p>

<p class="outstanding-subtitle">Método de Dos Fases</p>



# Problema

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
    7x_1 + 10x_2 & + S_1    &=& 1400\\
    12x_1 + 8x_2 &+ S_2  &=& 2000\\
    8x_1 + 10x_2 &- S_3 & =& 900\\
    6x_1 + 7x_2 &- S_4 & =& 300\\
    5x_1 + 4x_2 &+ S_5 & =& 1700\\
    5x_1 + 4x_2 &- S_6 & =& 300
\end{align*}
$$

$$x_1, x_2, S_1, S_2, S_3, S_4, S_5, S_6  \geq 0$$


La gráfica está este enlace: <a href="https://www.geogebra.org/calculator/njyyua9d" target="_blank" alt="plot">Gráfica del Problema de Destilación De Crudos</a>



## Calculando el número de soluciones básicas

- $n$: número de variables
- $m$: número de ecuaciones (restricciones)
- El número de soluciones básicas es:

$$_mC_n = \frac{n!}{m! (n - m)!} = \frac{8!}{6! (8 - 6)!}$$

Para el ejemplo que estamos resolviendo tenemos un total de 

$$_mC_n = \frac{8!}{6! 2!} = \frac{8 \cdot 7 \cdot 6!}{6! \cdot 2!} = \frac{8 \cdot 7}{2 \cdot 1} = 4 \cdot 7 = 28$$

28 soluciones básicas.




# Método de Dos Fases

- Es necesario agregar variables artificiales a las restricciones para obtener una solución factible básica inicial a un problema de programación lineal. 
- Si se quiere resolver el problema, las **variables artificiales deben reducirse a cero**. 
- El método de dos fases es otro método para manejar estas variables artificiales. Aquí el problema de programación lineal se resuelve en dos fases.
- El problema tiene algunas restricciones con desigualdades $\geq$ o ecuaciones ($=$)
- Se agreagan variables artificiales $A_i$ cuando se restan variables de superávit $(- S_i)$ o bien cuando la restriccion es una ecuación.


## Fase I

+ En esta fase encontramos una solución factible básica inicial para el problema original. 
+ Para ello, todas las variables artificiales deben ser **llevadas a cero**. 
+ Para ello, se crea una función objetivo artificial $(w)$, que es **la suma de todas las variables artificiales**. 
+ Esta **nueva función objetivo se minimiza**, sujeta a las restricciones del problema (original) dado, utilizando el método simplex. 

---

Al final de la fase I, surgen tres casos:

1. Si el valor mínimo de **$w > 0$**, y **al menos una variable artificial** aparece en la base en un nivel positivo, entonces el problema dado **no tiene solución factible** y el procedimiento termina.

2. Si el valor mínimo de **$w = 0$**, **y no aparece ninguna variable artificial en la base**, entonces **se obtiene una solución factible básica** para el problema dado. 
    + La(s) columna(s) artificial(es) se eliminan para los cálculos de la fase II.

---

3. Si el valor mínimo de $w = 0$ y una o más variables artificiales aparecen en la base en el nivel cero, entonces se obtiene una solución factible para el problema original. 
    + Sin embargo, debemos tener cuidado con esta variable artificial y asegurarnos de que nunca se vuelva positiva durante los cálculos de la fase II.
    - Se asigna un coeficiente de costo cero a esta variable artificial y se conserva en la tabla inicial de la fase II.
    - Si esta variable permanece en la base en el nivel cero en todos los cálculos de la fase II, no hay problema.

---

3.    
   - Sin embargo, el problema surge si se vuelve positiva en alguna iteración. En tal caso, se adopta un enfoque ligeramente diferente para seleccionar la variable saliente. No se adopta el criterio de relación de reemplazo no negativa más baja para encontrar la variable saliente.
   - Se **selecciona la variable artificial** (o una de las variables artificiales si hay más de una) como variable saliente. 
   - Luego, se puede aplicar el método simplex como de costumbre para obtener la solución factible básica óptima para el problema de programación lineal dado.

## Fase II

- **Cuando la fase I da como resultado (2) o (3), pasamos a la fase II** para encontrar la solución óptima para el problema de programación lineal dado.
- La solución factible básica encontrada al final de la fase I se utiliza ahora como solución inicial para el problema original.
- La **tabla final de la fase I** se convierte en **la tabla inicial de la fase II** en la que la función objetivo artificial (auxiliar) se reemplaza por la función objetivo original.
- A continuación, se aplica el método simplex para llegar a la solución óptima. Las variables artificiales que no aparecen en la base se pueden eliminar.

---

### Observaciones.

1.  En la fase I, **las iteraciones se detienen** tan pronto como el valor de **la nueva función objetivo (artificial) se convierte en cero** porque este **es su valor mínimo**. **No hay necesidad** de continuar hasta que se alcance la **optimalidad** si este valor **se convierte en cero antes de eso**. 
2. Nótese que la nueva **función objetivo siempre es de tipo minimización** independientemente de si el problema original es de tipo maximización o minimización.


## Tabla Simplex Inicial Fase I

Consultar el siguiente enlace: <a href="https://docs.google.com/spreadsheets/d/1bweGkQ2UR7GTtNDsAnMKCwXScdR0Zw5YpyoqgoVZC3s/edit?usp=sharing" target="_blank" alt="big M method">Simplex para Ejemplo de Destilación de Crudos</a>

$$\min W = A_3 + A_4 + A_6$$

| **Min W** | cj      | 0   | 0   | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  |      |
|-----------|---------|-----|-----|----|----|----|----|----|----|----|----|----|------|
| Cb        | basis   | x1  | x2  | s1 | s2 | s3 | s4 | s5 | s6 | A3 | A4 | A6 | b    |
| 0         | s1      | 7   | 10  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1400 |
| 0         | s2      | 12  | 8   | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 2000 |
| 1         | A3      | 8   | 10  | 0  | 0  | -1 | 0  | 0  | 0  | 1  | 0  | 0  | 900  |
| 1         | A4      | 6   | 7   | 0  | 0  | 0  | -1 | 0  | 0  | 0  | 1  | 0  | 300  |
| 0         | s5      | 5   | 4   | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1700 |
| 1         | A6      | 5   | 4   | 0  | 0  | 0  | 0  | 0  | -1 | 0  | 0  | 1  | 300  |
|           | zj      | 19  | 21  | 0  | 0  | -1 | -1 | 0  | -1 | 1  | 1  | 1  | 1500 |
|           | cj - zj | -19 | -21 | 0  | 0  | 1  | 1  | 0  | 1  | 0  | 0  | 0  | --   |


## Tabla Simplex Inicial Fase I

Consultar el siguiente enlace: <a href="https://docs.google.com/spreadsheets/d/1bweGkQ2UR7GTtNDsAnMKCwXScdR0Zw5YpyoqgoVZC3s/edit?usp=sharing" target="_blank" alt="big M method">Simplex para Ejemplo de Destilación de Crudos</a>

---

<!-- _paginate: skip -->

<p class="outstanding-title">Método Simplex</p>
<p class="outstanding-subtitle">Método de Penalización</p>

