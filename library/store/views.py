# IMPORTS
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from store.models import lib_user_model, book
from store.forms import new_lib_user_form, new_lib_book_form
from django.urls import reverse
from store.filter import BookFilter

# FUNCTIONS
def index(request):
    return render(request,'store/index.html')

def about_us(request):
    return render(request,'store/about_us.html')

def rules(request):
    return render(request,'store/lib_rules.html')

def search(request):
    book_list = book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list)
    return render(request,'store/book_filter_list.html', {'filter': book_filter})

# CLASSES
class New_lib_user(CreateView):
    form_class = new_lib_user_form
    model = lib_user_model

class New_lib_book(CreateView):
    form_class = new_lib_book_form
    model = book


class bookList(ListView):
    queryset = book.objects.all().order_by('-published_date')
    template_name = "store/book_list.html"

class availableBookList(ListView):
    queryset = book.objects.all().filter(available=1).order_by('book_id')
    template_name = "issuing/issuing_form.html"


class BookDetail(DetailView):
    model = book
    template_name = 'store/book_detail.html'