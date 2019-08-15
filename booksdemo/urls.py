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
    url(r'^$', booksdemo.views.book_list, name='book_list'),
    url(r'^(?P<pk>\d+)/delete/$', booksdemo.views.book_delete, name='book_delete'),
    url(r'^(?P<pk>\d+)/update/$', booksdemo.views.book_update, name='book_update'),
    url(r'^create/$', booksdemo.views.book_create, name='book_create'),
    path('books/', include('books.urls')),
]


