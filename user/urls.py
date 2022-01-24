from django.contrib import admin
from django.urls import path
from . import views

apps_name='user'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userLogout, name='userLogout'),
]
