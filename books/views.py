# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#books/views.py
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Book

class BookDetailView(DetailView):
        model = Book

        # # by default DetailView look for tempate at
        # # appname/lowercaseClassname_detail.html
        # template_name = "books/book_detail.html"

        def get_content_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            context["now"] = timezone.now()
            context["books"] = Book.objects.all()

            return context

class BookListView(ListView):
        model = Book

        # # by default ListView look for tempate at
        # # appname/lowercaseClassname_list.html
        # template_name = "books/book_list.html"



