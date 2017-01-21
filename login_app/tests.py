from django.test import TestCase
from login_app.models import *

# Create your tests here.
def test():
    user = User(id = '11', password = '먹으러', nickname = '갈래?')
    user.save()