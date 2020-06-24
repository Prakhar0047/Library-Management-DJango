from django.db import models
from django.urls import reverse
from django.utils.timezone import now

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

class lib_user_model(models.Model):
    user_id = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=40)
    uni_roll_no = models.IntegerField(unique=True)
    branch = models.IntegerField(choices=CATEGORY,default=0)

    def get_absolute_url(self):
        return reverse('store:index')

class book(models.Model):
    book_id = models.IntegerField(unique=True)
    book_title = models.CharField(max_length=100)
    author_id = models.CharField(max_length=6, unique=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=10)
    published_date = models.DateTimeField(default=now)
    available = models.IntegerField(choices=AVAILABLE, default=0)
    
    def get_absolute_url(self):
        return reverse('store:index')

    def __str__(self):
        return self.book_title