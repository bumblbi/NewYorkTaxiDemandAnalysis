#import pandas
#import random

#filename = "train.csv"
#n = sum(1 for line in open(filename)) - 1 #number of records in file (excludes header)
#s = 10000 #desired sample size
#skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
#df = pandas.read_csv(filename, skiprows=skip)
#df.to_csv("sample_train.csv", index=False)

from asyncio.windows_events import NULL
import geopy
import pandas as pd
import numpy as np


def get_zipcode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]),timeout=200)
    try:
        df["zip code"] = location.raw['address']['postcode']

    except:
        df["zip code"] = np.NaN
    
    return df


geolocator = geopy.Nominatim(user_agent='https')

df = pd.read_csv("temp/trips_manhattan.csv")
df["zipcode"] = df.apply(get_zipcode, axis=1, geolocator=geolocator, lat_field='pickup_latitude', lon_field='pickup_longitude')
print(df.head())
df.to_csv("temp/manhattan_withzip.csv", index=False)