# find the solution for quadratic equation

import cmath

def solve_quadratic_eqn(a=0,b=0,c=0):
    d = (b**2) - (4*a*c)
    sol1 = (-b + cmath.sqrt(d))/(2*a)
    sol2 = (-b - cmath.sqrt(d))/(2*a)

    print(f"Two solutions are {sol1} and {sol2}")

solve_quadratic_eqn(1,5,6)