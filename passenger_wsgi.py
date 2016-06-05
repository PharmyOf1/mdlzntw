import sys, os
INTERP = "/home/phihar23/mdlzsupply.com/data/bin/python"
#INTERP is present twice so that the new python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/mdlzntw') 

sys.path.insert(0,cwd+'/data/bin')
#sys.path.insert(0,cwd+'/data/lib/python3.5/site-packages/django')
sys.path.insert(0,cwd+'/data/lib/python3.5/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "mdlzntw.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()