from django.urls import path,re_path
from django.views.generic import DetailView, ListView, UpdateView
from .form import RestaurantForm,DishForm
from .models import Restaurant,Dish
from .views import  RestaurantDetail,RestaurantCreate,DishCreate,DishDetail
from . import views
from django.utils import timezone

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),

    re_path(r'^myrestaurants',ListView.as_view(
        	queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:10],
            context_object_name='latest_restaurant_list',
            template_name='restaurant_list.html'),
            name='restaurant_list'),


     re_path(r'^mydishes',ListView.as_view(
        	queryset=Dish.objects.filter(date__lte=timezone.now()).order_by('date')[:10],
            context_object_name='latest_dishes_list',
            template_name='dish_list.html'),
            name='dish_list'),


    re_path(r'^restaurants/(?P<pk>\d+)/\$',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),


    re_path(r'^mydishes/(?P<pkr>\d+)/\$',
        DishDetail.as_view(),
        name='dish_detail'),  

    re_path(r'\^restaurants/create/\$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),


    re_path(r'\^mydishes/create/\$',
    	DishCreate.as_view(),
        name='dish_create'),


     re_path(r'^Customerpage/',views.CustomerPage,name='customerpage'),


     re_path(r'^Customersupport/',views.CustomerSupport,name='customersupport'),

     re_path(r'^deals/',views.Deals,name='deals'),

     re_path(r'^menu/',views.Menu,name='menu'),
	 
	 re_path(r'^chat/', views.Chat, name='chat'),




]