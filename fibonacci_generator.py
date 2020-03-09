'''
This is a fibonacci number generator.
Input: integer (n)
Output: list of integers (fibonacci numbers -> len = n)
'''

def gen_fib():
    n = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if n == 0:
        fib = []
    elif n == 1:
        fib = [1]
    elif n == 2:
        fib = [1, 1]
    elif n > 2:
        fib = [1, 1]
        while i < (n - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1

    return fib

# Example

print(gen_fib())