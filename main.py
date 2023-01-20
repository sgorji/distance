import sys
import numpy as np
import pandas as pd

# Geography
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent='Airmine')

fileInputFlag = False


def randomPlaces(n):
    # randomly generated coordinates
    # but this way does not generate an uniform distribution
    places = []
    while len(places) < n:
        coordinates = (np.random.rand(n, 2) * [180, 360]) - [90, 180]
        for latitude, longitude in coordinates:
            coordinateString = str(latitude) + ',' + str(longitude)
            location = geolocator.reverse(coordinateString)
            if location:
                try:
                    name = location[0].split(',')[0]
                    places.append([name, latitude, longitude])
                except:
                    print('no name at ' + coordinateString)

    print(f'Generate {n} random places.')
    print(places)
    return places


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


