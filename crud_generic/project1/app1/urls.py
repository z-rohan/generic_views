from django.urls import path
from .views import *

urlpatterns=[
    path('ab/',AddBook.as_view(),name="addbook_url"),
    path('sb/',ShowView.as_view(),name="showbooks_url"),
    path('db/<int:pk>/',DeleteBook.as_view(),name='deletebook_url'),
    path('ub/<int:pk>/',UpdateBook.as_view(),name='updatebook_url')
]