
from django.urls import path, include


from . import views

urlpatterns=[
    
    path('',views.home, name='index'),
    path('add',views.add, name='add'),

]