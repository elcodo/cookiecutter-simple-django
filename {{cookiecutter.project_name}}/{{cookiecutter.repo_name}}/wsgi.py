import os
import sys

sys.path.append(os.path.abspath(__file__ + '/../..'))
sys.path.insert(1, os.path.abspath(__file__ + '/../../../.venv/lib/python{{cookiecutter.python_version}}/site-packages'))

print(os.path.abspath(__file__ + '/../../../.venv/lib/python2.7/site-packages'))
source_dir = os.path.abspath(__file__ + '/../../../.venv/src/')
if os.path.exists(source_dir):
    for name in os.listdir(source_dir):
        if os.path.isdir(os.path.join(source_dir, name)):
            sys.path.append(os.path.join(source_dir, name))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.repo_name}}.settings")

application = get_wsgi_application()