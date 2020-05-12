def menu():
    print('welcome to budgetLy, here are your possible actions:')
    print('1 - check balance')
    print('2 - edit/register/delete categories')
    print('3 - edit/register/delete new transactions')
    print('4 - exit')

    option = int(input())
    check_input(option)

from menuFunctions import *

def check_input(op):
    if(op != 1 and op != 2 and op != 3 and op != 4):
        print('choose a valid option')
        menu()
    elif(op == 1):
        checkBalance()
    elif(op == 2):
        manageCategories()
    elif(op == 3):
        manageTransactions()
    elif(op == 4):
        pass

menu()

#TODO finish API (all database functios running properly)
