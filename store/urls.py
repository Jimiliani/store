from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from items.urls import urlpatterns as items_urlpatterns
from requests.urls import urlpatterns as requests_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(items_urlpatterns)),
    path('', include(requests_urlpatterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
