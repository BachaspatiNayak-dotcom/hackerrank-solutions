'''
WAP to print the character with the maximum occurence in a given string
'''
S=input('enter string:')
print(max(S,key=S.count))