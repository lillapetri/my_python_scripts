'''
Special Number kata solutions from www.codewars.com

A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5
Given a number determine if it special number or not .
'''

def special_number(number):
    number = str(number)
    allowed_numbers = {'0', '1', '2', '3', '4', '5'}
    if set(number).issubset(allowed_numbers):
        return "Special!!"
    else:
        return "NOT!!"

def special_number2(number):
    return "Special!!" if max(str(number)) <= "5" else "NOT!!"

