# TEST SOPLAYA

## Avviare applicativo

Avviare il DB tramite docker

```shell
docker-compose up -d db_postgis_soplaya
```

Avviare la parte web/api tramite docker
```shell
docker-compose up -d soplaya_web
```

NB: Avviare prima il DB prima di avviare la parte web.

Quando verrà avviato il container web, verranno in automatico eseguiti i comandi:

```shell
python3 manage.py makemigrations
python3 manage.py migrate auth
python3 manage.py migrate
```

### Comando per importare un file csv

Per importare il file csv dei restaurant
```shell
python3 manage.py import_data_restaurant <path_file>
```

Esempio

```shell
python3 manage.py import_data_restaurant /code/data/dataset.csv 
```

NB: /code è il path interno del container docker 

### Test Automatici

```shell
python3 manage.py test
```

### Info Varie

Nella cartella collections è presente un file "basilare" postman per testare le 2 api

