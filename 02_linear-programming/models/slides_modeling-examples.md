---
marp: true
title: "slides_modeling-examples"
header: 'Modelado Matemático'
footer: 'Introducción a la Programación Lineal'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>


# 01 Destilación de Crudos

Una compañía de petróleos produce en sus refinerías gasóleo ($G$), gasolina sin plomo ($P$) y gasolina súper ($S$) a partir de dos tipos de crudos,$C_1$ y $C_2$. Las refinerías están dotadas de dos tipos de tecnologías.

La tecnología nueva $T_n$ utiliza en cada sesión de destilación 7 unidades de $C_1$ y 12 de $C_2$, para producir 8 unidades de $G$, 6 de $P$ y 5 de $S$. Con la tecnología antigua $T_a$, se obtienen en cada destilación 10 unidades de $G$, 7 de $P$ y 4 de $S$, con un gasto de 10 unidades de $C_1$ y 8 de $C_2$.

---

Estudios de demanda permiten estimar que para el próximo mes se deben producir al menos 900 unidades de $G$, 300 de $P$ y entre 800 y 1700 de $S$. La disponibilidad de crudo $C_1$ es de 1400 unidades y de $C_2$ de 2000 unidades.

Los beneficios por unidad producida son

| Gasolina    | $G$ | $P$ | $S$ |
|:------------|:---:|:---:|:---:|
| Beneficio/u |  4  |  6  |  7  |


  La compañía desea conocer **cómo utilizar ambos procesos de destilación**, que se pueden realizar total o parcialmente, y los crudos para que el **beneficio sea el máximo**.


# 02 Problema de la Dieta
  
En un centro de nutrición de desea obtener la dieta de coste mínimo con unos determinados requisitos vitamínicos para un grupo de niños que van a asistir a campamentos de verano. El especialista estima que la dieta debe contener entre 26 y 32 unidades de vitamina $A$, al menos 25 unidades de vitamina $B$ y 30 de $C$, y, a lo sumo, 14 de vitamina $D$. 

Se desea **construir un modelo de programación lineal** para conocer la cantidad de cada alimento que hay que preparar y que satisfaga los requisitos propuestos **con coste mínimo**.

---

La siguiente tabla nos da el número de unidades de las distintas vitaminas por unidad de alimento consumido para seis alimentos elegidos, denominados 1, 2, 3, 4, 5, 6, así como su coste por unidad

<br>

| Alimentos | A | B | C | D | costo \$ / unidad |
|-----------|---|---|---|---|-------------------|
| 1         | 1 | 1 | 0 | 1 | 10                |
| 2         | 1 | 2 | 1 | 0 | 14                |
| 3         | 0 | 1 | 2 | 0 | 12                |
| 4         | 3 | 1 | 0 | 1 | 18                |
| 5         | 2 | 1 | 2 | 0 | 20                |
| 6         | 1 | 0 | 2 | 1 | 16                |



# 03 Producción de gasolinas

Una compañía de petróleos produce tres tipos de gosolinas: Súper, Normal y Euro. Se obtienen por mezcla de tres calidades de crudos ($A$,$B$,$C$) que contienen tres componentes (1,2,3). La participación de estos componentes en la composición de cada crudo se muestra en la Tabla 1 en porcentaje 



| Crudos | 1  | 2  | 3  |
|--------|----|----|----|
| A      | 8  | 10 | 5  |
| B      | 45 | 30 | 20 |
| C      | 30 | 40 | 25 |


---

y las especificaciones de los tres tipos de gasolina en la Tabla 2 (porcentaje):

|        | 1         | 2         | 3         |
|--------|-----------|-----------|-----------|
| Super  | $\geq$ 60 | $\leq$ 25 | $\geq$ 10 |
| Normal | $\geq$ 50 | $\leq$ 30 | $\leq$ 15 |
| Euro   | $\leq$ 40 | $\geq$ 35 | $\geq$ 20 |

---

Los costes por barril de crudos $A$, $B$ y $C$ son 650, 500 y 450 $, respectívamente. El presupuesto diario de compra es de 50 millones \$; la disponibilidad diaria de crudos $B$ y $C$ se limita, respectivamente, a 3,000 y 7,000 barriles. Ciertos acuerdos obligan a comprar al menos 2,500 barriles de $A$ por día. 

Las demandas de gasolina Súper y Normal son de 2,000 y 2,500 barriles diarios, que deben satisfacerse. La compañía desea **maximizar la producción** de gasolina Euro. Formular un **modelo de programación lineal** que dé respuesta al problema planteado por la compañía.

---

<img src="https://res.cloudinary.com/rafaeltorrese/image/upload/v1708524471/operations-research/02_linear-programming-introduction/03_gasoline-production.png" class="center" width="800" height="800"> 


# 04 Elaboración de Zumos

Una empresa de alimentación produce zumos de pera; naranja, limón, tomate, manzana, además de otros dos tipos denominados $H$ y $G$ que son combinados de algunos de los anteriores. La disponibilidad de fruta para el periodo próximo, así como los costes de producción y los precios de venta paro los zumos, vienen dados en la Tabla 1.

---

| Fruta         | Disponibilidad Máxima (kg) | Costo (\$ / kg) | Precio venta (\$ / L) |
|---------------|----------------------------|-----------------|-----------------------|
| Naranja ($N$) | 32,000                     | 94              | 129                   |
| Pera ($P$)    | 25,000                     | 87              | 125                   |
| Limón ($L$)   | 21,000                     | 73              | 110                   |
| Tomate ($T$)  | 18,000                     | 47              | 88                    |
| Manzana ($M$) | 27,000                     | 68              | 97                    |


