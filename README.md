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

