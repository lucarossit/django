from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.car_detail, name="car_detail"),
    # /cars/register
    path('register/', views.register_user, name='register'),
]
