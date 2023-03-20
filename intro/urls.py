from django.urls import path

from intro import views

urlpatterns = [
    path("firstpage/", views.first_page, name="first-page"),
    path('list_of_cars/', views.cars, name='list-of-cars'),
    path('list_of_series/', views.series, name='list-of-series')
]
