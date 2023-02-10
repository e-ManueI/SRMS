## STEPS

### Clone from repository and Go to root directory of this project

````
pip install pipenv
pipenv shell
````

````
pipenv install -r .\requirements.txt
python manage.py makemigrations
python manage.py migrate

````

<p>username = admin </p>
<p>password = verification123</p>

### To change admin password, Go to terminal and run
````
py manage.py changepassword <username>
py manage.py changepassword admin
````

