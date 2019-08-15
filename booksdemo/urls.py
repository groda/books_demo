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
    path("db/", booksdemo.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('',booksdemo.views.BookList.as_view(), name='book_list'),
]

###    path("", booksdemo.views.index, name="index"),
###    path('view/<int:pk>',booksdemo.views.BookView.as_view(), name='book_view'),
###    path('new',booksdemo.views.BookCreate.as_view(), name='book_new'),
###    path('view/<int:pk>',booksdemo.views.BookView.as_view(), name='book_view'),
###    path('edit/<int:pk>',booksdemo.views.BookUpdate.as_view(), name='book_edit'),
###    path('delete/<int:pk>',booksdemo.views.BookDelete.as_view(), name='book_delete'),


