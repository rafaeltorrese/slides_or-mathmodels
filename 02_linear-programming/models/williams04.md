# Optimización de la refinería


Una refinería de petróleo compra dos crudos (crudo 1 y crudo 2). Estos petróleos crudos se someten a cuatro procesos: destilación, reformado, craqueo y mezcla, para producir gasolinas y combustibles que se venden.

## Destilación
La destilación separa cada petróleo crudo en fracciones conocidas como nafta ligera, nafta media, nafta pesada, petróleo ligero, petróleo pesado y residuo según sus puntos de ebullición. Las naftas ligeras, medias y pesadas tienen octanos de 90, 80 y 70, respectivamente. Las fracciones en que se descompone un barril de cada tipo de crudo se dan en la siguiente tabla:

| -       | nafta ligera | nafta media | nafta pesada | Aceite ligero | Aceite pesado | Residuo |
|---------|--------------|------------:|-------------:|--------------:|--------------:|--------:|
| Crudo 1 | 0.10         |        0.20 |         0.20 |          0.12 |          0.20 |    0.13 |
| Crudo 2 | 0.15         |        0.25 |         0.18 |          0.08 |          0.19 |    0.12 |


NÓTESE BIEN. Hay una pequeña cantidad de desperdicio en la destilación.


## Reforma
Las naftas se pueden utilizar inmediatamente para mezclarlas con diferentes grados de gasolina o pueden pasar por un proceso conocido como reformado. El reformado produce un producto conocido como gasolina reformada con un octanaje de 115. Los rendimientos de gasolina reformada de cada barril de las diferentes naftas se dan como sigue:

- 1 barril de nafta ligera produce 0.60 barriles de gasolina reformada;
- 1 barril de nafta media rinde 0.52 barriles de gasolina reformada;
- 1 barril de nafta pesada produce 0.45 barriles de gasolina reformada.

## Craqueo

Los aceites (ligeros y pesados) pueden usarse directamente para mezclarlos con combustible para aviones o aceite combustible o someterse a un proceso conocido como craqueo catalítico. El craqueador catalítico produce aceite y gasolina craqueados. La gasolina craqueada tiene un octanaje de 105.

- 1 barril de petróleo ligero produce 0.68 barriles de petróleo craqueado y 0.28 barriles de gasolina craqueada;
- 1 barril de petróleo pesado produce 0.75 barriles de petróleo craqueado y 0.20 barriles de gasolina craqueada.

El aceite craqueado se utiliza para mezclar _aceite combustible_ y _combustible para aviones_; La gasolina craqueada se utiliza para mezclar gasolina. El residuo se puede utilizar para producir _aceite lubricante_ o mezclarlo con _combustible para aviones_ y _aceite combustible_:

- 1 barril de residuo produce 0,5 barriles de aceite lubricante.

## Mezcla

### Gasolina (combustible para motor)

Hay dos tipos de gasolina, regular y premium, que se obtienen mezclando nafta, gasolina reformada y gasolina craqueada. Las únicas estipulaciones que les conciernen son que los regulares deben tener un octanaje de al menos 84 y los premium deben tener un octanaje de al menos 94. Se supone que los octanos se mezclan linealmente por volumen.

### Combustible para aviones

La estipulación relativa al combustible para aviones es que su presión de vapor no debe exceder 1 kg cm<sup>2</sup>. Las presiones de vapor para aceites ligeros, pesados, craqueados y residuos son 1.0, 0.6, 1.5 y 0.05 kg cm<sup>2</sup>, respectivamente. Se puede suponer nuevamente que las presiones de vapor se mezclan linealmente según el volumen.

### Aceites combustibles

Para producir aceites combustibles, se deben mezclar petróleo ligero, petróleo craqueado, petróleo pesado y residuos en una proporción de 10:4:3:1. Existen limitaciones de disponibilidad y capacidad en las cantidades y procesos utilizados de la siguiente manera:

1. La disponibilidad diaria de crudo 1 es de 20,000 barriles.
2. La disponibilidad diaria de crudo 2 es de 30,000 barriles.
3. Se pueden destilar como máximo 45,000 barriles de crudo al día.
4. Se pueden reformar como máximo 10,000 barriles de nafta por día.
5. Se pueden craquear como máximo 8,000 barriles de petróleo al día.
6. La producción diaria de aceite lubricante deberá estar entre 500 y 1,000 barriles.
7. La producción de combustible de motor premium debe ser al menos el 40% de la producción de combustible de motor normal.

Las contribuciones a los beneficios de la venta de los productos finales son (en peniques por barril) las siguientes:


| Producto                 | Contribución |
|--------------------------|--------------:|
| gasolina premium         | 700          |
| gasolina normal          | 600          |
| Combustible para aviones | 400          |
| Combustible              | 350          |
| Aceite lubricante        | 150          |

¿Cómo deberían planificarse las operaciones de la refinería para maximizar la utilidad total?