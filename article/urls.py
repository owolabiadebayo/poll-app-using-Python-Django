from django.urls.resolvers import URLPattern
from django.urls import path

from . import views
from .views import DeleteListView, UpdateListView, ContactView

app_name='article'

urlpatterns=[
    path("home/", views.HomeListView.as_view(), name='home'),
    path("<str:id>/delete/", DeleteListView.as_view(), name="delete"),
    path("<str:id>/update/", UpdateListView.as_view(), name="update"),

    
]