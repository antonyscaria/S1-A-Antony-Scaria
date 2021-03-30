Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = float(input("Enter first number: "))
Enter first number: 5
>>> num2 = float(input("Enter second number: "))
Enter second number: 7
>>> num3 = float(input("Enter third number: "))
Enter third number: 9
>>> if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3

   
>>> print("The largest number is",largest)
The largest number is 9.0
>>> 