from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()
import booksdemo.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/


urlpatterns = [
    path("", booksdemo.views.index, name="index"),
    path("db/", booksdemo.views.db, name="db"),
    path("admin/", admin.site.urls),
    url(r'^$', booksdemo.views.BookList, name='book_list'),
    url(r'^(?P<pk>\d+)/delete/$', booksdemo.views.BookDelete, name='book_delete'),
    url(r'^(?P<pk>\d+)/update/$', booksdemo.views.BookUpdate, name='book_update'),
    url(r'^create/$', booksdemo.views.BookCreate, name='book_create'),
]


