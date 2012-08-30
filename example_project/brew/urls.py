from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from .models import Beverage

urlpatterns = patterns('brew.views',
    # Examples:
#    url(r'^$', 'restaurant.views.home', name='home'),
    url(r'^$', ListView.as_view(model=Beverage, context_object_name='beverages', allow_empty=True)),

)