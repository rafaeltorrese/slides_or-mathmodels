# Planificación de una fábrica 1

Una fábrica de ingeniería fabrica siete productos (PROD 1 a PROD 7) en las siguientes máquinas: cuatro amoladoras, dos taladros verticales, tres taladros horizontales, un barrenador y una cepilladora. Cada producto produce una determinada contribución a las ganancias (definida como £/precio de venta unitario menos el costo de las materias primas). Estas cantidades (en £/unidad) junto con los tiempos de producción unitaria (horas) necesarios en cada proceso se detallan a continuación. Un guión indica que un producto no requiere proceso.


| -                         | PROD1 | PROD2 | PROD3 | PROD4 | PROD5 | PROD6 | PROD7 |
|---------------------------|-------|-------|-------|-------|-------|-------|-------|
| Contribución al beneficio | 10    | 6     | 8     | 4     | 11    | 9     | 3     |
| Rectificado               | 0.5   | 0.7   | –     | –     | 0.3   | 0.2   | 0.5   |
| Taladrado vertical        | 0.1   | 0.2   | –     | 0.3   | –     | 0.6   | –     |
| Perforación horizontal    | 0.2   | –     | 0.8   | –     | –     | –     | 0.6   |
| Mandrinado                | 0.05  | 0.03  | –     | 0.07  | 0.1   | –     | 0.08  |
| Cepillado                 | –     | –     | 0.01  | –     | 0.05  | –     | 0.05  |

En el mes actual (enero) y los cinco meses siguientes, ciertas máquinas estarán fuera de servicio por mantenimiento. Estas máquinas serán las siguientes:

| Mes     | Máquinas                              |
|---------|---------------------------------------|
| Enero   | 1 molinillo                           |
| Febrero | 2 taladros horizontales               |
| Marzo   | 1 barrenador                          |
| Abril   | 1 taladro vertical                    |
| Puede   | 1 Amoladora y 1 Taladro vertical      |
| Junio   | 1 cepilladora y 1 taladro horizontal. |



Existen limitaciones de marketing para cada producto en cada mes. Estos son
dado en la siguiente tabla:


| Mes     | 1   | 2    | 3   | 4   | 5    | 6   | 7   |
|---------|-----|------|-----|-----|------|-----|-----|
| Enero   | 500 | 1000 | 300 | 300 | 800  | 200 | 100 |
| Febrero | 600 | 500  | 200 | 0   | 400  | 300 | 150 |
| Marzo   | 300 | 600  | 0   | 0   | 500  | 400 | 100 |
| Abril   | 200 | 300  | 400 | 500 | 200  | 0   | 100 |
| Mayo    | 0   | 100  | 500 | 100 | 1000 | 300 | 0   |
| Junio   | 500 | 500  | 100 | 300 | 1100 | 500 | 60  |


Es posible almacenar hasta 100 unidades de cada producto a la vez a un coste de 0,5 £ por unidad al mes. Actualmente no hay stocks, pero se desea tener un stock de 50 de cada tipo de producto a finales de junio.
La fábrica trabaja seis días a la semana con dos turnos de 8 h cada día. No es necesario considerar problemas de secuenciación.

¿Cuándo y qué debería fabricar la fábrica para maximizar el beneficio total? Recomendar cualquier aumento de precio y el valor de adquirir máquinas nuevas.
NÓTESE BIEN. Se puede suponer que cada mes consta sólo de 24 días hábiles.


# Planificación de una fábrica 2

En lugar de estipular cuándo cada máquina estará inactiva por mantenimiento en el problema de planificación de la fábrica, se desea encontrar el mejor mes para que cada máquina esté inactiva. Cada máquina debe estar fuera de servicio por mantenimiento en un mes de los seis, excepto las máquinas rectificadoras, de las cuales sólo dos deben estar fuera de servicio en cada seis meses. Amplíe el modelo para permitirle tomar estas decisiones adicionales. ¿Cuánto vale la flexibilidad adicional de permitir que se elijan los tiempos de inactividad?
