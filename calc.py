import math
print("Insert coefficients")
a = int(input("coefficient in front of X^2"))
b = int(input("coefficient in front of X "))
c = int(input("constant "))
D = b**2-4*a*c
print("The Discriminant is")
print (D)
if D < 0:
    print("No real number solutions")
elif D==0:
    solution = -b/(2*a)
    print("There is only one solution")
    print(solution)
else:
    solution1 = (-b+math.sqrt(D))/2*a
    solution2 = (-b-math.sqrt(D))/2*a
    print("There are two solutions")
    print(solution1)
    print(solution2)



