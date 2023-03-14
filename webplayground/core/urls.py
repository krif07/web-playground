from django.urls import path
from .views import HomePageView, SamplePageview

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageview.as_view(), name="sample"),
]