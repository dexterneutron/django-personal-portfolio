
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from blog import views


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]