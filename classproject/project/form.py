from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User
from .models import Restaurant, Dish

class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

class UserChangeForms(UserChangeForm):

    class Meta:

        model = User
        fields = UserChangeForm.Meta.fields


class RestaurantForm(ModelForm):
  class Meta:
    model = Restaurant
    exclude = ('user', 'date',)

class DishForm(ModelForm):
  class Meta:
    model = Dish
    exclude = ('user', 'date',)
