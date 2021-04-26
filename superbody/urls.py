from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('a1', views.a1, name='a1'),
path('contact/', views.contact, name='contact'),
path('diet/', views.diet, name='diet'),
path('about/', views.about, name='about'),
path('thankyou/', views.thankyou, name='thankyou'),
]