from django.contrib import admin
from .models import Restaurant
from .models import Dish
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .form import UserForm,UserChangeForms
from .models import User
from .models import Room


admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)



class UserAdmin(UserAdmin):
    new_form = UserForm
    form = UserChangeForms
    model = User
    display_form = ['User']

admin.site.register(User,UserAdmin)
admin.site.register(Restaurant)
admin.site.register(Dish)
