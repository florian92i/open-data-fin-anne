# coding=utf-8
import csv
import json
import numpy as np
import os
import pandas as pd
import requests

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


nameColumnReplace = {
  'n_operateur': {
    'delColumn': [
      {'isRegex': True, 'deleteIfMatchWith': 'F.*'},
      {'isRegex': False, 'deleteIfMatchWith': 'AIRESERVICES'},
      {'isRegex': False, 'deleteIfMatchWith': 'BOUYGUES ENERGIES ET SERVICES'},
      {'isRegex': False, 'deleteIfMatchWith': 'SIEL42'}
    ],
    'regexReplace': [
      {'valueMatch': '‚', 'replacerValueBy': 'a'},
      {'valueMatch': 'test', 'replacerValueBy': ''}
    ]
  },
  # fin exemple
  # ---------------------------------
  'n_enseigne': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'id_station': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'n_station': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'ad_station': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'code_insee': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'Xlongitude': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'Ylatitude': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'nbre_pdc': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'id_pdc': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'puiss_max': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'type_prise': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'acces_recharge': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'accessibilité': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'},
  'observations': {'delColumn': 'er', 'valueMatch': 'true', 'replacerValueBy': 'toto'}
}


# effet de bord de batard car il influe sur la variable df en dehors de son scop de function de base
def replaceDataRegex(data, regexReplace):
  for i in range(len(regexReplace)):
    data['n_operateur'].replace(regexReplace[i]['valueMatch'], regexReplace[i]['replacerValueBy'], regex=True,
                                inplace=True)  # exemple de regex


def dropDataWithCondition(data, conditionsDeleteLine):
  for i in range(len(conditionsDeleteLine)):
    filter = data['n_operateur'].str.contains(conditionsDeleteLine[i]['deleteIfMatchWith'],
                                              regex=conditionsDeleteLine[i]['isRegex'])
    data = data[~filter]
  return data


def printUniqValue(dfNameColumn):
  print(dfNameColumn.unique())


df = pd.read_csv("file.csv", encoding='utf-8', sep=";", na_values=['_______'])
df.drop(['n_amenageur', 'source', 'date_maj'], axis=1,
        inplace=True)  # drop column, inplace true for reasign the dataFrame for df
df.replace('', np.nan, inplace=True)
df.replace("\t", " ", regex=True)  ## remplace la tabulation

# df = df[df.n_operateur != 'BOUYGUES ENERGIES ET SERVICES']
replaceDataRegex(df, nameColumnReplace['n_operateur']['regexReplace'])
df = dropDataWithCondition(df, nameColumnReplace['n_operateur']['delColumn'])
print(df)
printUniqValue(df.n_operateur)

# dropDataWithCondition()
##df.to_csv('out.csv', encoding='utf-8')
