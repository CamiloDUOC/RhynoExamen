from unicodedata import name
from django.urls import URLPattern, path
from .views import home, contacto, login

urlpatterns= [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('login', login, name="login"),
]
