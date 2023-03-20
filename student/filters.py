import django_filters
from django import forms
from django_filters import DateFilter

from student.models import Student


class StudentFilter(django_filters.FilterSet):

    student_first_name = [(student.first_name, student.first_name.upper()) for student in Student.objects.filter(active=True)]
    new = set(student_first_name)

    #first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    first_name = django_filters.ChoiceFilter(choices=new, label='First name')


    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')

    start_date_gte = DateFilter(field_name='start_date', lookup_expr='gte', label='From start date',
                                widget = forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))

    start_date_lte = DateFilter(field_name='start_date', lookup_expr='lte', label='To start date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    end_date_gte = DateFilter(field_name='end_date', lookup_expr='gte', label='From end date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    end_date_lte = DateFilter(field_name='end_date', lookup_expr='lte', label='To end date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))





    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email', 'start_date_gte', 'start_date_lte', 'end_date_gte','end_date_lte',  'trainer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['first_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter first name'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter last name'})
        self.filters['email'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter email'})
        self.filters['age'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter email'})
        self.filters['trainer'].field.widget.attrs.update({'class': 'form-select'})


