from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Select, Textarea, DateInput

from student.models import Student


class StudentForm(forms.ModelForm):
    #address = forms.CharField()

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email', 'trainer', 'description',
                  'start_date', 'end_date', 'active', 'gender']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name:'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name:'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'trainer': Select(attrs={'class': 'form-select'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter description:',
                                           'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'})

        }

    def clean(self):
        cleaned_data = self.cleaned_data  # stocam in variabila cleaned_data un dictionar cu valoarile pe
        # care le introduce utilizatorul in formular
        all_students = Student.objects.filter(first_name__exact=cleaned_data.get(
            'first_name'))  # interogam tabela student_student si cautam daca exista un/mai multi studenti
        # cu first_name Adrian
        if all_students:  # daca exista un student cu numele de Adrian ne va genera o eroare
            msg = f'This first name {cleaned_data.get("first_name")} exists in the database'  # mesajul erorii
            self._errors['first_name'] = self.error_class([msg])  # afisarea erorii pe fieldul first_name

        st_date = cleaned_data.get('start_date')
        ed_date = cleaned_data.get('end_date')
        if st_date > ed_date:
            msg2 = f'The start date is greater than the end date'
            self.errors['start_date'] = self.error_class([msg2])

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email', 'trainer', 'description',
                  'start_date', 'end_date', 'active', 'gender']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name:'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name:'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'trainer': Select(attrs={'class': 'form-select'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter description:',
                                           'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'})

        }
