# Enter an integer to find its divisors.

x = int(input("Enter a number: "))
y = range(1,x+1)
# List comprehension
print([elem for elem in y if x % elem == 0])