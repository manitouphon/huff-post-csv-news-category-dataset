import json 
import csv 
import pandas as pd


with open('data.json',encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile,lines=True)

#Uncomment for simplified version

# df.pop("authors")
# df.pop("link")
# df.pop("date")
# df["headline"] = df["headline"] + ". " + df["short_description"]
# df.pop("short_description")

df.to_csv('data.csv', encoding='utf-8', index=False)