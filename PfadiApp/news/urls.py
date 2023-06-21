from django.urls import path

from . import views

urlpatterns = [
    path("", views.news, name="news"),
    path('<int:pk>/edit/', views.editNews, name='editNews'),
    path('new/', views.newNews, name='newNews'),
    path('deleteNews/<int:pk>/', views.deleteNews,name='deleteNews')
]
