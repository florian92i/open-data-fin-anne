# Yo la team

## Setup

Run `docker-compose up --build` si jamais vous avez modifier vos dependances ou le .dockerfile

Run `docker-compose up` 


## Data base
pour la db l'url: 

```sh
psql postgres://user:pass@localhost:35432/db
```

## Les script Python

file `script.py`

### Comment modifer les règles du fichier pour le remplacement de charactère?

C'est tres simple il faut changer le dictionnaire --> nameColumnReplace

```python
'regexReplace': [
    {'valueMatch': '‚', 'replacerValueBy': 'a'}, # la valeur ','  va être remplace par 'a'
    {'valueMatch': 'S', 'replacerValueBy': ''} # la valeur 'S' va être remplace par ''
]
```

> Rajouter un -->      {'valueMatch': '', 'replacerValueBy': ''}, pour chaque nouvelle règles

### Comment modifer les règles du fichier pour supprimer une ligne ? (WIP) venir me voir pour que je le fasse

```python
    'delColumn': [
      {'isRegex': True, 'deleteIfMatchWith': 'F.*'}, # Tout les mots qui contienne un F sont supprimer (regex)
      {'isRegex': False, 'deleteIfMatchWith': 'AIRESERVICES'}, # Mot qui contient 'AIRESERVICES' supprimé
      {'isRegex': False, 'deleteIfMatchWith': 'BOUYGUES ENERGIES ET SERVICES'}, 
      {'isRegex': False, 'deleteIfMatchWith': 'SIEL42'}
    ],
```

> Rajouter un élément dans le tableau pour rajouter des conditions de drop, les deux conditions ne se cumule pas ils seront traité séparement

### Structure global pour un champ

```python
  'n_operateur': { ## nom champ csv
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
```

> Au dessus l'exemple pour l'objet n_operateur

## Cmd postgres

https://www.datacamp.com/community/tutorials/10-command-line-utilities-postgresql



## Memo sql
psql -U postgres
\l
\c madatabase
CREATE TABLE films ();
\dt 
ALTER TABLE opendata ADD COLUMN phone VARCHAR;
COPY opendata FROM '/app/out.csv' DELIMITER ';' CSV HEADER;

## API les routes

Prefix par : /api-open-data/

/localisation/ --> Return les points latitude, longitude, id_station pour l'afficher dans la carte 
/localisation/{id_station} --> Return toutes les infos + calculer prixKwh
/localisation/?typeconnecteur=''&nbrborne=''&fournisseurBorne=''&prixKwh=''&typedeprise=''&accesrecharge=''

Dans le front avec l'api de google map : 
filtrer par périmètre + afficher le nombre de marqueur
Ne pas oublier d'afficher les selects en rapport avec les colonnes dans le csv
