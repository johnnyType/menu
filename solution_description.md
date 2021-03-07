##### We can observe that each topping combination can be determined by a 12 digits binary number.

##### Assume that our topping list is ordered as: (This order can give some benefits for us to offer a vegan pizza)
```
["ham","bacon","pepperoni","garlic","mushroom","pineapple","green peppers","arugula","basil","onion","olives","artichoke"]
|------ non vegan -------| --------------------------------------- vegan ------------------------------------------------|
```
  
##### For example, topping combination ```["mushroom","pepperoni","green peppers","arugula"]``` can be represented as 001010110000, which is equal to decimal number 688. 

##### We can also observe that all vegan pizzas can be represented as binary number from 0 to 000111111111, which is decimal number range from 0 to 511. That means there is 512 different kinds of vegan pizzas. (This is due to the benefit of specific order of topping list)

##### We can use the similar method to get the non-vegan pizzas number which is from 001000000000 to 111111111111, which is decimal number range from 512 to 4095. That means there is 3583 different kinds of non-vegan pizzas.


##### Based on the obeservation we can generate a menu on a date by:
- #####     map each date (day/month/year) to a range unique decimal number, which is calculated by day+(month-1)*31 (By this way, we can make the same date of different year will map to the same number and any generated number is unique among each year). We denote the number value as V. This V ranges from 1 to 372.
- #####     Then we directly select the vegan pizza based on V.
- #####     For the non-vegan pizza, the 9 non vegan pizza we select are the number values from 512+(V-1)*9 to 520+(v-1)*9
- #####     For each number we convert it into 12 digits binary number and then get topping combination based on the toppling list.
