from django.urls import path
from . import views

urlpatterns = [
  path('', views.email_home, name="email_home"),
  path('send_email', views.send_email, name="send_email"),
]