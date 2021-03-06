import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
%matplotlib inline

hourly = pd.read_csv("/Users/chrisfan/Downloads/hourlyTransactions.csv", sep = ";")
hour10 = hourly[hourly['hour'] == 10]
hour10_ratings = hour10[['meanRating.establishment',
 'meanRating.park',
 'meanRating.point_of_interest',
 'meanRating.general_contractor',
 'meanRating.lawyer',
 'meanRating.museum',
 'meanRating.doctor',
 'meanRating.health',
 'meanRating.real_estate_agency',
 'meanRating.electrician',
 'meanRating.home_goods_store',
 'meanRating.store',
 'meanRating.hospital',
 'meanRating.campground',
 'meanRating.lodging',
 'meanRating.food',
 'meanRating.finance',
 'meanRating.beauty_salon',
 'meanRating.bar',
 'meanRating.clothing_store',
 'meanRating.accounting',
 'meanRating.dentist',
 'meanRating.hair_care',
 'meanRating.spa',
 'meanRating.insurance_agency',
 'meanRating.cafe',
 'meanRating.restaurant',
 'meanRating.bus_station',
 'meanRating.transit_station',
 'meanRating.art_gallery',
 'meanRating.gym',
 'meanRating.physiotherapist',
 'meanRating.university',
 'meanRating.travel_agency',
 'meanRating.furniture_store',
 'meanRating.convenience_store',
 'meanRating.atm',
 'meanRating.movie_rental',
 'meanRating.storage',
 'meanRating.school',
 'meanRating.church',
 'meanRating.place_of_worship',
 'meanRating.funeral_home',
 'meanRating.shoe_store',
 'meanRating.local_government_office',
 'meanRating.book_store',
 'meanRating.night_club',
 'meanRating.zoo',
 'meanRating.meal_takeaway',
 'meanRating.laundry',
 'meanRating.florist',
 'meanRating.plumber',
 'meanRating.veterinary_care',
 'meanRating.locksmith',
 'meanRating.bank',
 'meanRating.moving_company',
 'meanRating.police',
 'meanRating.painter',
 'meanRating.car_repair',
 'meanRating.roofing_contractor',
 'meanRating.gas_station',
 'meanRating.pharmacy',
 'meanRating.bakery',
 'meanRating.jewelry_store',
 'meanRating.car_dealer',
 'meanRating.meal_delivery',
 'meanRating.parking',
 'meanRating.hardware_store',
 'meanRating.fire_station',
 'meanRating.grocery_or_supermarket',
 'meanRating.premise',
 'meanRating.liquor_store',
 'meanRating.electronics_store',
 'meanRating.shopping_mall',
 'meanRating.pet_store',
 'meanRating.library',
 'meanRating.rv_park',
 'meanRating.synagogue',
 'meanRating.post_office',
 'meanRating.department_store',
 'meanRating.natural_feature',
 'meanRating.courthouse',
 'meanRating.movie_theater',
 'meanRating.bicycle_store',
 'meanRating.stadium',
 'meanRating.car_wash',
 'meanRating.car_rental',
 'meanRating.political',
 'meanRating.light_rail_station',
 'meanRating.airport',
 'meanRating.cemetery',
 'meanRating.city_hall',
 'meanRating.embassy',
 'meanRating.hindu_temple',
 'meanRating.amusement_park',
 'meanRating.subpremise',
 'meanRating.bowling_alley',
 'meanRating.train_station',
 'meanRating.mosque']]
