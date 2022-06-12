from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator,EmptyPage

class ShowView(ListView):
    model = Book
    page=1
    booklist = Book.objects.all()
    paginator=Paginator(booklist,3)
    try:
        booklist=paginator.page(page)
    except EmptyPage:
        booklist=paginator.page(paginator.num_pages)
    context_object_name = "book_list"

class AddBook(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('showbooks_url')

class DeleteBook(DeleteView):
    model=Book 
    success_url = reverse_lazy('showbooks_url')

class UpdateBook(UpdateView):
    model=Book
    fields='__all__'
    success_url = reverse_lazy('showbooks_url')
