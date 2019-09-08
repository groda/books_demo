## API

 - API root: https://damp-earth-36259.herokuapp.com/api/
 - get all books https://damp-earth-36259.herokuapp.com/api/books/
 - vocabulary for book with ID 1: https://damp-earth-36259.herokuapp.com/api/words/?book=1
 - delete book with ID 3 `curl -X DELETE https://damp-earth-36259.herokuapp.com/api/books/3/`
 

## 

## Commit changes to Heroku

    git add .
    git commit -m 'new'
    git push heroku master

## Migrate local

    python manage.py makemigrations
    python manage.py migrate

## Migrate on Heroku

    heroku run python manage.py makemigrations
    heroku run python manage.py migrate

## Run local

    heroku local web

## Run on Heroku

    heroku open

## Create superuser

    python manage.py createsuperuser
    heroku run python manage.py createsuperuser

## Add migrations

    git add booksdemo/migrations/*.py'
    
## Reset Postgres DB on Heroku

    heroku pg:reset
