from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('New_User/',views.New_lib_user.as_view(),name='new_lib_user'),
    path('New_Book/',views.New_lib_book.as_view(),name='new_lib_book'),
    path('About_Us',views.about_us, name='about_us'),
    path('Rule',views.rules, name='rules'),
    path('Book_detail/<int:pk>',views.BookDetail.as_view(),name='book_detail'),
    path('search/', views.search, name='search'),
    path('',views.bookList.as_view(), name='index'),
]