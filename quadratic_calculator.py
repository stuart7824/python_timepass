import math
a = int(input("Enter the co efficient of X^2: ")
b = int(input("Enter the co efficient of X: ")
c = int(input("Enter the constant : ")
z = math.sqrt((b*b)-(4*a*c))
root1 = ((-b+z)/(2*a))
root2 = ((-b-z)/(2*a))
print("The roots are", root1, "and", root2)
