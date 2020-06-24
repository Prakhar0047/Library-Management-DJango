from django.urls import path
from issuing import views

app_name = 'issuing'

urlpatterns = [
    path('issue/',views.book_issue.as_view(),name='book_issue'),    
]