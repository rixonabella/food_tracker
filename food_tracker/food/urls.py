from django.conf.urls import url

from .views import index

#Register add_meal to urls.py
#from .views import index, add_meal

#Register delete_meal to urls.py
#from .views import index, add_meal, delete_meal

#Register update_meal to urls.py
from .views import index, add_meal, delete_meal, update_meal, view_meal, login


urlpatterns = [
    url(r'^$', login, name='login'),

    url(r'^index$', index, name='index'),
    #Register add_meal to urls.py
    url(r'^add_meal$', add_meal, name='add-meal'),
    #Register delete_meal to urls.py
    url(r'^delete_meal/(?P<meal_id>\d+)$', delete_meal, name='delete-meal'),
    #Register update_meal to urls.py
    url(r'^update_meal/(?P<meal_id>\d+)$', update_meal, name='update-meal'),
	#Register view_meal to urls.py
    url(r'^view_meal/(?P<meal_id>\d+)$', view_meal, name='view-meal'),
]