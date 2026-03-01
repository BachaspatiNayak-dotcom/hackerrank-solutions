'''
WAP to check if a number is prime or not
'''
def isprime(n):
    if n>1:
       for i in range(2,int(n**0.5)+1):
         if n%i==0:
            return 'it is not a prime number'
       else:
          return 'it is a prime number'
    else:
        return 'it is not a prime number'
print(isprime(50))
print(isprime(-78))