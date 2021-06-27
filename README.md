# Request Logger Middleware

- Middleware using Django, which will log error messages and error status codes to DB

- Add this to settings.py

 In Middleware
```
'request_logger.middleware.LoggingMiddleware'
```

```
DATABASE_ROUTERS = ['request_logger.dbRouter.LogRouter']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'handlers':{
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    	'log_db':{
            'level': 'DEBUG',
            'class': 'request_logger.dbHandler.DBHandler',
            'model': 'request_logger.models.SpecialLog',
            'expiry': 86400,
            }
    },
    'loggers': {
        'django.request': {
            'handlers': ['log_db'],
            'propagate': True,
        }
    }
}
    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR/ 'defaultdb.db',
    },
    'logger': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

