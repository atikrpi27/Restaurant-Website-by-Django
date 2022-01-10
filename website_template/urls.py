from django.contrib import admin
from django.urls import path
from . import views
apps_name='website_template'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