---


Las especificaciones y precios de venta de los combinados vienen dados en la Tabla 2.


| Combinado | Especificación                                                                   | Precio venta (\$ / Ltr.) |
|-----------|:---------------------------------------------------------------------------------|--------------------------|
| $H$       | No más del 50\% de $M$,<br> No más del 20\% de $P$,<br> No menos del 10\% de $L$ | 100                      |
| $G$       | 40\% de $N$, <br> 35\% de $L$, <br> 25\% de $P$                                  | 120                      |


---

- La demanda de los distintos zumos es grande, por lo que se espera vender toda la producción. 
- Por cada kg de fruta, se produce un litro del correspondiente zumo. 
- **Determinar los niveles de producción de los siete zumos**, de manera que se tenga **beneficio máximo** en el periodo entrante.

## Variables de Decisión

Observemos que los recursos son las cinco clases de fruta, y que los productos son, además de los zumos obtenidos directamente de éstas, los dos combinados. Una posible definición de las variables de decisión consiste en considerar las posibles combinaciones recursos-productos. Así, se tendrán 11 variables de decisión que denotamos

$$X_{NN}, X_{NG}, X_{PP}, X_{PH}, X_{PG}, X_{LL}, X_{LH}, X_{LG}, X_{TT}, X_{MM}, X_{MH}$$

donde $X_{NN}$ es la cantidad de naranjas utilizada para hacer zumo de naranja, $X_{NG}$ la cantidad de naranjas utilizadas para el combinado de zumo de tipo $G, \textellipsis$.

# 05 Planificación de la producción

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

# 06 Optimización de Mezclas en una Destilería

Una destilería dispone de malta propia en cantidad de 200 barriles/día. Además, puede comprar malta de dos distribuidores $A$ y $B$, con costes de 1000 y 1200 \$/barril, en cantidades máximas de 300 y 500 barriles/día, respectivamente. 

La malta puede mezclarse directamente o destilarse para producir malta enriquecida de dos tipos 1, 2. El destilador puede procesar a lo sumo 700 barriles/día. 

Un barril destilado de la propia casa produce 0.3 barriles de malta 1 y 0.6 de malta 2. Un barril de malta $A$ produce 0.4 de 1 y 0.4 de 2. Uno de malta $B$ produce 0.7 de 1 y 0.1 de 2. 

La mezcla de malta no procesada se vende a 1300 \$/barril, limitándose el mercado a 110 barriles/día.  El sobrante de malta debe destruirse con coste 100 \$/barril.

---

Con las maltas destiladas pueden hacerse dos productos: uno de alta calidad ($H$), que se vende a 1,900 \$/barril y debe contener al menos el 70\% de producto 1, y otro de baja calidad ($L$), que se vende a 1,500 \$/barril y puede contener a lo sumo el 55\% de producto 2.

La destilería desea satisfacer la demanda del producto de alta calidad, que es de 215 barriles/día, y asegurarse un beneficio de 30,000 \$/día. Además, puesto que se espera un cambio en el mercado del producto de baja calidad, la destilería desea minimizar su producción.

Formular un modelo de programación lineal que de respuesta al problema de planificación planteado teniendo en cuenta las limitaciones en la producción y las exigencias de demanda y beneficio económico, suponiendo, además, que la venta de la mezcla está garantizada.

# 07 Planificación de una planta química

Una planta química fabrica tres sustancias $A$, $B$ y $C$, utilizando carb6n como materia prima básica. La planta dispone de minas propias que pueden producir hasta 600 u/día de carbón con coste de 2000 $/u. Si la compañía necesita más carbón, puede adquirirlo a un distribuidor con un coste de 5000 $/n. Además, utiliza en el proceso de producción agua, electricidad, gasóleo y mano de obra. La compañía eléctrica administradora posee el siguiente sistema escalonado de tarifas

- 34,000 $/u para las primeras 2000 u(por día).
- 51,000 $/u para las primeras 800 u a partir de 2000 u
- 63,000 $/u a partir de 2800 u

---

La compañía de agua carga 7000  $/u de agua utilizada por día hasta 900 unidades y 8500 $/1t por encima de 900 unidades. Compra gasóleo a 4900 $/u, pero se restringe por motivos ecológicos al uso de 3000 unidades de gasóleo por día. Utilizando horario normal, la mano de obra disponible es de 750 horas sin costo. 

Puede conseguir hasta 220 horas extra con coste 15,200 $/hora. El resto de los datos del proceso de producción se dan en la siguiente tabla que contiene las unidades necesarias para fabricar cada unidad de sustancia, así como sus precios de venta.

---


| Sust. | Carb. | Elec. | Agua | Gas. | Horas | Beneficio / u ( $\times 10^3$ \$)                                             |
|-------|-------|-------|------|------|-------|:------------------------------------------------------------------------------|
| A     | 0.60  | 3.20  | 1.00 | 2.00 | 2.00  | 290 para las primeras 856 y 240 para las siguientes y 240 para las siguientes |
| B     | 0.90  | 2.50  | 0.26 | 2.40 | 3.00  | 320 / u hasta un máximo de 95 u                                               |
| C     | 1.20  | 4.00  | 1.70 | 3.00 | 2.00  | 3080 / u                                                                      |


Formular un modelo de programación lineal que proporcione el plan de producción de beneficio máximo

---

<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>