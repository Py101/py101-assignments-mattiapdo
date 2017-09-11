'''
my first program in python
'''

import sys
numbers = sys.argv[1:]
a,b = float(numbers[0]),float(numbers[1])

print("the number you've passed are:")
print(a,b)

print("a+b=", a+b)
print("a/b", a/b)

