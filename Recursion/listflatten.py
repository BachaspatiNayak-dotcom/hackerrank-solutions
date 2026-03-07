'''
WAP to flatten a list.
I/P=[10,[20,30],[[56,78]]]
O/P=[10,20,30,56,78]
'''
def flatten(L):
    print('entering:',L)
    L1=[]
    for ele in L:
        if isinstance(ele,list):
            L1.extend(flatten(ele))
        else:
            L1.append(ele)
    print('returning:',L1)
    return L1
print(flatten([10,[20,30],[[56,78]]]))