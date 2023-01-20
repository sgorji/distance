import sys
import numpy as np
import pandas as pd

fileInputFlag = False


def randomPlaces(n):
    print(f'Generate {n} random places.')
    return


argc = len(sys.argv)
if (argc > 1):
    try:
        n = int(sys.argv[1])
    except:
        print('Invalid argument!')
        fileInputFlag = True
else:
    fileInputFlag = True

if fileInputFlag:
    df = pd.read_csv('places.csv')
    print(df.to_string()) 
else:
    randomPlaces(n)


