from django.urls import path

# from the same directory imports the view file
from . import views

urlpatterns =[
    path("api/cars/",views.Index.as_view())
]