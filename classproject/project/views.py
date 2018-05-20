from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.urls import path,include,re_path
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .form import RestaurantForm, DishForm
from .models import Restaurant,Dish
from .form import UserForm
from .models import Room
from pusher import pusher
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



class SignUp(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class RestaurantDetail(DetailView):
    model = Restaurant
    template = 'project/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        return context

class DishDetail(DetailView):
    model = Dish
    template = 'project/dish_detail.html'

    def get_context_data(self, **kwargs):   
        context = super(DishDetail, self).get_context_data(**kwargs)
        return context

class RestaurantCreate(CreateView):
    model = Restaurant
    template_name = 'project/form.html'
    form_class = RestaurantForm
    success_url = reverse_lazy('customerpage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)

class DishCreate(CreateView):

    model = Dish
    template = 'project/dish_form.html'
    form_class = DishForm
    success_url = reverse_lazy('customerpage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DishCreate, self).form_valid(form)
    

def CustomerPage(request):
    return render(request, 'customerpage.html')


def CustomerSupport(request):
    return render(request, "customersupport.html")


def Deals(request):
    return render(request, 'Deals.html')

def Menu(request):
    return render(request, 'Menu.html')
	
pusher_client = pusher.Pusher(
  app_id='528963',
  key='990d674de4ae52226513',
  secret='eb8e90be2be631923f5b',
  host='api.pusherapp.com',
  ssl=True)
def Chat(request):

    return render(request, "chatlogin.html") 
	
	
@csrf_exempt
def broadcast(request):

	pusher_client.trigger('my-channel', 'my-event', {u'name': request.user.username, u'message': request.POST['message']})		
	return HttpResponse("done")