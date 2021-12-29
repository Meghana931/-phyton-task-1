"""to write a Python program which accepts the radius of a circle
 from the user and computes area.
 """

from math import pi
r = float(input("the radius of the circle :"))
print("the area of the circle with radius " + str(r) +" is:" + str(pi * r**2))

"""write a Python program to accept a filename from 
the user and print the extension of that.
"""

fn= input("Enter Filename: ")
f = fn.split(".")
print("Extension of the file is : " + f[-1])
|

