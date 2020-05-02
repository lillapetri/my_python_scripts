'''
Complete the pattern #1 kata solutions from www.codewars.com.
'''

def pattern(n):
    x = ''
    for number in range(1, n+1):
        x += number*str(number)+'\n'
    return x.rstrip()

print(pattern(16))