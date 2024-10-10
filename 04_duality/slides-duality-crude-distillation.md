---
marp: true
title: "slides-duality-crude-distillation"
header: "Dualidad"
footer: "Programación Lineal"
author: Rafael Torres Escobar
paginate: true
---



<!-- _paginate: false -->

<p class="outstanding-title">Dualidad en Programación lineal</p>

# Definición

- El problema dual se define sistemáticamente a partir del modelo de PL primal (u original). 
- Los dos problemas están estrechamente relacionados en el sentido de que la so- lución óptima de uno proporciona automáticamente la solución óptima al otro. 
- En la mayoría de los tratamientos de PL, el dual se define para varias formas del pri- mal según el sentido de la optimización (maximización o minimización), los tipos de restricciones ($\leq$, $\geq$ o $=$), y el signo de las variables (no negativas o irrestrictas). 


---

Las ideas clave para construir el dual a partir del primal se resumen como sigue:

1. Asigne una variable dual por cada restricción primal.
2. Construya una restricción dual por cada variable primal.
3. Los coeficientes de restricción (columna) y el coeficiente objetivo de la variable primal $j$-ésima definen respectivamente los lados izquierdo y derecho de la restricción dual $j$-ésima. 

---

4. Los coeficientes objetivo duales son iguales a los lados derechos de las ecuaciones de restricción primales. 
5. Una forma fácil de recordar el tipo de restricción en el dual (es decir, $\leq$ o $\geq$) es que si el objetivo dual es de minimización (es decir, apunta hacia abajo), entonces todas las restricciones serán del tipo $\geq$ (es decir, apuntan hacia arriba). Lo opuesto aplica cuando el objetivo dual es de maximización.

# Ejemplo

Una compañía de petróleos produce en sus refinerías gasóleo ($G$), gasolina sin plomo ($P$) y gasolina súper ($S$) a partir de dos tipos de crudos,$C_1$ y $C_2$. Las refinerías están dotadas de dos tipos de tecnologías.

La tecnología nueva $T_n$ utiliza en cada sesión de destilación 7 unidades de $C_1$ y 12 de $C_2$, para producir 8 unidades de $G$, 6 de $P$ y 5 de $S$. Con la tecnología antigua $T_a$, se obtienen en cada destilación 10 unidades de $G$, 7 de $P$ y 4 de $S$, con un gasto de 10 unidades de $C_1$ y 8 de $C_2$.

---

Estudios de demanda permiten estimar que para el próximo mes se deben producir al menos 900 unidades de $G$, 300 de $P$ y entre 800 y 1700 de $S$. La disponibilidad de crudo $C_1$ es de 1400 unidades y de $C_2$ de 2000 unidades.

Los beneficios por unidad producida son

| Gasolina    | $G$ | $P$ | $S$ |
|:------------|:---:|:---:|:---:|
| Beneficio/u |  4  |  6  |  7  |


  La compañía desea conocer **cómo utilizar ambos procesos de destilación**, que se pueden realizar total o parcialmente, y los crudos para que el **beneficio sea el máximo**.

# Modelo primal

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

# Modelo dual

## Formato Estándar del Primal

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


# Uso de Geogebra

- La representación gráfica solo es adecuada para problemas con 2 variables.
- La gráfica la puedes consultar en este enlace: [Gráfica del Problema de Destilación De Crudos](https://www.geogebra.org/calculator/njyyua9d).



# Uso de hojas de cálculo

### Google Sheets

+ [Index](https://support.google.com/docs/answer/3098242?hl=en)
+ [Indice](https://support.google.com/docs/answer/3098242?hl=es-419)
+ [Match](https://support.google.com/docs/answer/3093378?hl=en)
+ [Coincidir](https://support.google.com/docs/answer/3093378?hl=es-419&sjid=453663785966893365-NC)
+ [Offset](https://support.google.com/docs/answer/3093379?hl=en)
+ [Desref](https://support.google.com/docs/answer/3093379?hl=es-419)
  
  
---

### Excel
+ [Index](https://support.microsoft.com/en-us/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd)
+ [Índice](https://support.microsoft.com/es-es/office/indice-funci%C3%B3n-indice-a5dcf0dd-996d-40a4-a822-b56b061328bd)
+ [Match](https://support.microsoft.com/en-us/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a)
+ [Coincidir](https://support.microsoft.com/es-es/office/funci%C3%B3n-coincidir-e8dffd45-c762-47d6-bf89-533f4a37673a)
+ [Offset](https://support.microsoft.com/en-us/office/offset-function-c8de19ae-dd79-4b9b-a14e-b4d906d11b66)
+ [Desref](https://support.microsoft.com/es-es/office/desref-funci%C3%B3n-desref-c8de19ae-dd79-4b9b-a14e-b4d906d11b66)



---

<!-- _paginate: false -->

<p class="outstanding-title">Dualidad en Programación lineal</p>
