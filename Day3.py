import math

def quadratic_equation (a,b,c):
    x1 = 0
    x2 = 0
    denta = b**2 - 4*a*c
    if denta ==0:
        x1=x2=-b/2*a
        print(f' x1=x2={-b/2*a}')
    else:
        if denta > 0:
            x1 = (- b - math.sqrt(denta) ) / (2*a)
            x2 = (- b + math.sqrt(denta) ) / (2*a)
            print(f'x1={x1}, x2={x2}')
        if denta < 0:
            print('Phương trình vô nghiệm!')

    
print ("Test case 1: a=2,b=6,c=4")
quadratic_equation(a=2,b=6,c=4)

print("Test case 2: a=1,b=2,c=1")
quadratic_equation(a=1,b=2,c=1)

print("Test case 3: a=4,b=6,c=3")
quadratic_equation(a=4,b=6,c=3)