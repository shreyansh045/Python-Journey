#Reverse a string

""""
a="SHREYANSH"    #print(a[ : : -1])
b="" 
for i in range(len(a)-1,-1,-1):
    b=b+a[i]     #print(a[i])
print(b)   """ 

#check pallindrome or not

a="SHREYANSH"
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
if b==a:
    print("String is pallindrome")
else:
    print("string is not pallindrome")        