from django.urls import path
from .views import list_cars, create_car, update_car, delete_car

urlpatterns = [
  path('list', list_cars, name='list_cars'),
  path('new', create_car, name='create_cars'),
  path('update/<int:id>/', update_car, name='update_car'),
  path('delete/<int:id>/', delete_car, name='delete_car'),

]
