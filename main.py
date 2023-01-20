import sys
import numpy as np
import pandas as pd

# Geography
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.distance import geodesic as gd

geolocator = Nominatim(user_agent='Airmine')


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

    df = pd.DataFrame(
        data=places,
        columns=['Name', 'Latitude', 'Longitude']
        )
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
                        gd(row1[['Latitude', 'Longitude']],
                           row2[['Latitude', 'Longitude']]).km,
                        'km'])
                except:
                    print(row1)
                    print(row2)
                    input('?')

    # Convert distance list to a dataFrame and sort pairs by distance
    df = pd.DataFrame(
        distances, 
        columns=['Name1', 'Name2', 'Distance', 'Unit']
        ).sort_values(by=['Distance'])
    return df


def printOutput(df):
    # Average distance
    avgDist = df['Distance'].mean()

    # Finding the closest value to the average
    closest = df.iloc[(df['Distance']-avgDist).abs().argsort()[:1]]
    p1 = closest['Name1'].tolist()[0]
    p2 = closest['Name2'].tolist()[0]
    dist = closest['Distance'].tolist()[0]

    print(df.to_string(index=False, justify='left'))
    print(f'Average distance: {avgDist:.3f} km. Closest pair: ' +
          f'{p1} - {p2} {dist:.3f} km.')
    return


# Optional input argument 'n' and default input file as fallback 
try:
    n = int(sys.argv[1])
    df = randomPlaces(n)
except:
    df = pd.read_csv('places.csv')

df = calculateDistance(df)

printOutput(df)
