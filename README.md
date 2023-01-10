# todo-rest-api
Multiuser Todo app API, made with Django REST framework.

**************
How to install?
**************

* if you want to deploy this project to some hosting - follow exact hosting instructions how to set this prepared to work

- install python (3.9.10 or higher)

1) HOW TO: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

- install pip (pip 22.3.1 or higher)
- create project directory and come into it
- create the virtual environment and activate it   !(venv) in the beginning of the command string will appear
- install the requirements

2) HOW TO: https://docs.djangoproject.com/en/4.1/intro/tutorial01/

Execute the following commands (without "- " in the beginning):
- django-admin startproject todo
- python manage.py startapp todoapp

3) Create an empty PostgreSQL DataBase, that will be bounded to the app


Good, from now you got your project's skeleton with all the preinstalled modules is ready!
You can run the server to be sure everything is all right. And check the venv directory out whether all the modules are locked and loaded.


4) Follow the structure of the repository doing this!
- Copy all the files from this Git-repository to your project, overwriting existing ones if needed

5) HOW TO: https://docs.djangoproject.com/en/4.1/topics/migrations/

Execute the following commands (without "- " in the beginning):
- python manage.py makemigrations
- python manage.py migrate

6) Copy todoapp_status.csv to your database overwriting the existing one

7) Let's configure todo/settings.py, I recommend to take a look on it, there are many descriptions there.

Come on edit it from up to down:
- change DEBUG to False
- add two items to INSTALLED APPS:
    'rest_framework',
    'todoapp.apps.TodoappConfig',
- change DATABASES with following:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '**name**',
        'USER': '**user**',
        'PASSWORD': '**user**',
        'HOST': '**host**',  # if local - 127.0.0.1
        'PORT': '**port**',  # 5432 is default
    }
}
- you can change TIMEZONE, for example TIME_ZONE = 'Europe/Helsinki'
- add this setting for Django REST:
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]

}
- add the JWT-token parameters: (Description is here https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

8) Run your server with the command: (full description is here https://docs.djangoproject.com/en/4.1/ref/django-admin/)
- django-admin runserver  (by default it runs 127.0.0.1:8000)


**************
How to use API?
**************

! All the requests must be to htpps://(hosting_name)/api/v1/
! Passwords have the validation function (they cannot be simple)

1) signup/
- POST request is allowed with a json dict with "email", "password", "password2" inside. It creates a user and returns e-mail if succeed.

2) signin/
- POST request is allowed with a json dict with "username", "password". It returns JWT-tokens if succeed.

3) signin/refresh/
- POST request is allowed with a json dict with "refresh":"(refresh-token)". It returns a new access-token if succeed.

4) signin/verify/
- POST request is allowed with a json dict with "refresh":"(any-token)". It checks a given token and returns {} if succeed.

5) todos/ and todos/?status=[status_pk] , where [status_pk] is 1,2 or 3
- GET request is allowed with Authorization formatted as 'Bearer (access-token)'. Returns a dict of user's items. Has an option to filter items by status.

6) todos/
- POST request is allowed with Authorization formatted as 'Bearer (access-token)' and a json dict with "title", "content":"", "status":integer.
Content is empty by default, status is 1 by default and can be 1,2 or 3. Title is required. It creates the item and return it.

7) todos/[id] where [id] is a unique number of item.
- PUT request is allowed with Authorization formatted as 'Bearer (access-token)' and a json dict with "title", "content":"", "status":integer.
Content is empty by default, status is 1 by default and can be 1,2 or 3. Title is required. It makes changes to the given item.

8) todos/[id] where [id] is a unique number of item.
- DELETE request is allowed with Authorization formatted as 'Bearer (access-token)'. It deletes the given item, completely.

9) todos/[id] where [id] is a unique number of item.
- GET request is allowed with Authorization formatted as 'Bearer (access-token)'. It shows the given item as a dict.

10) changePassword/
- POST request is allowed with Authorization formatted as 'Bearer (access-token)' and a json dict with "old_password", "new_password", "new_password2".
 It changes the user's password.


Hope you enjoy using this
https://github.com/slava-zagriichuk/todo-rest-api/
