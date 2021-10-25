from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('posts.urls')),
    path('weather/', include('weather.urls')),
    path('chat/', include('chat.urls'))
]
