from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve


urlpatterns = [

    path('', home, name='home_html'),
    path('upload', upload, name='fileupload_html'),
    path('records/', display_records, name='display_records'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),    

    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
