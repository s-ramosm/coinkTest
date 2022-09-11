from django.shortcuts import render
from .forms import userForm
# Create your views here.
from .models import User


def createUser(request):
    
    if request.method == "GET": 

        return render(
            request, 
            'user_form.html',
            {
                "form" :  userForm
            }
        )

    else:

        form = userForm(request.POST)
        user = form.save()
        return render(
            request, 
            'user_form.html',
            {
                "form" :  userForm
            }
        )

def listUsers(request):
    users = User.objects.get_queryset()
    return render(
            request, 
            'users.html',
            {
                "users" :  users
            }
        )


def parzival(request):    
    if request.method == "GET": 
        return render(
            request, 
            'parzival.html',
        )