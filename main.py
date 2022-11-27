import pandas as pd
import csv

df = pd.read_csv("finals.csv")

del df["Luminosity"]
del df["temp_planet_date"]
del df["temp_planet_mass"]



df.to_csv('finals.csv') 