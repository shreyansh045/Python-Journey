# a="shreyan123456!@#$%^" 
a=input("Enter the string : ")
alpha=0
num=0
spchr=0
for i in a:
    if i.isalpha():     #string methods
        alpha+=1
    elif i.isdigit():
        num+=1
    else:
        spchr+=1
print(f"Your alphabets are {alpha}\n your digits are {num} \n your spchr are {spchr}")       

# print(dir(str))