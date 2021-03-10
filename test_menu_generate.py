import datetime
from generate_menu import main, get_topping_list, get_non_vegan_topping_list

## TEST GUIDE: RUN  python test_menu_generate.py IN TERMINAL. IF THERE IS ASSERTIONERROR, THEN IT MEANS THE TEST DOESN'T PASS.

## constraints to be tested
## 1. the menu must contain exactly 10 different pizzas
## 2. a pizza must be comprised of between 0 and 12 toppings, inclusive, using only the toppings listed above
## 3. at least one vegetarian pizza must be offered
## 4. a combination of pizza toppings cannot be duplicated at any point during the year
## 5. on any given day, the Pizzeria staff should be able to generate the same menu multiple times (i.e. if they run out of all their menus, they should be able to print new ones)




## This file tests whether the generate_menu func could satisfy all the constraints or not
## I would loop for a whole year 2021 to test the first 4 constraints
## Loop for both 2021 and 2020 to test the 5th constraint
def test_generate_menu():
    topping_comb_list = list()
    ## test 2021 year
    begin = datetime.date(2021,1,1)
    end = datetime.date(2021,12,31)
    days = (end-begin).days
    for i in range(days+1):
        cur_date = (begin+datetime.timedelta(days=i)).strftime("%Y%m%d")
        menu = main(cur_date)
        assert len(menu)==10 ## constraint 1
        assert has_vegan_pizza_in_menu(menu) ##constraint 3
        previous_year_cur_date = "2020"+cur_date[4:]
        previous_year_menu = main(previous_year_cur_date)
        for pizza in menu:
            assert is_pizza_toppings_in_list(pizza) ## constraint 2
            assert pizza not in topping_comb_list ##constraint 4
            topping_comb_list.append(pizza)
            assert pizza in previous_year_menu ##constraint 5
    print("all tests passed")

def is_pizza_toppings_in_list(pizza):
    topping_list = get_topping_list()
    for topping in pizza:
        if topping not in topping_list:
            return False
    return True
    
def has_vegan_pizza_in_menu(menu):
    for pizza in menu:
        if is_vegan_pizza(pizza):
            return True
    return False

def is_vegan_pizza(pizza):
    non_vegan_toppings = get_non_vegan_topping_list()
    for non_vegan_topping in non_vegan_toppings:
        if non_vegan_topping in pizza:
            return False
    return True

if __name__=="__main__":
    test_generate_menu()
