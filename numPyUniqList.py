
import numpy as np

myList = ["A","B","C","A","B","D","F"]

uniqueList, count = np.unnique(myList, return_counts=True)

print(uniqueList, count)

