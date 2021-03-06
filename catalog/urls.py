from . import views
from django.conf.urls import url
from django.urls import path




urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path(
        route='books_details/<int:pk>', 
        view= views.BookDetailView.as_view(), 
        name='book-detail'
         ),
    path(
        route='authors/',
        view= views.AuthorListView.as_view(),
        name='authors'
         ),
    path(
        route='authors_details/<int:pk>',
        view= views.AuthorDetailView.as_view(),
        name='author-detail'
         ),
    path(
        route='partida/', 
        view=views.partida, 
        name='logout_'
        ),
    path(
        route='login/', 
        view=views.login, 
        name='login'
        ),
    path(
        route='allstatusbooks/', 
        view=views.AllBorrowedListView.as_view(), 
        name='all-status'
        ),
    path(
        route='book/<uuid:pk>/renew/', 
        view=views.renew_book_librarian, 
        name='renew-book-librarian'
        ),
    path(
        route='author/create/', 
        view=views.AuthorCreate.as_view(),
        name='author_create'
        ),
    path(
        route='author/<int:pk>/update/', 
        view=views.AuthorUpdate.as_view(), 
        name='author_update'
        ),
    path(
        route='author/<int:pk>/delete/', 
        view=views.AuthorDelete.as_view(), 
        name='author_delete'
        ),
    path(
        route='book/create/', 
        view=views.BookCreate.as_view(),
        name='book_create'
        ),
    path(
        route='book/<int:pk>/update/', 
        view=views.BookUpdate.as_view(), 
        name='book_update'
        ),
    path(
        route='book/<int:pk>/delete/', 
        view=views.BookDelete.as_view(), 
        name='book_delete'
        ),
    path(
        route='bookInstance/<int:pk>/', 
        view=views.BookInstanceCreate.as_view(),
        name='bookinstance-create'
        ),


]
urlpatterns += [   
    path(
        route='mybooks/',
        view= views.LoanedBooksByUserListView.as_view(), 
        name='my-borrowed'
        ),
        
]