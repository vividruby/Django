from django.shortcuts import render
from .models import Restaurant


def index(request):
    restaurant_list = Restaurant.objects.order_by('restaurant_name')
    context = {'restaurant_list': restaurant_list}
    return render(request, 'rest/restaurant_list.html', context)

def detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    context = {'restaurant': restaurant}
    return render(request, 'rest/restaurant_detail.html', context)