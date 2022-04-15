import urllib.request
import json
import pandas as pd
import numpy as np
from time import sleep
# Your Bing Maps Key 
bingMapsKey = "AmoNBcIYDcFMMMpME2kddQFUd3v2WWuas2C-zQPBKBDhXnUwYeUEksR1DEJhLKEY"

#routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + str(-73.97306061) + "," + str(40.74992371) + "&wp.1=" + str(-73.98472595) + "," + str(40.74789047) + "&key=" + bingMapsKey
#routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + str(40.74992371) + "," + str(-73.97306061) + "&wp.1=" + str(40.74789047) + "," + str(-73.98472595) + "&key=" + bingMapsKey
#request = urllib.request.Request(routeUrl)
#response = urllib.request.urlopen(request)
#jsonResponse = json.load(response)
#print(jsonResponse["resourceSets"][0]["resources"][0]["travelDistance"])


def calculate_distance(df, pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude):
    sleep(0.3)
    routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + str(df[pickup_latitude]) + "," + str(df[pickup_longitude]) + "&wp.1=" + str(df[dropoff_latitude]) + "," + str(df[dropoff_longitude]) + "&key=" + bingMapsKey

    try:
        request = urllib.request.Request(routeUrl)
        response = urllib.request.urlopen(request)
        jsonResponse = json.load(response)
        df["travelDistance"] = jsonResponse["resourceSets"][0]["resources"][0]["travelDistance"]
        df["travelDuration"] = jsonResponse["resourceSets"][0]["resources"][0]["travelDuration"] 
        df["travelDurationTraffic"] = jsonResponse["resourceSets"][0]["resources"][0]["travelDurationTraffic"]
    except:
        df["travelDistance"] = np.NaN
        df["travelDuration"] = np.NaN 
        df["travelDurationTraffic"] = np.NaN
    return df


vehicle_df = pd.read_csv("sample_train.csv")
vehicle_df = vehicle_df.apply(calculate_distance, axis=1, pickup_latitude='pickup_latitude', pickup_longitude='pickup_longitude', dropoff_latitude='dropoff_latitude', dropoff_longitude='dropoff_longitude')
vehicle_df.to_csv("sample_train.csv", index=False)

