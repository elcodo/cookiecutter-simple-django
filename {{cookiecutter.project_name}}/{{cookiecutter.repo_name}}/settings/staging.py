{% if cookiecutter.use_psql == 'yes' %}DATABASES = {
    'default': {
        'NAME': '{{cookiecutter.repo_name}}',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
    }
}{% endif %}
{% if cookiecutter.use_mysql == 'yes' %}DATABASES = {
    'default': {
        'NAME': '{{cookiecutter.repo_name}}',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    },
}{% endif %}
