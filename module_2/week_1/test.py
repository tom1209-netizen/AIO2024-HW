import numpy as np

arr = np.arange(0, 10)
arrNew = np.repeat(arr, 3)
print(arrNew)
print(np.tile(arr, 3))
