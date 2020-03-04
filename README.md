git

    git add . 
    git pull origin master
    git commit -m "some commit"
    git push origin master
    git rm -r --cached .
    
My Config

create file my.cnf in the project and edit this file
    
    [client]
    database = mydatabase
    user = your_username
    password = password
    default-character-set = utf8

Django

    pip3 freeze > requirements.txt.
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python manage.py migrate

Database
    create database aution character set utf8 collate utf8_unicode_ci;

Run the collectstatic management command:

    python manage.py collectstatic

Go through each of your projects apps migration folder and remove everything inside, except the __init__.py file.

    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete


статичный локализация

    django-admin compilemessages
    django-admin.py makemessages -a

project update

        cd /docker/letsencrypt-docker-nginx/src/booking_prod/backend/booking/
        git pull origin master
        docker-compose up --build -d booking
        
python commands

        docker-compose exec booking python manage.py makemigrations
        docker-compose exec booking python manage.py migrate
