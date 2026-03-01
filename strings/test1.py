'''
finding how many times a given substring present in a given string
'''
MS=input('enter main string:')
SS=input('enter sub string:')
substring_count=0
for i in range(len(MS)-len(SS)+1):
    if MS[i:len(SS)+i]==SS:
        substring_count+=1
print(substring_count)