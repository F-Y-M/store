from app.config.logic import dataPostLogic
from django.views.generic import TemplateView
from os.path import join, dirname
from dotenv import load_dotenv
from  ..class.dataPost import dataPostLogic

class dataPost(TemplateView,dataPostLogic):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    status = os.getenv('STATUS')
    secret_key = os.getenv('SECRET_KEY')