import os
import sys

sys.path.append('/home/ubuntu/weatherStationProject/weatherstation/weatherstation')
sys.path.append('/home/ubuntu/weatherStationProject/weatherstation')
sys.path.append('/home/ubuntu/weatherStationProject')

apache_dir = os.path.dirname(__file__)
project = os.path.dirname(apache_dir)
workspace = os.path.dirname(project)
if workspace not in sys.path:
    sys.path.append(workspace)

os.environ['DJANGO_SETTINGS_MODULE'] = 'weatherstation.settings'
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
