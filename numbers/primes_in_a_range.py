'''
WAP to print all prime numbers in a given range.
'''
def primes(LL,UL):
    for num in range(LL,UL+1):
        if num>1:
          for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
          else:
            print(num)
primes(1,100)