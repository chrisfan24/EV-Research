###correlate distance of places where EVs park / charge most frequently
###to the distance of POIs, their rating, their prices

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt

point_types = pd.read_csv("/Users/chrisfan/Documents/Research/FleetPower/sandiego/san_diego_point_types.csv")
points = pd.read_csv("/Users/chrisfan/Documents/Research/FleetPower/sandiego/san_diego_points.csv")
sd_cars = pd.read_csv("/Users/chrisfan/Documents/Research/FleetPower/sandiego/sandiego.csv",
                     names = ["CarID", "VINnumber", "coordinates_longitude", "coordinates_latitude", "interiorStatus",
                              "exteriorStatus", "Address", "FuelState", "VehicleType", "CurrentlyCharging", "UnixTimestamp"])
poi_types = pd.read_csv("/Users/chrisfan/Documents/Research/FleetPower/sandiego/types.csv")

#distance btwn parking spot & nearest POI (second order )

sd_charging = sd_cars.query('CurrentlyCharging == 1')
#other proxy for parked?

#points with ratings
rated_points = points.query('rate != -1')

#points with prices
priced_points = points.query('price != -1')

#cars with location data
sd_cars_wloc = sd_cars.query('coordinates_latitude != 0.0')

#boundaries of POIs

lon_min = points['lon'].min()
lat_min = points['lat'].min()
lon_max = points['lon'].max()
lat_max = points['lat'].max()

#cars within boundaries of POIs
cars_sample = sd_cars.query('coordinates_latitude > @lat_min & \
    coordinates_longitude > @lon_min & \
    coordinates_latitude < @lat_max & \
    coordinates_longitude < @lon_max' \
)

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    http://stackoverflow.com/questions/15736995/
    how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km
    
#minimum distance btwn point of interest / charged cars

sclon = cars_sample['coordinates_longitude']
sclat = cars_sample['coordinates_latitude']
plon = points['lon']
plat = points['lat']

cars_sample['nearest'] = ""

for x, y in zip(sclon, sclat):
    i = haversine(sclon, sclat, plon[0], plat[0])
    for a, b in zip(plon, plat):
        i = haversine(sclon, sclat, plon, plat)
        if i < haversine(sclon, sclat, plon, plat):
            i = haversine(sclon, sclat, plon, plat)
        

#filter / weight by: price, rate, rank, and hexagon

#give each hexagon a weight based on rank, avg price?







