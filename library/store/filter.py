from store.models import book
import django_filters

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = book
        fields = ['book_id','book_title','category']