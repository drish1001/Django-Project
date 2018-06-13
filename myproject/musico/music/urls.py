from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^list/$', views.music, name="music" ),
    url(r'^(?P<pk>[0-9]+)/$', views.listsong, name="list_song"),
    url(r'^settings/$', views.add_movie, name="setting"),
    url(r'^add-song/$', views.add_song, name="add-song")
]
