from django.urls import path
from .views import page_view

urlpatterns = [
    path("new_page/", page_view)
]