# Fabricación de alimentos 1


Un alimento se fabrica refinando aceites crudos y mezclándolos. Los aceites crudos son de dos categorías:

| Aceite             | Tipo  |
|--------------------|-------|
| Vegetable oils     | VEG 1 |
|                    | VEG 2 |
| Non-vegetable oils | OIL 1 |
|                    | OIL 2 |
|                    | OIL 3 |


Cada aceite puede comprarse para entrega inmediata (enero) o comprarse en el mercado de futuros para entrega en un mes posterior. Ls precios actuales y en el mercado de futuros se dan a continuación en (\$/ton):

| MONTH    | VEG 1 | VEG 2 | OIL 1 | OIL 2 | OIL 3 |
|----------|-------|-------|-------|-------|-------|
| January  | 110   | 120   | 130   | 110   | 115   |
| February | 130   | 130   | 110   | 90    | 115   |
| March    | 110   | 140   | 130   | 100   | 95    |
| April    | 120   | 110   | 120   | 120   | 125   |
| May      | 100   | 120   | 150   | 110   | 105   |
| June     | 90    | 100   | 140   | 80    | 135   |


El producto final se vende a \$150 por tonelada.
Los aceites vegetales y no vegetales requieren diferentes líneas de producción para su refinación. En cualquier mes no es posible refinar más de 200 toneladas de aceites vegetales y más de 250 toneladas de aceites no vegetales. No hay pérdida de peso en el proceso de refinación y se puede ignorar el costo de refinación.
Es posible almacenar hasta 1000 toneladas de cada aceite crudo para su uso posterior. El costo de almacenamiento de aceite vegetal y no vegetal es de \$5 por tonelada al mes. No se puede almacenar el producto final, ni tampoco los aceites refinados.

Existe una restricción tecnológica de dureza en el producto final. En las unidades en las que se mide la dureza, esta debe estar entre 3 y 6. Se supone que la dureza se mezcla linealmente y que las durezas de los aceites crudos son

| Aceite | Dureza |
|------|-----|
| VEG1 | 8.8 |
| VEG2 | 6.1 |
| OIL1 | 2.0 |
| OIL2 | 4.2 |
| OIL3 | 5.0 |


¿Qué política de compras y fabricación debe seguir la empresa para maximizar sus ganancias?
Actualmente hay almacenadas 500 toneladas de cada tipo de aceite crudo. Se requiere que estas existencias también existan a finales de junio.

# Fabricación de alimentos 2


Se desea imponer las siguientes condiciones adicionales al problema de la fabricación de alimentos:

1. La comida nunca podrá estar compuesta por más de tres aceites en un mes.
2. Si se utiliza un aceite en un mes, se deben utilizar al menos 20 toneladas.
3. Si se utiliza VEG 1 o VEG 2 en un mes, entonces OIL 3 también debe ser usado.
   
Ampliar el modelo de fabricación de alimentos para abarcar estas restricciones y encontrar la nueva solución óptima.

