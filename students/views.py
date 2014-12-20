from django.shortcuts import render, redirect
from django import forms
from students.models import Student
from courses.models import Course
from extradata.models import Dossier


class StudentForm(forms.Form):
    CHOICES = (('Standart', 'Standart'),
               ('Gold', 'Gold'))
    student_name = forms.CharField(max_length=100)
    student_surname = forms.CharField(max_length=255)
    student_date_of_birth = forms.DateField()
    student_email = forms.EmailField()
    student_phone = forms.CharField(max_length=15)
    student_package = forms.ChoiceField(widget=forms.RadioSelect,
                                        choices=CHOICES)
    student_course = forms.ModelChoiceField(queryset=Course.objects.all(),)
    student_dossier = forms.ModelChoiceField(queryset=Dossier.objects.all(),required=False)



def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def students_item(request, student_id):
    student = Student.objects.get(id=int(student_id))
    return render(request, 'students/item.html', {'student': student})

def students_edit(request, student_id=None):
    if student_id is None:
        student = Student()
    else:
        student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student.name = form.cleaned_data['student_name']
            student.surname = form.cleaned_data['student_surname']
            student.package = form.cleaned_data['student_package']
            student.date_of_birth = form.cleaned_data['student_date_of_birth']
            student.email = form.cleaned_data['student_email']
            student.phone = form.cleaned_data['student_phone']
            student.course = form.cleaned_data['student_course']
            student.dossier = form.cleaned_data['student_dossier']
            student.save()
            return redirect('students:list')

    else:
        form = StudentForm(initial={'student_name': student.name,
                                    'student_surname': student.surname,
                                    'student_date_of_birth': student.date_of_birth,
                                    'student_email': student.email,
                                    'student_phone': student.phone,
                                    'student_package': student.package,
                                    'student_course': student.course,
                                    'student_dossier': student.dossier})
    return render(request, 'students/edit.html', {'form': form})

def students_remove(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('students:list')
