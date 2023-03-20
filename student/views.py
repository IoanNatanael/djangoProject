import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.filters import StudentFilter
from student.forms import StudentUpdateForm
from student.models import Student
from trainer.models import Trainer


# Create your views here.
# CreateView -> il folosim pentru a adauga si salva  pe baza unui formular generat in interfata in tabela specificata.

class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('homepage')
    permission_required = 'student.add_student'

    # fields = '__all__'


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.view_list_of_students'

    def get_queryset(self):
        return Student.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super(StudentListView, self).get_context_data(**kwargs)

        trainers = Trainer.objects.all()

        data['get_all_trainers'] = trainers

        now = datetime.datetime.now()
        data['datetime'] = now

        students = Student.objects.filter(active=True) # Realizam un query prin care luam toti studentii active=True
        filters = StudentFilter(self.request.GET, queryset=students)
        data['all_students'] = filters.qs
        data['filters_form'] = filters.form

        return data


# UpdateView -> Actualizam datele unei inregistrari
class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('homepage')
    permission_required = 'student.change_student'


# DELETEVIEW

class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.delete_student'


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student
    permission_required = 'student.view_student'


@login_required()
@permission_required('student.search_navbar', raise_exception=True)
def search_navbar(request):
    get_value = request.GET.get('search')
    # request.GET-> returneaza un dict cu valoarea pe care am introdus-o in input de search(din interfata)
    # request.GET.get('search') -> iau valoarea cheii search (pe care am scris-o inputul din interfata)
    if get_value:
        students = Student.objects.filter(Q(first_name__icontains=get_value) | Q(email__icontains=get_value))
    else:
        students = {}

    return render(request, 'student/search.html', {'allstudents': students})


@login_required()
@permission_required('student.inactivate_student', raise_exception=True)
def inactivate_student(request, pk):
    Student.objects.filter(id=pk).update(active=False)
    return redirect('list_of_students')
