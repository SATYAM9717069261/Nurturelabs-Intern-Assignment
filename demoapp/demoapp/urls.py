"""demoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ServerSide import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advisor/', views.Advisor_list),
    path('advisor/<int:pk>',views.Advisor_detail),


    path('user/', views.User_list),
    path('user/register/', views.User_detail),
    path('user/<int:pk>',views.User_detail),


    path('user/<int:pk>/advisor', views.Advisor_list),
    path('user/<int:uid>/advisor/<int:aid>', views.Booking_detail),
    path('user/advisor/booking/',views.Booking_list),
]
