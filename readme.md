configure settings.py example of the default configuartion.
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DemoProject',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # Use your database host
        'PORT': '3306',       # Default MySQL port
    }
}
```
Inject the sql data contained in project specs folder. undated test project dump(1).sql into the database
Then run this project

```manage.py runserver 8000```

