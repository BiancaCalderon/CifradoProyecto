#Matrix Mult.py

import numpy as np
import math

mensaje = [7,0,24,16,20,4,18,4,17,3,14,12,14,11,14,18,3,8,6,17,0,5,14,18,26,18,14,11,14,21,4,17,7,0,2,8,0,0,3,4,11,0,13,19,4]
coded = []
a = np.array([[1,9,7],[3,5,2],[10,4,1]])
print("Mensaje cifrado")
for i in range (0, len(mensaje), 3):
    b = np.array(mensaje[i:i+3])
    c = np.dot(a,b)
    coded.append(c)
    print(c)

inv = np.array([[3/116,-19/116,17/116],[-17/116,69/116,-19/116],[19/58,-43/58,11/58]])
print("Mensaje descifrado")
for array in coded:
    b = (array)

    c = np.dot(inv, b)
    array = []
    for i in c:
        
        array.append((math.ceil(i-0.5)))
    print(array)
    


    
