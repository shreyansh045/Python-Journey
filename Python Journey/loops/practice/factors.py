#factors
"""
n=int(input("Enter the no you want to find factors:"))
for i in range(1,n+1):
    if n%i==0:
        print(i) """

#Perfect number or not like factors of 6 = 1+2+3

n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("Your no. is perfect no.")     
else :
    print("your no. is not a perfect number")       
