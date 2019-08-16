# Commit changes to Heroku
git add .
git commit -m 'new''
git push heroku master'

# Migrate local
python manage.py makemigrations
python manage.py migrate

# Migrate on Heroku
heroku run python manage.py makemigrations
heroku run python manage.py migrate

# Run local
heroku local web

# Run on Heroku
heroku open

# Create superuser
python manage.py createsuperuser
heroku run python manage.py createsuperuser

# Add migrations
git add booksdemo/migrations/*.py'
