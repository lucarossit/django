from django.urls import path
from . import views  #importing our view file 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.homepage, name="home"), #mapping the homepage function
]

urlpatterns += staticfiles_urlpatterns()
