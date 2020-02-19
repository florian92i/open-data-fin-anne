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
