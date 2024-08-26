---
marp: true
title: "model-chemical-factory-planning"
header: 'Construcción de Modelos'
footer: 'Introducción a la Programación Lineal'
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
---



<!-- _paginate: skip -->

<p class="outstanding-title">Construcción de Modelos Matemáticos</p>

# Planificación de una planta química

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