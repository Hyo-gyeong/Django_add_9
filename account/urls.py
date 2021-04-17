from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account'

urlpatterns = [
  path('login/', LoginView.as_view(template_name = 'account/login.html'), name='login'),
  path('logout/', LogoutView.as_view(template_name = 'account/logout.html'), name='logout'),
  #장고에서 지원하는 loginview와 logoutview를 활용하여 바로 login.html과 logout.html로 연결시켜줌
]