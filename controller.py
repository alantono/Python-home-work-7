from view import menu, get_num
from functions import func_1, func_2, func_3, func_4, func_5, func_6


def button_click():
    n = get_num()
    if n == 5:
        func_5()
    elif n == 1:
        func_1()
    elif n == 2:
        func_2()
    elif n == 3:
        func_3()
    elif n == 4:
        func_4()
    elif n == 6:
        func_6()
    else:
        button_click()


menu()
