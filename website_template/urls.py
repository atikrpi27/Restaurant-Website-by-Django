from django.contrib import admin
from django.urls import path
from . import views

apps_name='website_template'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('team/', views.team, name='team'),
    path('special_dishes/', views.special_dishes, name='special_dishes'),
    path('base/', views.base, name='base'),
]
