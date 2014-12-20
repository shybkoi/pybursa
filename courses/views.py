from django.shortcuts import render, redirect
from django import forms
from courses.models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})

def course_item(request, course_id):
    course = Course.objects.get(id=int(course_id))
    print course.assistant
    return render(request, 'courses/item.html', {'course': course})

def course_edit(request, course_id=None):
    if course_id is None:
        course = Course()
    else:
        course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST,  instance=course)
        if form.is_valid():
            course.save()
            return redirect('courses:list')
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})

def course_remove(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('courses:list')
