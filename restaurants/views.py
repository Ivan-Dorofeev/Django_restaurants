from django.views.generic import ListView
from .models import Restaurant


class RestaurantView(ListView):
    model = Restaurant
    template_name = 'restaurants/restaurants_list.html'
    context_object_name = 'restaurant_data'
