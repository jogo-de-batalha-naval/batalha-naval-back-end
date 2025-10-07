import numpy as np

array= np.array([[1,2,3,4,5], 
                 [6,7,8,9,10],
                 [11,12,"a",14,15],
                 [16,17,18,19,20],
                 [21,22,23,24,25]])

print(array)
sort1= int(input("Escolha uma posição:"))
sort2= int(input("Escolha uma posição:"))
sort3= int(input("Escolha uma posição:"))


print(array[sort1,sort2:sort3])