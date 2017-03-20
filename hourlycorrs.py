import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt

#predict rentals per day for each cell
#use hour as a filter, or use fixed effects for hour
#use other variables to predict rentals per hour. 

rentals = pd.read_csv("/Users/chrisfan/Downloads/RentalTransactions2014MayJune.csv", sep = ";")

hourly = pd.read_csv("/Users/chrisfan/Downloads/hourlyTransactions.csv", sep = ";")
#number of rentals in the cell, by hour 

hour10 = hourly[hourly['hour'] == 10]
hour10cell44 = hour10[hour10['cell'] == 44]
hour10means = hour10.groupby('cell').mean()

hour10meanRentals = hour10means['rentalsPerDay'].values
hour10meanRatings = hour10means['meanRating'].values
hour10meanTemp = hour10means['Mean.TemperatureC'].values
hour10numPOIs = hour10means['numberOfPOIs'].values
hour10meanPrice = hour10means['meanPrice'].values
hour10numLawyers = hour10means['lawyer'].values
hour10numFood = hour10means['food'].values
hour10numBowlingAlleys = hour10means['bowling_alley'].values
hour10numWorship = hour10means['place_of_worship'].values
hour10numBars = hour10means['bar'].values
hour10numTrainStations = hour10means['train_station'].values
hour10numGyms = hour10means['gym'].values
hour10numParks = hour10means['park'].values
hour10numMuseums = hour10means['museum'].values
hour10numDoctors = hour10means['doctor'].values
hour10numHealth = hour10means['health'].values
hour10numStores = hour10means['store'].values
hour10numHospitals = hour10means['hospital'].values
hour10numLodging = hour10means['lodging'].values
hour10numAccounting = hour10means['accounting'].values
hour10numUniversities = hour10means['university'].values
hour10numSchools = hour10means['school'].values
hour10numNightClubs = hour10means['night_club'].values
hour10numGasStations = hour10means['gas_station'].values
hour10numJewelry = hour10means['jewelry_store'].values
hour10numClothingStore = hour10means['clothing_store'].values
hour10numShoeStore = hour10means['shoe_store'].values

#cell 46 only had data point. The rest were usually 40-60, few in the 20s
#this will affect averages.
plt.scatter(hour10meanRatings, hour10meanRentals)
plt.scatter(hour10meanTemp, hour10meanRentals)
plt.scatter(hour10meanPrice, hour10meanRentals)
#essentially no correlation

plt.scatter(hour10numPOIs, hour10meanRentals)
#correlated
plt.scatter(hour10numLawyers, hour10meanRentals)
#linear
plt.scatter(hour10numFood, hour10meanRentals)
#VERY LINEAR!
plt.scatter(hour10numBowlingAlleys, hour10meanRentals)
#Most cells have no bowling alleys!
plt.scatter(hour10numWorship, hour10meanRentals)
#nonlinear 
plt.scatter(hour10numBars, hour10meanRentals)
#linear
plt.scatter(hour10numTrainStations, hour10meanRentals)
#Most cells have no train stations!
plt.scatter(hour10numGyms, hour10meanRentals)
#linear but not perfectly correlated

#are people more likely to park when ratings are higher?
#hard because no constant to compare to - I don't have a place with 500 lawyers
#of mean rating 3 and 500 lawyers of mean rating 4

#RentalProbability = num rentals / num available cars?

#more plots 2/28/17
plt.scatter(hour10numParks, hour10meanRentals)
#kind of correlated
plt.scatter(hour10numMuseums , hour10meanRentals)
#slightly correlated
plt.scatter(hour10numDoctors , hour10meanRentals)
#slightly correlated
plt.scatter(hour10numHealth , hour10meanRentals)
#slightly correlated
plt.scatter(hour10numStores , hour10meanRentals)
#correlated
plt.scatter(hour10numHospitals , hour10meanRentals)
#slightly correlated
plt.scatter(hour10numLodging , hour10meanRentals)
#very correlated
plt.scatter(hour10numAccounting , hour10meanRentals)
#correlated
plt.scatter(hour10numUniversities , hour10meanRentals)
#somewhat correlated
plt.scatter(hour10numSchools , hour10meanRentals)
#correlated
plt.scatter(hour10numNightClubs , hour10meanRentals)
#correlated
plt.scatter(hour10numGasStations , hour10meanRentals)
#not correlated
plt.scatter(hour10numJewelry , hour10meanRentals)
#correlated
plt.scatter(hour10numShoeStore, hour10meanRentals)
#somewhat correlated
plt.scatter(hour10numClothingStore, hour10meanRentals)
#correlated

#Ratios

LawyerRatio = hour10numLawyers / hour10numPOIs
FoodRatio = hour10numFood / hour10numPOIs
WorshipRatio = hour10numWorship / hour10numPOIs
BarRatio = hour10numBars / hour10numPOIs
GymRatio = hour10numGyms / hour10numPOIs
ParkRatio = hour10numParks / hour10numPOIs
MuseumRatio = hour10numMuseums / hour10numPOIs
DoctorRatio = hour10numDoctors / hour10numPOIs
HealthRatio = hour10numHealth / hour10numPOIs
StoreRatio = hour10numStores / hour10numPOIs
HospitalRatio = hour10numHospitals / hour10numPOIs
LodgingRatio = hour10numLodging / hour10numPOIs
AccountingRatio = hour10numAccounting / hour10numPOIs
UniversityRatio = hour10numUniversities / hour10numPOIs
SchoolRatio = hour10numSchools / hour10numPOIs
NightClubRatio = hour10numNightClubs / hour10numPOIs
GasStationRatio = hour10numGasStations / hour10numPOIs
JewelryRatio = hour10numJewelry / hour10numPOIs
ShoeStoreRatio = hour10numShoeStore / hour10numPOIs
ClothingStoreRatio = hour10numClothingStore / hour10numPOIs

plt.scatter(LawyerRatio, hour10meanRentals)
#correlated
plt.scatter(FoodRatio, hour10meanRentals)
#not correlated
plt.scatter(WorshipRatio, hour10meanRentals)
#close to negatively correlated
plt.scatter(BarRatio, hour10meanRentals)
#correlated
plt.scatter(GymRatio, hour10meanRentals)
#slightly correlated
plt.scatter(ParkRatio, hour10meanRentals)
#not correlated
plt.scatter(MuseumRatio, hour10meanRentals)
#not correlated
plt.scatter(DoctorRatio, hour10meanRentals)
#not correlated
plt.scatter(HealthRatio, hour10meanRentals)
#not correlated
plt.scatter(StoreRatio, hour10meanRentals)
#not correlated
plt.scatter(HospitalRatio, hour10meanRentals)
#not correlated
plt.scatter(LodgingRatio, hour10meanRentals)
#somehwat correlated
plt.scatter(AccountingRatio, hour10meanRentals)
#not correlated
plt.scatter(UniversityRatio, hour10meanRentals)
#not correlated
plt.scatter(SchoolRatio, hour10meanRentals)
#not correlated
plt.scatter(NightClubRatio, hour10meanRentals)
#somewhat correlated
plt.scatter(GasStationRatio, hour10meanRentals)
#not correlated
plt.scatter(JewelryRatio, hour10meanRentals)
#somewhat correlated
plt.scatter(ClothingStoreRatio, hour10meanRentals)
#correlated
plt.scatter(ShoeStoreRatio, hour10meanRentals)
#not as correlated

#correlated