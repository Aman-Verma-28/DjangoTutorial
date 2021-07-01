from django.urls import path
from . import views


urlpatterns = [
    path("",views.index2,name="index2"),
    path("signup",views.signup,name="signup"),
    path("user",views.user,name="user"),
    path("v1/",views.v1,name="v1",),
    path("add",views.add,name="add")
]

