from decimal import Decimal

while True:

   num11 = input("Enter first number: ")
   num1 = Decimal(num11)
   operator = input("What operation do you want to do?(+,-,*,/): ")
   num21 = input("Enter your second number: ")
   num2 = Decimal(num21)



   if operator == "+":
       print(num1 + num2)
   elif operator == "-":
       print(num1 - num2)
   elif operator == "*":
       print(num1*num2)
   elif operator == "/" and num2 != 0:
       print(num1/num2)
   elif operator == '/' and num2 == 0:
       print("You cannot divide a number by 0")
   else:
       print("That is not a valid operation")

   while True:
       answer = input('Run again? (y/n): ')
       if answer in ('y', 'n'):
           break
       print('Invalid input.')
   if answer == 'y':
       continue
   else:
       print('Goodbye')
       break
