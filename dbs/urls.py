from django.urls import path
from .views import BookCreate
urlpatterns = [
    path('books/', BookCreate.as_view(), name="add_book"),
]
