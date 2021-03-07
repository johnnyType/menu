##### We can observe that each topping combination can be determined by a 12 digits binary number.

##### Assume that our topping list is ordered as: (This order can give some benefits for us to offer a vegan pizza)
```
["ham","bacon","pepperoni","garlic","mushroom","pineapple","green peppers","arugula","basil","onion","olives","artichoke"]
|------ non vegan -------| --------------------------------------- vegan ------------------------------------------------|
```
  
##### For example, topping combination ```["mushroom","pepperoni","green peppers","arugula"]``` can be represented as 001010110000, which is equal to decimal number 688. 

##### We can also observe that all vegan pizzas can be represented as binary number from 0 to 000111111111, which is decimal number range from 0 to 511. That means there is 512 different kinds of vegan pizzas.

##### We can use the similar method to get the non-vegan pizzas number which is from 001000000000 to 111111111111, which is decimal number range from 512 to 4095. That means there is 3583 different kinds of non-vegan pizzas.


##### Based on the obeservation we can generate a menu on a date by:
- ##### map each date to a range unique decimal number
- ##### convert decimal number to a 12 digits decimal number
