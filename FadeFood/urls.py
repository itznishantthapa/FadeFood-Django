"""
URL configuration for FadeFood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentications.views import create_user, login_user,get_user_details, edit_user_details
from restaurant.views import register_restaurant, edit_restaurant
from foods.views import add_food
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', create_user),
    path('edit_user_details/', edit_user_details),
    path('login_user/', login_user),
    path('get_user_details/', get_user_details),
    path('register_restaurant/', register_restaurant),
    path('edit_restaurant/', edit_restaurant),
    path('add_food/', add_food),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
