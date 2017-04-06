from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^list/$', views.BookListView.as_view(), name='book-list'),
    url(r'^create/$', views.book_create, name='book_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.book_update, name='book_update'),
]
