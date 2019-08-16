from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()
import booksdemo.views
from rest_framework import routers
from .views import BookViewSet
from .views import WordViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'words',WordViewSet, basename='word')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^books/$', booksdemo.views.books, name='books'),
    url(r'^words/$', booksdemo.views.words, name='words'),
    #path(r'books', booksdemo.views.BookAPIView.as_view(), name='book-list'),
    #path(r'words', booksdemo.views.WordAPIView.as_view(), name='word-list'),
]

