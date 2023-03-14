from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page

# Create your views here.
class PageListView(ListView):
    model = Page
    paginate_by = 20


class PageDetailView(DetailView):
    model = Page
