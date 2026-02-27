
'''
given a number of times you need to ask user to input 2 sets and their respective 
no.of elements.then check if a set is subset of another
'''


t = int(input())

for _ in range(t):
    nA = int(input())
    A = set(map(int, input().split()))

    nB = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))
