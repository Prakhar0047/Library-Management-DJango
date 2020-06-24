from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from issuing.models import issuing
from issuing.forms import book_issuing
from django.urls import reverse

class book_issue(CreateView):
    form_class = book_issuing
    model = issuing