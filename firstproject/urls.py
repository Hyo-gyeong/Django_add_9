from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('like.urls')),
    path('account/', include('account.urls')),
    path('email/', include('emailapp.urls')),
    path('chat/', include('chat.urls')),
    path('weather/', include('weather.urls')),
    path('star/', include('star.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
