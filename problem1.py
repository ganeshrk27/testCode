
## Task: To obtain a specific standard deviation

## Import the libraries

import numpy as np
import pandas as pd


## Function to obtain the standard deviation

def getStd(ip):
    s = []

    df = pd.DataFrame(data=ip)
    
    (n , d) = df.shape
    
    # check if dimensions are correct
    if (n < 2 or n > 50) or (d < 1 or d > 50): 
        print("Wrong dimensions")
        return 0 

    df.replace(0, np.nan, inplace=True)

    df.apply(np.nanmean, axis=0).tolist()

    df.fillna(df.apply(np.nanmean, axis=0), axis=0, inplace=True )

    s = df.std(ddof=0, axis=0).tolist()
    # print(s)

    return s


## Test Cases
print("Input matrix")
ip2 = [[1, 2, 0], [0, 1, 1], [5, 6, 5]]
print(ip2)
print("Output")
op2 = getStd(ip2)
print(op2)
print()


print("Input matrix")
ip3 = [[1,2,0]]
print(ip3)
print("Output")
op3 = getStd(ip3)
print(op3)
print()

print("Input matrix")
ip4 = [[1, -5, 8], [-2, 0, -3], [2, 4, 7]]
print(ip4)
print("Output")
op4 = getStd(ip4)
print(op4)
print()

print("Input matrix")
ip5 = [[]]
print(ip5)
print("Output")
op5 = getStd(ip5)
print(op5)
print()

