# random function must be imported at first, it wouldn' work without it
import random
# a user must type his five numbers


def matches(n1, n2, n3, n4, n5):
    # all the chosen vairable will be stored in empty list
    win_list = []
    # each of the variable will choose random number from the specified list
    win_list += [random.choice([1, 2, 3, 4, 5])]
    win_list += [random.choice([6, 7, 8, 9, 10])]
    win_list += [random.choice([11, 12, 13, 14, 15])]
    win_list += [random.choice([16, 17, 18, 19, 20])]
    win_list += [random.choice([21, 22, 23, 24, 25])]
    # storages are used to store the matches
    stor1 = []
    stor2 = []
    stor3 = []
    stor4 = []
    stor5 = []
    # check_list is used to display matches in an order, from the smallest to the biggest numbers
    check_list = stor1, stor2, stor3, stor4, stor5
    # after first turn, the user will see his and chosen numbers
    print("-------------------------------------")
    print("Numbers of your ticket: ", n1, n2, n3, n4, n5)
    print("Numbers are: ", win_list)
    # if chosen number is in a list of randomly chosen numbers, than will add that number to it's storage and print it
    if n1 in win_list:
        stor1 = stor1.insert(0, n1)
        print(stor1)
    if n2 in win_list:
        stor2 = stor2.insert(1, n2)
        print(stor2)
    if n3 in win_list:
        stor3 = stor3.insert(2, n3)
        print(stor3)
    if n4 in win_list:
        stor4 = stor4.insert(3, n4)
        print(stor4)
    if n5 in win_list:
        stor5 = stor5.insert(4, n5)
        print(stor5)
    # will print check_list that is used to check, if the user won the price
    print(check_list)
    # final_list stores variables that are used in the verfication
    final_list = 0
    # if user's number is located in the check_list, than will add 1 unit to the final_list
    if any(n1 in s for s in check_list):
        final_list += 1
    if any(n2 in s for s in check_list):
        final_list += 1
    if any(n3 in s for s in check_list):
        final_list += 1
    if any(n4 in s for s in check_list):
        final_list += 1
    if any(n5 in s for s in check_list):
        final_list += 1
    # will print matches
    print("Matches:", final_list)
    # verify the if_function for each possible solutions
    if final_list == 5:
        print("Congratulations,you won £ 1.000.000.")
        print("________________________________________________________________")
        print("Your bank account: £ 1.000.000.")
    if final_list == 4:
        print("You won: £ 50.000.")
    

# matches(2,3,45,6,12)
