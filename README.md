# Distance
A python program that calculates the air distance between all pairs  from a list of locations. The location list is either provided by the user in a file or is randomly generated by the application.

The user can provide an integer **n** as the input argument. The algorithm randomly chooses n locations on earth and calculates their pairwise distances from each other. 
Moreover, it provides the average distance among locations and the pair closest to the average.

In case of an absent input argument, the algorithm automatically uses the predefined list of locations in the accompanying "places.csv" file.


## Features

* [x] [Numpy]()
* [x] [Pandas]()
* [x] [Geopy]()

## Usage

Running the program using terminal
```
$ python3 main.py <n>
```

where **n** is an optional argument and it determines the number of randomly chosen locations.



