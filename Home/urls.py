from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact_us/',views.mail,name="mail"),
    path('reports/',views.reports,name="reports"),
    path('reports/<str:pk>',views.report,name="report"),
    path('events/',views.events,name="events"),
    path('events/<str:pk>',views.event,name="event"),
    path('about/',views.about,name="about"),
    path('history/',views.history,name="history"),
    path('gallery/',views.gallery,name="gallery"),
    path('videogallery/',views.video,name="videogallery"),
]
