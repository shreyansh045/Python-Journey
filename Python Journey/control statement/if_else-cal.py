num1=float(input('Enter first no.= '))
num2=float(input('Enter second no.= '))
choice=input('Enter your choice + - * / = ')
if choice=='+':
    print(f'Addition={num1+num2}')

elif choice=='-':
    print(f'Subtraction={num1-num2}')

elif choice=='*':
    print(f'Multiplication={num1*num2}')

elif choice=='/':
    print (f'Division={num1/num2}')    

else :
   print ('Invalid choice')        
 