# Examen Modelo En Red


Para el siguiente problema de “Optimización de Redes” el modelo matemático.

# Problema

Durante la fase de Optimización de Redes, el gerente decide sobre la ubicación y asignación de la capacidad de cada instalación. Además de esto, debe decidir sobre cómo asignar los mercados a las instalaciones. Esta asignación debe tomar en cuenta las restricciones de servicio al cliente en términos del tiempo de respuesta. Las decisiones sobre asignación de la demanda pueden modificarse con regularidad, conforme los costos cambian y los mercados evolucionan. Al diseñar la red, tanto las decisiones de ubicación como asignación deben de tomarse de manera conjunta. Ilustramos los modelos de optimización de la red relevantes utilizando el ejemplo de dos fabricantes de equipo de telecomunicaciones de fibra óptica.  Tanto Telexyz como H-Opt son fabricantes de la última generación de este tipo de equipo. 

Telexyz se ha enfocado en la mitad este de Estados Unidos. Tiene plantas de manufactura ubicadas en Baltimore, Memphis y Wichita para atender los mercados de Atlanta, Boston y Chicago. H-Opt se ha enfocado en la mitad oeste del país para atender los mercados de Denver, Omaha y Portland con plantas en Cheyenne y Salt Lake City.  **El costo variable de producción y transporte por millares de unidades** enviadas se muestran en la Tabla 1 [@tbl:costs]. La capacidad y los costos fijos mensuales de cada planta están en la Tabla 2. La demanda del mercado están en la Tabla 3. La capacidad y la demada se expresan en miles de unidades.




| Región de oferta | ATLANTA | BOSTON | CHICAGO | DENVER | OMAHA | PORTLAND |
|------------------|---------:|--------:|---------:|--------:|-------:|----------:|
| BALTIMORE        | 1,675   | 400    | 685     | 1,630  | 1,160 | 2,800    |
| CHEYENNE         | 1,460   | 1,940  | 970     | 100    | 495   | 1,200    |
| SALT LAKE        | 1,925   | 2,400  | 1,425   | 500    | 950   | 800      |
| MEMPHIS          | 380     | 1,355  | 543     | 1,045  | 665   | 2,321    |
| WICHITA          | 922     | 1,646  | 700     | 508    | 311   | 1,797    |

 : Costo variable de producción y transporte {#tbl:costs}.

 

| Fabrica   | Costo fijo mensual ($) | Capacidad Mensual |
|-----------|------------------------|-------------------|
| BALTIMORE | 7650                   | 18                |
| CHEYENNE  | 3500                   | 24                |
| SALT LAKE | 5000                   | 27                |
| MEMPHIS   | 4100                   | 22                |
| WICHITA   | 2200                   | 31                |

: Costos fijos y capacidad de producción de las fábricas.


| Mercado  | Demanda |
|----------|---------:|
| ATLANTA  | 10      |
| BOSTON   | 8       |
| CHICAGO  | 14      |
| DENVER   | 6       |
| OMAHA    | 7       |
| PORTLAND | 11      |

: Demanda de los mercados.


# Asignación de la demanda a las instalaciones de producción

Con base en la Tabla 1, calculamos que Telexyz tiene una capacidad de producción total de 71,000 unidades por mes y una demanda total de 30,000 unidades por mes, mientras que H-Opt tiene una capacidad de producción de 51,000 unidades por mes y una demanda de 24,000 por mes. Cada año, los gerentes de ambas compañías deciden cómo asignar la demanda a sus instalaciones de producción conforme cambian la demanda y los costos.


El problema de asignar la demanda se resuelve empleando el modelo de asignación de la demanda, el cual requiere de los siguientes datos:

- $n$ = número de ubicaciones fabriles
- $m$ = número de mercados o puntos de demanda
- $D_j$ = demanda anual del mercado $j$
- $K_i$ = capacidad de la fábrica $i$
- $c_{ij}$ = costo de producir y enviar una unidad de la fábrica $i$ al mercado $j$ (el costo incluye producción, inventario y transporte)

El objetivo es asignar la demanda de diferentes mercados a varias plantas para minimizar el costo total de las instalaciones, el transporte y el inventario. definimos las variables de decisión:

- $x_{ij}$ = cantidad enviada desde la fábrica $i$ al mercado $j$


# Instrucciones

Se solicita lo siguiente:

1. En Parejas (las que ya tienen asigndas).
2. Resolver con Gurobi Python.
3. Incluir el **diagrama de red**.
4. Los dos modelos a resolver son: 
    - Transporte.
    - Costo Fijo.
5. Entregar dos archivos [`.ipynb` (Jupyter Notebook)](https://youtu.be/xK8w0LWQ5q0?si=ojAOTKAqB0aJOdMl "notebook").
6. El archivo debe contener [documentación en celdas de texto](https://drive.google.com/drive/folders/1vwGNpJEH68QY74CG89JpDwPtFf8gfd3t?usp=drive_link "celdas de text"). 
   - Título y subtítulos
   - Incluir figuras
   - Incluir tablas
   - Incluir enlaces (links)
   - Conjuntos, Parámetros, Variables de Decisión, Función Objetivo, Restricciones. Usar fórmulas.
   - Determinar cual es la asignación que optmiza el costo del modelo. Usar una tabla para mostrar los resultados

Los modelos los resolvimos en Excel previamente, por lo tanto, **ya saben cuál es la solución óptima**.

# Bibliografía de apoyo

* Chase, R. B. y Aquilano, N. J. (2018). [Administración de operaciones, producción y cadena de suministros](https://drive.google.com/file/d/1U6cnpSMpuwWA82SmfvXbru_CjXOsHSfC/view?usp=sharing "chase"), 15a. ed., México (Mc Graw Hill)
* Sunil Chopra y Peter Mendil. (2018). [Administración de la cadena de suministros](https://drive.google.com/file/d/1mANYq0hcmx_6uqYgolPgAWR3eN8asCoI/view?usp=sharing "chopra"), 5a. ed., México (Pearson Educación)
* Ballou, R. H. (2004). [Logística. Administración de la Cadena de Suministro](https://drive.google.com/file/d/1LEHtjOSoByBpnKMUVLFwF9p5ouD3Z15v/view?usp=sharing "ballou"). 5a. ed., México (Pearson Educación)
* Anderson, D. R. Sweeney, D. J. & Williams, T. A. (2011). [Métodos cuantitativos para los negocios: (11 ed.)](https://elibro.net/es/lc/anahuac/titulos/93212 "anderson"). Cengage Learning. 

