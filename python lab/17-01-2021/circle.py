Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def findArea(r): 
    PI = 3.142
    return PI * (r*r)

>>> num=float(input("Enter r value:"))
Enter r value:4
>>> print("Area is %.6f" % findArea(num)); 

 
Area is 50.272000
>>> 