## Build and Develop this project

### code structure
> The whole file structure can be found in the file_tree.txt <br>
> All format is like: file --> content 

```
│  file_tree.txt                    --> the file tree of this project
│  manage.py                        --> the django manage python file
│  readme.md                        --> the document of the project
│  requirements.txt                 --> pip install it
├─game_2048
│  │  admin.py                      --> django 
│  │  models.py                     --> django model, orm to sql
│  │  tests.py                      --> test file
│  │  views.py                      --> views
│  │  __init__.py
│  │  
│  ├─migrations                     --> sql generate by use the django
│  │  │  0001_initial.py
│  │  │  __init__.py
│  ├─static
│  │      2048.css                  --> 2048 css files
│  │      jquery.min.js             --> external jQuery 
│  │      main2048.js               --> 2048 js
│  │      showanimation2048.js      --> main loginc files
│  │      support2048.js            --> other js
│  ├─templates
│  │  └─game_2048
│  │          login.html            --> login view html
│  │          project3.html         --> play games files
└─Project3
    │  settings.py                  --> django setting files
    │  urls.py                      --> defines the url 
    │  wsgi.py
    │  __init__.py

            
```

### build and run this project

#### step1: build the localhost env
```
required environment:
python3, mysql


```

#### step2: set the config of mysql

```
Change the mysql setting in the 
└─Project3
    │  settings.py    

```


#### step3: generate the mysql or init the mysql:
```
use the two command to generate the mysql tables:
python manage.py makemigrations
python manage.py migrate

or 
import the existed sql script in the root dir: project3.sql
```

#### step4: create the test user

```
insert the test user in the mysql table: user

or
use this command that the django provide

python manage.py createsuperuser
input the super user's name and email, password

then open:
http://127.0.0.1:8000/admin/login/?next=/admin/
create some test user
in the existed sql, there is an user provided: test1+1234(user+password)

```

#### step5: run the project and open in the browser
```
python manage.py runserver 0.0.0.0:8000

then, open localhost:8000/login,

```

#### finally: enjoy this 2048 game

### Develop process

#### The game can read the highest score from the server via json request:
```
curl --request POST \
  --url http://localhost:8000/update_score/ \
  --header 'content-type: application/json' \
  --cookie JSESSIONID=BDC8E68EED46AB9BA9B5F05329AA1E05 \
  --data '{
	"username":"test1",
	"score":99
}'
```

> we can find the logic in the update_score in the views.py

#### The app use the database of mysql:
```
we can find the relation of tables in the model.py
```

#### The app must have a user system (including creation, login and logout)

```
game_2048.views.login is the login logic, 
and the logout logic is game_2048.views.logout.

```





