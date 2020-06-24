from django.contrib import admin
from store.models import book, lib_user_model

admin.site.register(book)
admin.site.register(lib_user_model)