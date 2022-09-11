from .models import User
from django.forms import ModelForm


class userForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'city', 'first_name', 'last_name')