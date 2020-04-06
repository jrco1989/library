from . import views
from django.conf.urls import url
from django.urls import path




urlpatterns = [
    path(
        route='',
        view= views.index,
        name='index'
         ),
    path(
        route='books/',
        view= views.BookListView.as_view(),
        name='books'
         ),
    path (
        route='books_details/<int:pk>',
        view= views.BookDetailView.as_view(),
        name='book-detail'
         ),
    path (
        route='authors/', 
        view=views.AuthorListView.as_view(),
        name='authors'
        ),
    path(
        route='authors_details/<int:pk>',
        view= views.AuthorDetailView.as_view(),
        name='author-detail')

]