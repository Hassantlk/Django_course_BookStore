from django.urls import path, include
from .views import *
urlpatterns = [
    path('', BookListView.as_view(), name="book_list"),
    path('<int:pk>', BookDetailView.as_view(), name="book_detail"),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name="book_update"),
    path('<int:pk>/delete/', BookdeleteView.as_view(), name="book_delete"),
    path('create/', BookCreateView.as_view(), name="book_create"),
]
