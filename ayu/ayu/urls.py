"""
URL configuration for ayu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.chat, name='chat')
Class-based views
    1. Add an import:  from other_app.views import chat
    2. Add a URL to urlpatterns:  path('', chat.as_view(), name='chat')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
# from . import views
# from ayuapp.views import chat_list 
# from ayuapp.views import login
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('get-response/', views.get_response, name='get_response'),
#     path('login/', views.login, name='login'),
#     path('about/', views.about, name='about us'),
#     path('contact/', views.contact, name='contact us'),
#     path('chat/', views.chat, name='chat'),
#     path('chatList/', chat_list, name='chat_list'),
# ]

from django.urls import path
from django.contrib import admin

from ayu import views
# from ayuapp import views as ayuapp_views
urlpatterns = [
    path('', views.home, name='home'),
    path('get-response/', views.get_response, name='get_response'),
    path('admin/', admin.site.urls),   # use login from ayuapp.views
    path('about/', views.about, name='about us'),
    path('contact/', views.contact, name='contact us'),
    path('chat/', views.chat, name='chat'),
    # path('chatList/',ayuapp_views.chat_list, name='chat_list'),
]


