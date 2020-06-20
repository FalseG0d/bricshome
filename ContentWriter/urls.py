from django.urls import path
from . import views

urlpatterns = [
    path('',views.interface,name="interface"),
    path('login',views.loginPage,name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
