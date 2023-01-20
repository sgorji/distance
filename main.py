import sys
import numpy as np
import pandas as pd

# Geography
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.distance import geodesic as gd

geolocator = Nominatim(user_agent='Airmine')

fileInputFlag = False


def randomPlaces(n):
    # randomly generated coordinates and places
    # but this way does not generate a uniform distribution
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

    print(f'Generated {n} random places.')
    df = pd.DataFrame(data = places, 
                        columns = ['Name', 'Latitude', 'Longitude'])
    return df


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
else:
    df = randomPlaces(n)

print(df.to_string()) 

