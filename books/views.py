from audioop import reverse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Ep.169 , Ep.171
from django.contrib.auth.decorators import login_required # Ep.169

from books.models import MdlBook
from .forms import *
# Create your views here.

class BookListView(generic.ListView):
    model = MdlBook
    paginate_by = 2
    template_name = "books/book_list.html"
    context_object_name = "books"


# class BookDetailView(generic.DetailView):
#     model = MdlBook
#     template_name = "books/book_detail.html"
#     context_object_name = "book"
    
@login_required
def book_detail_view(request, pk): #
    book = get_object_or_404(MdlBook, pk=pk)
    book_comments = book.comments.all() # mainmodel.relatedName.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {
        "book": book,
        "comments": book_comments,
        "comment_form": comment_form,
    }
    return render(request, "books/book_detail.html", context)

class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = MdlBook
    fields = ["title", "author", "content", "price", "cover"]
    template_name = "books/book_create.html"
    
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = MdlBook
    fields = ["title", "author", "content", "price", "cover"]
    template_name = "books/book_update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    
class BookdeleteView(LoginRequiredMixin, generic.DeleteView):
    model = MdlBook
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    