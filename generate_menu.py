from utils.date_to_number import date_to_number
from utils.num_to_binary_list import num_to_binary_list
from utils.filter_list import filter_list

def main(date):
    ## topping list orders as three non-vegan toppings as the first 3 elements, the rest 9 topping are all vegan
    topping_list = ["ham","bacon","pepperoni","garlic","mushroom","pineapple","green peppers","arugula","basil","onion","olives","artichoke"]
    ## map today date to a fixed number based on month and day, the num range is from 1 to 372
    num = date_to_number(date)
    menu = []

    ## get one topping combination from vegan combinations, the possible number is from 1 to 511 
    vegan_topping_comb = filter_list(topping_list,num_to_binary_list(num))
    menu.append(vegan_topping_comb)

    ## get one topping combination from non-vegan combinations, the possible number is from 512 to 4095
    ## the current num range is from 512+(num-1)*9 to 511+num*9
    for i in range(9):
        cur_num = 512+(num-1)*9+i
        non_vegan_topping_comb = filter_list(topping_list,num_to_binary_list(cur_num))
        menu.append(non_vegan_topping_comb)
    print(menu)
    return menu
    


if __name__=="__main__":
    import sys
    main(sys.argv[1])