hour10_prices = hour10[['meanPrice.establishment',
 'meanPrice.park',
 'meanPrice.point_of_interest',
 'meanPrice.general_contractor',
 'meanPrice.lawyer',
 'meanPrice.museum',
 'meanPrice.doctor',
 'meanPrice.health',
 'meanPrice.real_estate_agency',
 'meanPrice.electrician',
 'meanPrice.home_goods_store',
 'meanPrice.store',
 'meanPrice.hospital',
 'meanPrice.campground',
 'meanPrice.lodging',
 'meanPrice.food',
 'meanPrice.finance',
 'meanPrice.beauty_salon',
 'meanPrice.bar',
 'meanPrice.clothing_store',
 'meanPrice.accounting',
 'meanPrice.dentist',
 'meanPrice.hair_care',
 'meanPrice.spa',
 'meanPrice.insurance_agency',
 'meanPrice.cafe',
 'meanPrice.restaurant',
 'meanPrice.bus_station',
 'meanPrice.transit_station',
 'meanPrice.art_gallery',
 'meanPrice.gym',
 'meanPrice.physiotherapist',
 'meanPrice.university',
 'meanPrice.travel_agency',
 'meanPrice.furniture_store',
 'meanPrice.convenience_store',
 'meanPrice.atm',
 'meanPrice.movie_rental',
 'meanPrice.storage',
 'meanPrice.school',
 'meanPrice.church',
 'meanPrice.place_of_worship',
 'meanPrice.funeral_home',
 'meanPrice.shoe_store',
 'meanPrice.local_government_office',
 'meanPrice.book_store',
 'meanPrice.night_club',
 'meanPrice.zoo',
 'meanPrice.meal_takeaway',
 'meanPrice.laundry',
 'meanPrice.florist',
 'meanPrice.plumber',
 'meanPrice.veterinary_care',
 'meanPrice.locksmith',
 'meanPrice.bank',
 'meanPrice.moving_company',
 'meanPrice.police',
 'meanPrice.painter',
 'meanPrice.car_repair',
 'meanPrice.roofing_contractor',
 'meanPrice.gas_station',
 'meanPrice.pharmacy',
 'meanPrice.bakery',
 'meanPrice.jewelry_store',
 'meanPrice.car_dealer',
 'meanPrice.meal_delivery',
 'meanPrice.parking',
 'meanPrice.hardware_store',
 'meanPrice.fire_station',
 'meanPrice.grocery_or_supermarket',
 'meanPrice.premise',
 'meanPrice.liquor_store',
 'meanPrice.electronics_store',
 'meanPrice.shopping_mall',
 'meanPrice.pet_store',
 'meanPrice.library',
 'meanPrice.rv_park',
 'meanPrice.synagogue',
 'meanPrice.post_office',
 'meanPrice.department_store',
 'meanPrice.natural_feature',
 'meanPrice.courthouse',
 'meanPrice.movie_theater',
 'meanPrice.bicycle_store',
 'meanPrice.stadium',
 'meanPrice.car_wash',
 'meanPrice.car_rental',
 'meanPrice.political',
 'meanPrice.light_rail_station',
 'meanPrice.airport',
 'meanPrice.cemetery',
 'meanPrice.city_hall',
 'meanPrice.embassy',
 'meanPrice.hindu_temple',
 'meanPrice.amusement_park',
 'meanPrice.subpremise',
 'meanPrice.bowling_alley',
 'meanPrice.train_station',
 'meanPrice.mosque']]
hour10_numbers = hour10[['establishment',
 'park',
 'point_of_interest',
 'general_contractor',
 'lawyer',
 'museum',
 'doctor',
 'health',
 'real_estate_agency',
 'electrician',
 'home_goods_store',
 'store',
 'hospital',
 'campground',
 'lodging',
 'food',
 'finance',
 'beauty_salon',
 'bar',
 'clothing_store',
 'accounting',
 'dentist',
 'hair_care',
 'spa',
 'insurance_agency',
 'cafe',
 'restaurant',
 'bus_station',
 'transit_station',
 'art_gallery',
 'gym',
 'physiotherapist',
 'university',
 'travel_agency',
 'furniture_store',
 'convenience_store',
 'atm',
 'movie_rental',
 'storage',
 'school',
 'church',
 'place_of_worship',
 'funeral_home',
 'shoe_store',
 'local_government_office',
 'book_store',
 'night_club',
 'zoo',
 'meal_takeaway',
 'laundry',
 'florist',
 'plumber',
 'veterinary_care',
 'locksmith',
 'bank',
 'moving_company',
 'police',
 'painter',
 'car_repair',
 'roofing_contractor',
 'gas_station',
 'pharmacy',
 'bakery',
 'jewelry_store',
 'car_dealer',
 'meal_delivery',
 'parking',
 'hardware_store',
 'fire_station',
 'grocery_or_supermarket',
 'premise',
 'liquor_store',
 'electronics_store',
 'shopping_mall',
 'pet_store',
 'library',
 'rv_park',
 'synagogue',
 'post_office',
 'department_store',
 'natural_feature',
 'courthouse',
 'movie_theater',
 'bicycle_store',
 'stadium',
 'car_wash',
 'car_rental',
 'political',
 'light_rail_station',
 'airport',
 'cemetery',
 'city_hall',
 'embassy',
 'hindu_temple',
 'amusement_park',
 'subpremise',
 'bowling_alley',
 'train_station',
 'mosque']]
 
num_data = hour10_numbers.values
price_data = hour10_prices.values
rating_data = hour10_ratings.values

num_pca = PCA(n_components = 99)
num_pca.fit(num_data)
num_var = num_pca.explained_variance_ratio_
num_var=np.cumsum(np.round(num_pca.explained_variance_ratio_, decimals=4)*100)
print num_var
plt.plot(num_var)

#how to deal with changing means and their weights?
num_pca = PCA(n_components = 99)
num_pca.fit(num_data)
num_var = num_pca.explained_variance_ratio_
num_var=np.cumsum(np.round(num_pca.explained_variance_ratio_, decimals=4)*100)
print num_var
plt.plot(num_var)