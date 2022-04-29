from pathlib import Path
from django.db.backends.mysql.base import DatabaseWrapper

# version 문제 발생시 해결 사항
DatabaseWrapper.data_types['DateTimeField'] = 'datetime' # fix for MySQL 5.5
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'csweb',
        'USER': 'admin',
        'PASSWORD': '123qwe',
        'HOST': '54.180.102.243',
        'PORT': '57420',
    }
    # ,
    # 'referencedb1': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'csweb',
    #     'USER': 'admin',
    #     'PASSWORD': '123qwe',
    #     'HOST': '54.180.79.115',
    #     'PORT': '52146',
    # }
}
SECRET_KEY = 'django-insecure-5mkhqyjvr-_c%%3zw8i+z9+cuc4qbuqh^l*p^mqgcqrxt40*jd'
