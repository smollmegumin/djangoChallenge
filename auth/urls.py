from django.urls import path

# from the same directory imports the view file
from . import views

urlpatterns =[
    path("auth/",views.Auth.as_view()),
    path("access/",views.Access.as_view())
]