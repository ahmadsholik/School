from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import belle.urls

urlpatterns = [
    url(r"^belle/", include(belle.urls)),
    url(r'^admin/', admin.site.urls),
]

# shouldn't be in the same place as the rest upon deploy
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
