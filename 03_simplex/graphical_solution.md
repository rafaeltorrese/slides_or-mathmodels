<style>
.inside {
    background-color: "red";
    border-collapse: collapse;
}
</style>

# Plotting a Linear Programming Problem with Python
- Go to Chapter 02 Section 2.1 "MODELO DE PL CON DOS VARIABLES" and read "Ejemplo 2.1-1 (La compañía Reddy Mikks)" Page 13 in the book [Investigación de operaciones (9a. ed.) de Hamdy A. Taha](https://anahuac.primo.exlibrisgroup.com/permalink/52ANAHUAC_INST/ttdqh7/cdi_proquest_ebookcentral_EBC5243899).
- Open a new Jupyter Notebook
- Change title of the new `.ipynb`  file. Use the following name *"Graphical Method Solution. An Example"*

## The Problem
**From the [Taha ebook][Taha] go to Ejemplo 2.1-1 (La compañía Reddy Mikks)**

[Taha]: https://anahuac.primo.exlibrisgroup.com/permalink/52ANAHUAC_INST/ttdqh7/cdi_proquest_ebookcentral_EBC5243899
"Taha, Hamdy A. Investigación de operaciones (9a. ed.). Distrito Federal: Pearson Educación, 2012. Print.
"


Reddy Mikks produce pinturas para interiores y exteriores con dos materias primas, $M_1$ y $M_2$.
La tabla siguiente proporciona los datos básicos del problema.

<table class="inside">
<thead align="center">
    <tr>
        <td></td>
        <td colspan="2">Toneladas de materia prima por tonelada de</td>
        <td rowspan="2">Disponibilidad diaria máxima (toneladas)</td>
    </tr>
    <tr>
        <td></td>
        <td>Pintura para exteriores</td>
        <td>Pintura para interiores</td>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Materia prima $M_1$</td>
        <td>6</td>
        <td>4</td>
        <td>24</td>
    </tr>
    <tr>
        <td>Materia prima $M_2$</td>
        <td>1</td>
        <td>2</td>
        <td>6</td>
    </tr>
</tbody>
<tfoot>
    <tr>
        <td>Utilidad por tonelada (\$1000)</td>
        <td>5</td>
        <td>4</td>
        <td></td>
    </tr>
</tfoot>
</table>

Una encuesta de mercado indica que la demanda diaria de pintura para interiores no puede exceder la de pintura para exteriores en más de una tonelada. Asimismo, que la demanda diaria máxima de pintura para interiores es de dos toneladas.

Reddy Mikks se propone determinar la (mejor combinación óptima de pinturas para interiores y exteriores que maximice la utilidad diaria total. 

Todos los modelos de IO, incluido el de PL, constan de tres componentes básicos.

1. Las **variables** de decisión que pretendemos determinar.
2. El **objetivo** (la meta) que necesitamos optimizar (maximizar o minimizar).
3. Las **restricciones** que la solución debe satisfacer.

## The Model
### Decision Varibles
- $x_1$
    :  Toneladas producidas diariamente de pintura para exteriores

- $x_2$
    : Toneladas producidas diariamente de pintura para interiores

### Objective Function
$$\max Z = 5x_1 + 4x_2$$

### Constraints

$$
\begin{align*}
6x_1 + 4x_2 &\leq 24 \\
x_1 + 2x_2 &\leq 6 \\
-x_1 + x_2 &\leq 1 \\
x_2 & \leq 2 \\
\end{align*}
$$


## Isolate all $x_2$ variables

Transform all expressions as functions of $x_2$

+ Objective function becomes
    : $x_2 = (Z - 5x_1) / 4$
  
- Constraints
    : 
    - Equation 1
        : $x_2 = (24 - 6x_1) / 4$
    - Equation 2
        : $x_2 = (6 - x_1) / 2$
    - Equation 3
        : $x_2 = (1 + x_1)$
    - Equation 2
        : $x_2 = 2$

## Code in Python
First we need to import the following modules

```python
import numpy as np
import matplotlib.pyplot as plt
```

Then, we define the domain of $x_1$

```python
x = np.linspace(0, 100, 10)
```

After, we define $Z$ function (the objective function) as a **lambda function**. [How are the lambda functions used?](https://www.w3schools.com/python/python_lambda.asp)

```python
zfunction = lambda z, x: (z - 5 * x) / 4
zlabel = r"$Z = 5x_1 + 4x_2$"
zdomain = np.linspace(5, 50, 5)
```

After we need to define all functions of $x_2$ as variables. In this example, all functions of $x_2$ were defined with the variable name: *equation*

```python
equation1 = (24 - 6 * x) / 4
equation2 = (6 - x) / 2
equation3 = 1 + x
equation4 = np.full_like(x, 2)  #  it's a constant
```

The `np.full_like(x, 2)` creates a `numpy.ndarray` object of the same shape from the variable `x` define as a `numpy.ndarray` with the `np.linspace( )` function. For further details see the [numpy.full_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html) documentation.

Now we create a list of equations as the following:

```python
equations = [
    equation1, 
    equation2, 
    equation3, 
    equation4,
    ]
```

We also need the mathematical expression for every equation; this is achieved with a list of strings. If you have questions about the r character before the string, you can see an explanation in [this blog](https://www.journaldev.com/23598/python-raw-string)

```python
labels = [
    r"$Eq1:\, 6x_1 + 4x_2 = 24$",
    r"$Eq2:\, x_1 + 2x_2 = 6$",
    r"$Eq3:\, -x_1 + x_2 = 1$",
    r"$Eq4:\, x_2= 2$",
]
```

## Plot the equations

See this [matplotlib tutorial](https://www.w3schools.com/python/matplotlib_pyplot.asp) for further details.

Now we are going to plot all the equations, first, we'll adjust the size of the plot

```python
plt.figure(figsize=(10, 10))
plt.xlim(-1, 7)
plt.ylim(-1, 7)
```

Set te $x$ and $y$ axes

```python
plt.axvline(0, color="0.4")  # y axis
plt.axhline(0, color="0.4")  # x axis
```

Plot all equations with its labels. 

```python
# Plot lines: x, f(x)
for equation, label in zip(equations, labels):
    plt.plot(x, equation, lw=2, label=label)
```

Plot values int the objective function
```python
# Plot z values
plt.plot(x, zfunction(0, x), color="magenta", ls="--", label=zlabel, alpha=0.3)
for z in zdomain:
    plt.plot(x, zfunction(z, x), ls="--", color="magenta", alpha=0.3)
```

Fill areas of the inequalities. We used the `fill_between` function from `matplotlib.pyplot`; further details of this function in [this link](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_demo.html)
```python
# Plot areas
plt.fill_between(x, 
                equation1, 
                where=(x < equation1), 
                color="orange", 
                alpha=0.2, 
                interpolate=True,
                label=r"$x_1 + 2x_2 \leq 6$")

plt.fill_between(x,
                 equation2, 
                 where=(x < equation2), 
                 color="green", 
                 alpha=0.2, 
                 interpolate=True,
                 label=r"$x_1 + 2x_2 \leq 6$",
                 )

plt.fill_between(x, 
                equation3,
                where=(x <= equation3), 
                color="red", 
                alpha=0.2, 
                interpolate=True,
                label=r"$-x_1 + x_2 \leq 1$")

plt.fill_between(x, 
                equation4,
                color="blue",
                alpha=0.2,
                label=r"$x_2 \leq 2$",
                )

```

Show the legends
```python
plt.legend(
    fontsize=15, 
    loc="upper right"
    )
```

Show the plot, don't forget his bottom line
```python
plt.show()
```