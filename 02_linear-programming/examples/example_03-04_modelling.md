## Example 3.3: A vehicle mix problem

A curtain manufacturer receives three orders for curtain material with widths and lengths as follows:

Order Number | Width (m) | Length (Number of Rolls)
----- | ----- | -----
1 | 2.5 | 30
2 | 3.8 | 50
3 | 4.9 | 10

Rolls of curtain material are produced in two standard widths, 5 and 10 m. These can be cut to the sizes specified by the order. There is no practical length limitation as rolls can be joined together. Determine the production
plan that minimizes the curtain material trim loss.


### Solution
#### Defining the variables:
The variables can be defined using subscripts of notation such as i, where i has a range of values $(i ?=1, 2, \ldots , n)$.
$X_{1i} = \text{number of rolls produced from a 5 m width roll of orders combination} i$
$X_{2i} = \text{number of rolls produced from a 10 m width roll of orders combination} i$


The 5 m width roll can be cut in three different ways and the 10 m width roll can be cut in six different ways to produce 2.5, 3.8, and 4.9 m width rolls. The variables are explained below to provide a better understanding.
Using a 5 m width roll, you can produce

- tow 2.5 m width rolls with no trim loss ($X_{11}$)
_ one 3.8 m width roll with 1.2 m trim loss ($X_{12}$) or
- one 4.9 m width roll with 0.1 trim loss ($X_{13}$)
