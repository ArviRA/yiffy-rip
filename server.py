from os import name
from waitress import serve 
from yiffy.wsgi import application

if __name__ == '__main__':
    serve(application,port='8000')
