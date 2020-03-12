'''
Automorphic number kata solutions from www.codewars.com

A number is called Automorphic number if and only if its square ends in the same digits as the number itself.
Given a number determine if it Automorphic or not .
examples:
25**2 = 625 -> 25 is an automorphic number
13**2 = 169 -> 13 is not an automorphic number
'''

def automorphic(n):
    x = len(str(n))
    sq = str(n*n)
    return "Automorphic" if sq[-x:] == str(n) else "Not!!"

def automorphic2(n):
    return "Automorphic" if str(n*n).endswith(str(n)) else "Not!!"
