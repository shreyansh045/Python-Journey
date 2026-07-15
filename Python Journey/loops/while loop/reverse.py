#   revesre a number

"""n=int(input("Enter the number:"))
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
print(rev) """

# chech the no is pallindrome or not
 
n=int(input("Enter your number:"))
copy=n 
rev=0
while n>0:
 rev=rev*10+n%10
 n=n//10
if copy==rev:
 print("It is pallindrome number")
else:
 print("It is not pallindrome")