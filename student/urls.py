from django.urls import path

from student import views

urlpatterns = [
    path('create-student/', views.StudentCreateView.as_view(), name='create_student'),
    path('list-of-students/', views.StudentListView.as_view(), name='list_of_students'),
    path('update-student/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete-student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student'),
    path('details-student/<int:pk>/', views.StudentDetailView.as_view(), name='details_student'),
    path('search-navbar', views.search_navbar, name='search'),
    path('inactivate-student/<int:pk>', views.inactivate_student, name='inactivate-student')
]