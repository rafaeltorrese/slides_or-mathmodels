---
marp: true
title: "slides-diet-two-variables"
header: 'Mëtodo Analítico'
footer: 'Método Simplex'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Método Analítico</p>

# Problema de la dieta

Ozark Farms consume diariamente un mínimo de 800 lb de un alimento especial, el cual es una mezcla de maíz y soya con las siguientes composiciones en libras por libra de forraje:


Forraje | Proteína | Fibra | Costo (\$ / lb)
----|----|----|----
 Maíz | 0.09 | 0.02| 0.30
 Soya |0.60|0.06|0.90


---

Las necesidades dietéticas del alimento especial son un mínimo de 30% de proteína y un máximo de 5% de fibra. El objetivo es determinar la mezcla diaria de alimento a un costo mínimo. Las variables de decisión del modelo son

- $x_1$: libras de maíz en la mezcla diaria
- $x_2$: libras de soya en la mezcla diaria

---

El objetivo es minimizar el costo diario total (en dólares) de la mezcla de alimento, es decir,

$$\min z = 0.30x_1 + 0.90x_2$$

Las restricciones representan la cantidad diaria de la mezcla y las necesidades dietéticas. Ozark Farms requiere un mínimo de 800 lb de alimento al día, es decir,

$$x_1 + x_2 \geq 800$$

---

La cantidad de proteína contenida en $x_1$ libras de maíz y en $x_2$ libras de soya es $(0.09x_1 + 0.60x_2)$ lb. Esta cantidad debe ser al menos igual al 30% de la mezcla de alimentos total $(x_1 + x_2)$ lb, es decir,

$$0.90 x_1 + 0.60 x_2 \geq 0.60(x_1 + x_2)$$


Asimismo, la necesidad de fibra de 5% máximo se representa como sigue

$$0.02x_1 + 0.06x_2 \leq 0.05(x_1 + x_2)$$


## Modelo Matemático

Las restricciones se simplifican cambiando los términos en $x_1$ y $x_2$ al lado izquierdo de cada desigualdad, con sólo una constante del lado derecho. El modelo completo es

<br>

$$\min z = 0.30x_1 + 0.90x_2$$

<center>
sujeto a
</center>

$$\begin{align*}
x_1 + x_2 & \geq 800\\
0.21 x_1 - 0.30 x_2 & \leq 0\\
0.03x_1 - 0.01x_2 & \geq 0\\[5mm]
x_1, x_2 & \geq 0
\end{align*}$$

# Solución por Método Analítico

#### Formato Estándar del Problema de PL

$$\min z = 0.30x_1 + 0.90x_2$$

<center>
sujeto a
</center>

$$\begin{align*}
x_1 + x_2 - S_1 & = 800\\
0.21 x_1 - 0.30 x_2 + S_2 & = 0\\
0.03x_1 - 0.01x_2 - S_3 & = 0\\[5mm]
x_1, x_2 & \geq 0
\end{align*}$$

---

Del formato estándar, tenemos un total de

- $n = 5$ variables
- $m = 3$ ecuaciones

por lo tanto, vamos a calcular un total de

$$_nC_m = \frac{n!}{m!(n - m)!} = \frac{n \cdot (n - 1) \cdot m!}{m! (n - m)!} = \frac{n \cdot (n - 1)}{(n - m)!}$$

$$_5C_3 = \frac{5!}{3!2!}  = \frac{5\cdot 4 \cdot 3!}{3!2!} = \frac{20}{2} = 10$$

soluciones básicas


# Archivos de Soporte

- Los cálculos los pueden consultar en el siguiente archivo de Excel: [`data_table_analytical-method.xlsx`](https://docs.google.com/spreadsheets/d/1OJp8CGvU_LyKQFAKlDzOiF18LCxbzOJW/edit?usp=sharing&ouid=108465964376312334067&rtpof=true&sd=true).

- Los videos con la explicación están disponibles en los siguientes enlaces:
    + [Tabla de Datos 01](https://app.screencastify.com/v3/watch/1qsScB0LiLNerXv98bGf)
    + [Tabla de Datos 02](https://app.screencastify.com/v3/watch/BbCSee2XUttC2fQHsK8Y)
    + [Tabla de Datos 03](https://app.screencastify.com/v3/watch/5W4HbekXcKY5GlzrqFPF)



# Uso de Python

```python
from itertools import combinations
import numpy as np
import pandas as pd
```

```python
A = np.array(
    [
        [1.00,  1.00, -1.00, 0.00,  0.00],
        [0.21, -0.30,  0.00, 1.00,  0.00],
        [0.03, -0.01,  0.00, 0.00, -1.00],
        ], dtype=float
        )

m, n = A.shape
b = np.array([800, 0, 0], dtype=float).reshape((m, -1))
c = np.array([0.30, 0.90, 0, 0, 0], dtype=float).reshape((-1, n))
```

---

```python
labels = 'x1 x2 s1 s2 s3'.split()
combination_labels = [*combinations(labels, m)]
num_basic_solutions = len(combination_labels)
print(f'Number of combinations: {num_basic_solutions}')
```


```python
df1 = pd.DataFrame(
    data=A,
    index=range(1, m + 1),
    columns=labels,
    )

df2 = pd.DataFrame(
    data=b,
    index=range(1, m + 1),
    columns=['b'],
    )

```

---


```python
df3 = pd.DataFrame(
    data=c,
    index=['z'],
    columns=labels,
    )

df4 = pd.DataFrame(
    data=combination_labels,
    index=range(1, num_basic_solutions + 1),
    columns=range(1, m + 1),
    )
```

```python
with pd.ExcelWriter('data.xlsx') as writer:
    df1.to_excel(writer, sheet_name='lhs')
    df2.to_excel(writer, sheet_name='rhs')
    df3.to_excel(writer, sheet_name='objective')
    df4.to_excel(writer, sheet_name='combinations')
```
---




<p class="outstanding-title">Método Analítico</p>