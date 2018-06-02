from django.urls import path
from livraria_app.views import index, contact, about, \
    AuthorDetail, UpdateAuthor, DeleteAuthor, CreateAuthor, AuthorList, \
    PublisherDetail, UpdatePublisher, DeletePublisher, CreatePublisher, PublisherList, \
    BookDetail, UpdateBook, DeleteBook, CreateBook, BookList, \
    CategoryDetail, UpdateCategory, DeleteCategory, CreateCategory, CategoryList


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    # author
    path('author/create', CreateAuthor.as_view(), name='create-author'),
    path('author/list', AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/detail', AuthorDetail.as_view(), name='author-detail'),
    path('author/<int:pk>/update', UpdateAuthor.as_view(), name='update-author'),
    path('author/<int:pk>/delete', DeleteAuthor.as_view(), name='delete-author'),
    # book
    path('book/create', CreateBook.as_view(), name='create-book'),
    path('book/list', BookList.as_view(), name='book-list'),
    path('book/<int:pk>/detail', BookDetail.as_view(), name='book-detail'),
    path('book/<int:pk>/update', UpdateBook.as_view(), name='update-book'),
    path('book/<int:pk>/delete', DeleteBook.as_view(), name='delete-book'),
    # publisher
    path('publisher/create', CreatePublisher.as_view(), name='create-publisher'),
    path('publisher/list', PublisherList.as_view(), name='publisher-list'),
    path('publisher/<int:pk>/detail', PublisherDetail.as_view(), name='publisher-detail'),
    path('publisher/<int:pk>/update', UpdatePublisher.as_view(), name='update-publisher'),
    path('publisher/<int:pk>/delete', DeletePublisher.as_view(), name='delete-publisher'),
    # category
    path('category/create', CreateCategory.as_view(), name='create-category'),
    path('category/list', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/detail', CategoryDetail.as_view(), name='category-detail'),
    path('category/<int:pk>/update', UpdateCategory.as_view(), name='update-category'),
    path('category/<int:pk>/delete', DeleteCategory.as_view(), name='delete-category'),
]