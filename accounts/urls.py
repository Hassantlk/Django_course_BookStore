from django.urls import include, path

from .views import *

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup")
]
