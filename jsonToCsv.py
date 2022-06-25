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


'''
# Begin to optimise the category v1:
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
'''



# '''
# Begin to optimise the category v2:
new_cat = df["category"].tolist()

switcher ={
  "POLITICS":"POLITICS",
  "WELLNESS":"HEALTH & WELLNESS",
  "ENTERTAINMENT":"ENTERTAINMENT",
  # "TRAVEL":"TRAVEL",
  "TRAVEL":"NONE",
  "STYLE & BEAUTY" : "LIFE STYLE",
  "HEALTHY LIVING" : "LIFE STYLE",
  "PARENTING" : "WOMAN & CHILD",
  # "QUEER VOICES":"SOCIETY",
  "QUEER VOICES":"NONE",
  "FOOD & DRINK":"NONE",
  "BUSINESS":"BUSINESS",
  "COMEDY":"ENTERTAINMENT",
  "SPORTS":"SPORTS",
  # "BLACK VOICES":"SOCIETY",
  "BLACK VOICES":"NONE",
  # "HOME & LIVING":"LIFE STYLE",
  "HOME & LIVING":"NONE",
  # "PARENTS":"WOMAN & CHILD",
  "PARENTS":"NONE",
  "THE WORLDPOST":"NONE",
  # "WEDDINGS":"LIFE STYLE",
  "WEDDINGS":"NONE",
  "WOMEN":"WOMAN & CHILD",
  # "IMPACT":"OTHERS",
  "IMPACT":"NONE",
  # "DIVORCE":"LIFE STYLE",
  "DIVORCE":"NONE",
  # "CRIME":"SOCIETY",
  "CRIME":"NONE",
  # "MEDIA":"ENTERTAINMENT",
  "MEDIA":"NONE",
  # "WEIRD NEWS":"OTHERS",
  "WEIRD NEWS":"NONE",
  # "GREEN":"OTHERS",
  "GREEN":"NONE",
  # "WORLDPOST":"OTHERS",
  "WORLDPOST":"NONE",
  # "RELIGION":"POLITICS",
  "RELIGION":"NONE",
  "STYLE":"LIFE STYLE",
  # "WORLD NEWS":"SOCIETY",
  "WORLD NEWS":"NONE",
  # "TASTE":"LIFE STYLE",
  "TASTE":"NONE",
  "TECH":"SCIENCE & TECH",
  "MONEY":"BUSINESS",
  "ARTS":"ENTERTAINMENT",
  # "FIFTY":"HEALTH & WELLNESS",
  "FIFTY":"NONE",
  # "GOOD NEWS":"OTHERS",
  "GOOD NEWS":"NONE",
  "ARTS & CULTURE":"ENTERTAINMENT",
  # "ENVIRONMENT":"OTHERS",
  "ENVIRONMENT":"NONE",
  "COLLEGE":"EDUCATION",
  # "LATINO VOICES":"OTHERS",
  "LATINO VOICES":"NONE",
  "CULTURE & ARTS":"ENTERTAINMENT",
  "EDUCATION":"EDUCATION",
  "SCIENCE":"SCIENCE & TECH",


}


# '''


# '''
for x in range(len(new_cat)):
  new_cat[x] = switcher.get(new_cat[x], "UNKNOW_LOL")


df.pop("category")
df["category"] = new_cat
# '''


# Eliminate None:
df = df[df["category"].str.contains("NONE")==False]



# End of Category optimisation 


print("Total Numbers of Categories: ", df["category"].nunique(),"\n", df["category"].value_counts())



df.to_csv('simplified_data.csv', encoding='utf-8', index=False)
