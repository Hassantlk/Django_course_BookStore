from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from books.models import MdlBook
# Create your views here.

class BookListView(generic.ListView):
    model = MdlBook
    template_name = "books/book_list.html"
    context_object_name = "books"


class BookDetailView(generic.DetailView):
    model = MdlBook
    template_name = "books/book_detail.html"
    context_object_name = "book"

class BookCreateView(generic.CreateView):
    model = MdlBook
    fields = ["title", "author", "content", "price"]
    template_name = "books/book_create.html"
    
class BookUpdateView(generic.UpdateView):
    model = MdlBook
    fields = ["title", "author", "content", "price"]
    template_name = "books/book_update.html"
    
class BookdeleteView(generic.DeleteView):
    model = MdlBook
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")
    