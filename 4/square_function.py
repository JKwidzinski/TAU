from math import sqrt

def calculate_roots(a,b,c):
    if a==0 or b==0:
        raise ValueError("a and b must be different than 0")
    
    delta = pow(b, 2) - 4*a*c
    
    if delta == 0:
        return float("{:.2f}".format((-b)/(2*a)))
    elif delta < 0:
        return None
    else:
        return [float("{:.2f}".format((-b + sqrt(delta))/(2*a))) , float("{:.2f}".format((-b - sqrt(delta))/(2*a)))]

print(calculate_roots(3,6,3))