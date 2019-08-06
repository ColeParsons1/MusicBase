from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from .import views


urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^music/', views.index, name='index'),
    url(r'^genres/$', views.genres, name='genres'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^albums/$', views.albums, name='albums'),
    url(r'^genre_details/$', views.genre_details, name='genre_details'),
    url(r'^genre_History/$', views.genre_details, name='genre_History'),
]

