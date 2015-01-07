from django.shortcuts import render, redirect
from django import forms
from students.models import Student
from courses.models import Course
from extradata.models import Dossier
from django.utils.translation import ugettext_lazy as _

import logging
logger = logging.getLogger(__name__)


class StudentForm(forms.Form):
    CHOICES = (('Standart', 'Standart'),
               ('Gold', 'Gold'))
    student_name = forms.CharField(label=_("Name"), max_length=100)
    student_surname = forms.CharField(label=_("Surname"), max_length=255)
    student_date_of_birth = forms.DateField(label=_("Date of bith"))
    student_email = forms.EmailField()
    student_phone = forms.CharField(label=_("Phone number"), max_length=15)
    student_package = forms.ChoiceField(label=_("Package"), widget=forms.RadioSelect,
                                        choices=CHOICES)
    student_course = forms.ModelChoiceField(label=_("Course"), queryset=Course.objects.all(),)
    student_dossier = forms.ModelChoiceField(label=_("Dossier"), queryset=Dossier.objects.all(),required=False)



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
            try:
                student.save()
                logger.info("Student %s %s was updated." % (student.name, student.surname))
            except:
                logger.error("Student %s %s didn't update." % (student.name, student.surname))
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
    try:
        student.delete()
        logger.info("Student %s %s was removed." % (student.name, student.surname))
    except:
        logger.error("Student %s %s didn't romove." % (student.name, student.surname))
    return redirect('students:list')
