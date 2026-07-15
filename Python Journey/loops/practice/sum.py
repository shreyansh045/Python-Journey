#sum upto n

"""n=int(input("Enter the no.:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(f"Your sum is {sum}") """

#factorial

"""n= int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"Your factorial is {fact}")    """

#Print the sum of all even and odd no in a range separately

n=int(input("Enter your number:"))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print(f"your even and odd sum are {even},{odd}")