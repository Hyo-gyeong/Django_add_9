from django.urls import path
from .views import PhotoList, PhotoCreate, PhotoDetail, PhotoUpdate, delete
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views

app_name = "like" #다른 앱들과 urlpattern이 겹치는것을 방지하기위해 사용
urlpatterns = [
    path('', PhotoList.as_view(), name="index"), #클래스형 view
    path('create/', PhotoCreate.as_view(), name="create"),
    path('delete/<int:post_id>', views.delete, name="delete"),
    path('update/<int:pk>', PhotoUpdate.as_view(), name="update"),
    path('detail/<int:pk>', PhotoDetail.as_view(), name="detail"),
    path('like/', views.post_likes, name="post_likes"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
