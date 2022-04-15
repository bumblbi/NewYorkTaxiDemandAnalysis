import pandas as pd
import numpy as np
import geopy.distance


def calculate_distance(df, pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude):
    dist_dec = round(geopy.distance.distance((df[pickup_latitude],df[pickup_longitude]), (df[dropoff_latitude],df[dropoff_longitude])).km,2)
    return dist_dec

num = 2.75
print(round(num,2))
vehicle_df = pd.read_csv("sample_train.csv")
vehicle_df['distance'] = vehicle_df.apply(calculate_distance, axis=1, pickup_latitude='pickup_latitude', pickup_longitude='pickup_longitude', dropoff_latitude='dropoff_latitude', dropoff_longitude='dropoff_longitude')
vehicle_df.to_csv("sample_train.csv", index=False)

