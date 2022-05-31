import json 
import csv 
import pandas as pd


with open('data.json',encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile,lines=True)



df.pop("authors")
df.pop("link")
df.pop("date")

#Uncomment for simplified version
df["headline"] = df["headline"] + ". " + df["short_description"]
df["description"] = df["headline"]

df.pop("short_description")
df.pop("description")



# Begin to optimise the category:
new_cat = df["category"].tolist()

switcher ={
  "POLITICS":"POLITICS",
  "WELLNESS":"HEALTH & WELLNESS",
  "ENTERTAINMENT":"ENTERTAINMENT",
  "TRAVEL":"TRAVEL",
  "STYLE & BEAUTY" : "LIFE STYLE",
  "HEALTHY LIVING" : "LIFE STYLE",
  "PARENTING" : "WOMAN & CHILD",
  "QUEER VOICES":"SOCIETY",
  "FOOD & DRINK":"HEALTH & WELLNESS",
  "BUSINESS":"BUSINESS",
  "COMEDY":"ENTERTAINMENT",
  "SPORTS":"SPORTS",
  "BLACK VOICES":"SOCIETY",
  "HOME & LIVING":"LIFE STYLE",
  "PARENTS":"WOMAN & CHILD",
  "THE WORLDPOST":"OTHERS",
  "WEDDINGS":"LIFE STYLE",
  "WOMEN":"WOMAN & CHILD",
  "IMPACT":"OTHERS",
  "DIVORCE":"LIFE STYLE",
  "CRIME":"SOCIETY",
  "MEDIA":"ENTERTAINMENT",
  "WEIRD NEWS":"OTHERS",
  "GREEN":"OTHERS",
  "WORLDPOST":"OTHERS",
  "RELIGION":"POLITICS",
  "STYLE":"LIFE STYLE",
  "WORLD NEWS":"SOCIETY",
  "TASTE":"LIFE STYLE",
  "TECH":"SCIENCE & TECH",
  "MONEY":"BUSINESS",
  "ARTS":"ENTERTAINMENT",
  "FIFTY":"HEALTH & WELLNESS",
  "GOOD NEWS":"OTHERS",
  "ARTS & CULTURE":"ENTERTAINMENT",
  "ENVIRONMENT":"OTHERS",
  "COLLEGE":"EDUCATION",
  "LATINO VOICES":"OTHERS",
  "CULTURE & ARTS":"ENTERTAINMENT",
  "EDUCATION":"EDUCATION",
  "SCIENCE":"SCIENCE & TECH",


}

for x in range(len(new_cat)):
  new_cat[x] = switcher.get(new_cat[x], "UNKNOW_LOL")

df.pop("category")
df["category"] = new_cat


# End of Category optimisation 

print("Total Numbers of Categories: ", df["category"].nunique(), df["category"].value_counts())



df.to_csv('simplified_data.csv', encoding='utf-8', index=False)
