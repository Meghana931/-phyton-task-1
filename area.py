"""to write a Python program which accepts the radius of a circle
 from the user and computes area.
 """

import math as M  
Radius = float (input ("Please enter the radius of the given circle: "))  
area_of_the_circle = M.pi* Radius * Radius  
print (" The area of the given circle is: ", area_of_the_circle)  

"""write a Python program to accept a filename from 
the user and print the extension of that.
"""

fn= input("Enter Filename: ")
f = fn.split(".")
print("Extension of the file is : " + f[-1])