---
marp: true
title: "model-juice-production"
header: 'Construcción de Modelos'
footer: 'Introducción a la Programación Lineal'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>


# Elaboración de Zumos

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

---

<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>