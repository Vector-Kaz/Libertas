#books/urls.py
from django.conf.urls import url

from .views import BookDetailView, BookListView

urlpatterns = [
    url(r'^$', BookListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', BookDetailView.as_view(), name='detail'),
]
