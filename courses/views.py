from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView, DeleteView)
from django import forms
from courses.models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course


class CourseListView(ListView):
    model = Course
    template_name = 'courses/list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/item.html'
    context_object_name = 'course'


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    success_url = reverse_lazy('courses:list')
    context_object_name = 'course'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/edit.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('courses:list')
    context_object_name = 'course'


class CourseDeleteView(DeleteView):
    template_name = 'courses/remove.html'
    model = Course
    success_url = reverse_lazy('courses:list')


