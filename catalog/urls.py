from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('mybooks/', views.loan_book, name='my-borrowed'),
    path('borrowed/', views.borrowed, name='all_borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('new_book/', views.new_book, name='new_book'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='delete_book'),
    path('book/<int:pk>/edit/', views.BookEdit.as_view(), name='edit_book'),
    path('signup/', views.signup, name='signup'),
    # uidb64 was bugging, its just a user pk now
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signup/success_register/', views.success_register, name='success_register'),
    path('signup/success_activate/', views.success_activate, name='success_activate')
]