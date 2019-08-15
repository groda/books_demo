from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()
import booksdemo.views
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path("", booksdemo.views.index, name="index"),
    path("db/", booksdemo.views.db, name="db"),
    #path("admin/", admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^books/$', booksdemo.views.books, name='books'),
    #path(r'books', booksdemo.views.BookAPIView.as_view(), name='book-list'),
    path(r'words', booksdemo.views.WordAPIView.as_view(), name='word-list'),
]

