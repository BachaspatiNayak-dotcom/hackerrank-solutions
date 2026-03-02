'''
WAP to print sum of indivisual digits of a number using recursion
'''
def summ(n):
    if n < 10:
        return n
    return (n % 10) + summ(n // 10)

print(summ(156))