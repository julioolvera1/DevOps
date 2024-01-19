'''
Write a function that accepts a radius and returns the area of a circle – search online for the correct equation to use. 
'''

import math as mt

def area_circle(radius):
    
    area=mt.pi*(radius**2)

    return area


if __name__ == '__main__':
    
    radius=float(input('Please enter the radius of the circle: '))
    
    area=area_circle(radius)

    print(f'The area of the circle is {area:.2f}')