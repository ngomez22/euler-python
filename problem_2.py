"""
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""


def Fibonacci():
    a, b = 0, 1
    while a + b < 4000000:
        yield a + b
        a, b = b, a + b

f = Fibonacci()
print(sum([x for x in f if x % 2 == 0]))
