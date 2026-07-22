# try and except,else,finally,raise
"""
n=int(input("Enter the number:"))
try:
    print(10/n)

except Exception as err:
    print(f"sorry there is an error {err}")

# else will run only if no exception occur 
else:
    print("Good there is no exception")

# finally will run code whether there is exception or not
finally:
    print("This will run no matter what")

print("ok i have done the division") 
"""


# manually throw an exception
age=int(input("Enter your age:"))
try:
    if age<10 or age>18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club")

except Exception as err:
    print(f"An error occured as {err}")

print("The club will start soon")
