---
theme: default
header: "Modelos Matemáticos"
title: "Programación Matemática"
footer: "Investigación de Operaciones"
author: Rafael Torres Escobar
headingDivider: 2
paginate: true
style: |
  h1 {
    text-transform: capitalize;
    font-size: 40px; /* Larger font size for heading */
    font-family: "Lucida Console";
    color:  #069;
    position: fixed;
    top: 45px;
    margin-bottom: 10px;

  }

  h2 {
    font-size: 35px; /* Larger font size for heading */
    font-family: "Lucida Console";
    color: #0000ff; 
    position: fixed;
    top: 35px; 
  }
 
  p {
    text-align: justify;
    text-justify: inter-word;
  }
  
   li {
    text-align: justify;
  }
  
  strong {
    color: red;
  }
  
  .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  
  img {
    max-width: 100%;
    height: auto;
  }
 
  section {
    position: top;
  }
  
  table {
    width: 100%;
    font-size: 25px;
  }
  
  th {
    color: black;
    text-align: center;
  }

  td {
    text-align: center;
    font-size: 25px;
  }
  
  .outstanding-title {
    font-family: "Lucida Console";
    font-size: 58px; /* Adjust the font size */
    text-align: center;
    font-weight: bold; /* Make the text bold */
    color: #ff5722; /* Set the text color */
    color:  #069;
    text-transform: uppercase; /* Convert text to uppercase */
    letter-spacing: 2px; /* Increase letter spacing for emphasis */
    line-height: 1.2; /* Set line height for readability */
    margin-bottom: 20px; /* Add space at the bottom */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Add a shadow for depth */
  }
  
  .definition-block {
    border: 2px solid #007bff; /* Blue border */
    border-radius: 5px; /* Rounded corners */
    padding: 10px; /* Padding inside the block */
    margin-bottom: 20px; /* Bottom margin for spacing */
  }
  
  h3 {
    text-transform: uppercase;
    border: 2px solid #3cb371;
    border-radius: 5px; /* Rounded corners */
    padding: 10px; /* Padding inside the block */
    margin-bottom: 10px; /* Bottom margin for spacing */
    color: #0000ff; /* Blue color for heading */
    font-size: 20px; /* Larger font size for heading */
    margin-top: 0; /* Remove top margin for heading */
  }
---


<p class="outstanding-title">Construcción de Modelos Matemáticos</p>

<!-- _paginate: skip -->


# Producción de gasolinas

Una compañía de petróleos produce tres tipos de gosolinas: Súper, Normal y Euro. Se obtienen por mezcla de tres calidades de crudos ($A$,$B$,$C$) que contienen tres componentes (1,2,3). La participación de estos componentes en la composición de cada crudo se muestra en la Tabla 1 en porcentaje y las especificaciones de los tres tipos de gasolina en la Tabla 2 (porcentaje):

---

| Crudos | 1  | 2  | 3  |
|--------|----|----|----|
| A      | 8  | 10 | 5  |
| B      | 45 | 30 | 20 |
| C      | 30 | 40 | 25 |



|       | 1        | 2        | 3        |
|--------|----------|----------|----------|
| Super  | $\geq$ 60 | $\leq$ 25 | $\geq$ 10 |
| Normal | $\geq$ 50 | $\leq$ 30 | $\leq$ 15 |
| Euro   | $\leq$ 40 | $\geq$ 35 | $\geq$ 20 |

---

Los costes por barril de crudos *A*, *B* y *C* son 650, 500 y 450 $, respectívamente. El presupuesto diario de compra es de 50 millones $; la disponibilidad diaria de crudos *B* y *C* se limita, respectivamente, a 3000 y 7000 barriles. Ciertos acuerdos obligan a comprar al menos 2500 barriles de *A* por día. Las demandas de gasolina Súper y Normal son de 2000 y 2500 barriles diarios, que deben satisfacerse. La compañía desea maximizar la producción de gasolina Euro. Formular un modelo de programación lineal que dé respuesta al problema planteado por la compañía.

---

<img src="https://res.cloudinary.com/rafaeltorrese/image/upload/v1708524471/operations-research/02_linear-programming-introduction/03_gasoline-production.png" class="center" width="600" height="600"> 

---


<p class="outstanding-title">Construcción de Modelos Matemáticos</p>

<!-- _paginate: skip -->
