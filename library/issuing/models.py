from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from store.models import lib_user_model, book

STATUS = [
    (0,'Unpaid'),
    (1,'Paid'),
]

AVAILABLE = [
    (0,'Issued'),
    (1,'Not Issued'),
]

CATEGORY = [
    (0,'UIB'),
    (1,'CSE'),
    (2,'IT'),
    (3,'CEE'),
    (4,'CE'),
    (5,'ME'),
]

# Create your models here.
class issuing(models.Model):
    user_id = models.ForeignKey(lib_user_model, on_delete=models.CASCADE, related_name='issuing_user')
    book_id = models.ForeignKey(book, on_delete= models.CASCADE, related_name='issuing_book')
    book_status = models.ForeignKey(book,on_delete=models.CASCADE, related_name='issuing_book_status')
    date_issued = models.DateTimeField()
    # date_due_for_return = date_issued + 14  Don't Know How
    # date_of_returned = models.DateTimeField()
    # amount_of_fine = models.IntegerField(default=0)