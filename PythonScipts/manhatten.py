import pandas as pd
import numpy as np

zipcode_df = pd.read_csv("manhattan_zipcodes.txt", sep="\t")
vehicle_df = pd.read_csv("ny_ev_registrations_public.csv")
sample_df = pd.read_csv("sample_train_withzip.csv")

print(type(zipcode_df["Zip Code"]))
zipcode_df["Zip Code"] = zipcode_df["Zip Code"].astype(int)
vehicle_df["Zip Code"] = vehicle_df["Zip Code"].astype(int)
sample_df["Zip Code"] = pd.to_numeric(sample_df["Zip Code"], errors='coerce')
sample_df = sample_df.dropna(subset=['Zip Code'])
sample_df["Zip Code"] = sample_df["Zip Code"].astype(int)

final_df1 = vehicle_df[vehicle_df["Zip Code"].isin(zipcode_df["Zip Code"])]
final_df2 = sample_df[sample_df["Zip Code"].isin(zipcode_df["Zip Code"])]
final_df1.to_csv("manhattan_evs.csv", index=False)
final_df2.to_csv("sample_train.csv", index=False)