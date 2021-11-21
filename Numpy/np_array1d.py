import numpy as np
from numpy.lib.function_base import delete

if __name__  == "__main__":
    arr = np.array([10, 20, 30])
    print(arr)
    print(arr.ndim)

    print(arr[0]) # get first element of array  
    print(arr[-1]) # get last element of array

    for i in arr:
        print(type(i))