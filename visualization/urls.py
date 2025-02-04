from django.urls import path

from visualization.views import login, views
# from visualization.views import views

urlpatterns = [
    path("", login.login),
]
