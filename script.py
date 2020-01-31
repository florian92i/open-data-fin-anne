# coding=utf-8
import csv
import requests
import json
import pandas as pd
import os
import numpy as np

# $ pip install -r requirements.txt
urlOpenData = requests.get("https://www.data.gouv.fr/api/1/datasets/5448d3e0c751df01f85d0572/")


def jprint(obj):
    # create a formatted string of the Python JSON object open data
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def downloadCsv(urlOpenDataArg):
    jsonOpenDataWebSite = urlOpenDataArg.json()
    jprint(jsonOpenDataWebSite['resources'][0]['latest'])
    url = jsonOpenDataWebSite['resources'][0]['latest']  # get url for download CSV
    response = requests.get(url)
    with open(os.path.join("file.csv"), 'wb') as f:
        f.write(response.content)


# downloadCsv(urlOpenData) # active for PROD production only, no need for DEV production

df = pd.read_csv("file.csv", encoding='utf-8', sep=";", na_values=['_______'])
print(df.columns)
df.drop(['n_amenageur', 'source'], axis=1, inplace=True)  # drop column, inplace true for reasign the dataFrame for df
df.replace('', np.nan, inplace=True)
print(df)

# print(df.head(5))
# df.head(5).to_csv('out.csv', encoding='utf-8')
