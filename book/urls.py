from django.urls import path
from book import views

urlpatterns = [
    path('get_data/', views.get_books_by_emag, name='get-data')
]