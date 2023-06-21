from django.urls import path

from . import views

urlpatterns = [
    path("", views.events, name="events"),
    path('new/', views.newEvent, name='newEvent'),
    path('participate/', views.participate,name='participate'),
    path('deleteEvent/<int:pk>/', views.deleteEvent,name='deleteEvent'),
    path('viewParticipants/<int:pk>/', views.viewParticipants,name='viewParticipants'),
    path('participating/', views.participating,name='participating'),
]