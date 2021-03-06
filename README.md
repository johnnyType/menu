# Pizza Generator
For the upcoming calendar year, Pizzeria will generate their pizza menu every 
morning. Pizzas are defined by the combination of toppings, e.g. ["garlic", "mushroom"], 
["pineapple", "ham", "onion", "green peppers"], ["basil"]. 
Various orderings of the same toppings constitute only one combination, i.e. ["mushroom", "sausage"] and 
["sausage", "mushroom"] are considered to be the same.

The toppings available will be:
- garlic
- mushroom
- pineapple
- pepperoni
- green peppers
- arugula
- bacon
- basil
- onion
- ham
- olives
- artichoke

The following constraints govern each day's menu:
- the menu must contain exactly 10 different pizzas
- a pizza must be comprised of between 0 and 12 toppings, inclusive, using only the toppings listed above
- at least one vegetarian pizza must be offered
- a combination of pizza toppings cannot be duplicated at any point during the year
- on any given day, the Pizzeria staff should be able to generate the same menu multiple times (i.e. if they run out of all their menus, they should be able to print new ones)

Your task is to write a program that can generate daily menus everyday for a calendar year. 
When the program is run it should output the menu to the command line. You may use any 
programming language you like. 

The submitted project should contain a testing suite that demonstrates the constraints are met.

## Example
A solution written in Python might be run like this:
```bash
python generate_todays_menu.py
```

And produce output like this:
```bash
basil, bacon 
pepperoni
arugula, garlic
basil, onion, olives
artichoke, onion, ham, green peppers, mushroom, pineapple, garlic
mushroom, ham
pineapple, bacon, basil, garlic
artichoke, ham, onion
green peppers
ham, olives, pineapple, arugula, artichoke, mushroom
```


