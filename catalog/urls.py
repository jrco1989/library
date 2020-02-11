from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path ('books_details/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]