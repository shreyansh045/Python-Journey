#check whether the no is prime or not

n=int(input("Enter your no."))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("Number is prime number")
else:
    print("Number is not prime")            
