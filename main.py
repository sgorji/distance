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
                    if len(places) == n:
                        break
                except:
                    print('no name at ' + coordinateString)

    print(f'Generated {n} random places.')
    df = pd.DataFrame(data=places,
                      columns=['Name', 'Latitude', 'Longitude'])
    return df


def calculateDistance(df):
    distances = []
    for i, row1 in df.iterrows():
        for j, row2 in df.iterrows():
            if i < j:
                try:
                    distances.append([
                        row1['Name'],
                        row2['Name'],
                        '%10.2f km' % gd(row1[['Latitude', 'Longitude']],
                           row2[['Latitude', 'Longitude']]).km])
                except:
                    print(row1)
                    print(row2)
                    input('?')

    df = pd.DataFrame(distances, columns =['Name1', 'Name2', 'Distance'])
    sorted = df.sort_values(by=['Distance'])
    print(sorted)
    return sorted


def printOutput(df):
    averageDistance = df['Distance'].mean()
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
else:
    df = randomPlaces(n)

print(df.to_string())
calculateDistance(df)
printOutput()

