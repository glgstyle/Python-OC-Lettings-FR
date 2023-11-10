from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.
                          STATIC_ROOT)
