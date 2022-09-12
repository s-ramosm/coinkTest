from django.urls import path
from .views import createUser, listUsers
urlpatterns = [
    path('', createUser,name="user" ),
    path('all/' , listUsers, name="list_user")
]
