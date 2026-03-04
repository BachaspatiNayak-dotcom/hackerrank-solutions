'''
I/P='Python is very easy'
O/P={'python':1,'is':1,'very':1,'easy':2}
every word is a key and the no.of vowels present in that word is their respective values
'''
S=input('enter string:')
L=S.split()
D=dict()
for ele in L:
    count=0
    for i in ele.lower():
        if i in 'aeiou':
            count+=1
    D[ele]=count
print(D)