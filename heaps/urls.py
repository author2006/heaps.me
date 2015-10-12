from django.conf.urls import include, url, static
from django.contrib import admin
from django.conf.urls.static import static
from heaps import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'ckeditor', include('ckeditor_uploader.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('heaps_app.urls', namespace='heaps_app')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
