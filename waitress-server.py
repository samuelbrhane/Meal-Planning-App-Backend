from waitress import serve
from plateplanbackend.wsgi import application

serve(application, host='localhost', port='8000')
