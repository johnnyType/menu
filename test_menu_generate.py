import datetime
from generate_menu import main
## TEST GUIDE: RUN  python test_menu_generate.py IN TERMINAL. IF THERE IS ASSERTIONERROR, THEN IT MEANS THE TEST DOESN'T PASS.

## This file tests whether the generate_menu func could satisfy all the constraints or not
## I would loop for a whole year 2021 to test the first 3 constraints
## Loop for both 2021 and 2020 to test the 4th constraint
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
        assert has_vegan_pizza_in_menu(menu) ##constraint 2
        previous_year_cur_date = "2020"+cur_date[4:]
        previous_year_menu = main(previous_year_cur_date)
        for pizza in menu:
            assert pizza not in topping_comb_list ##constraint 3
            topping_comb_list.append(pizza)
            assert pizza in previous_year_menu ##constraint 4
    
def has_vegan_pizza_in_menu(menu):
    for pizza in menu:
        if is_vegan_pizza(pizza):
            return True
    return False

def is_vegan_pizza(pizza):
    non_vegan_toppings = ["ham","bacon","pepperoni"]
    for non_vegan_topping in non_vegan_toppings:
        if non_vegan_topping in pizza:
            return False
    return True

if __name__=="__main__":
    test_generate_menu()