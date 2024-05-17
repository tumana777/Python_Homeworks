from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name="index"),
    path('info/<int:id>/', views.book_info, name="book_info"),
    path('delete/<int:id>/', views.delete_book, name="delete_book"),
]
