from django.urls import path
from . import views
# associate aparticular url with aparticular view
# the way django does that is through a variable called urlPatterns
# urlPatterns is list of all of urls supported by this app
urlPatterns = [
    path("", views.index)
]
