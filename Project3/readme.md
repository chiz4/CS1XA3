#  init my project:


# then, generate the table in mysql
## change your password in settings.py

python manage.py makemigrations
 
python manage.py migrate

python manage.py createsuperuser

http://127.0.0.1:8000/admin/login/?next=/admin/







