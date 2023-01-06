from django.urls import path, re_path, include
from . import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', views.post, name='post'),
]

#nos permite ver las imagenes con el debug en true

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]