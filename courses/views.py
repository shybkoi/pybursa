from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView, DeleteView)
from django import forms
from courses.models import Course

import logging
logger = logging.getLogger(__name__)


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

    def form_valid(self, form):
        try:
            form.save()
            logger.info("Course %s %s was updated." % (form.cleaned_data['name'], form.cleaned_data['description']))
        except:
            logger.error("Course %s %s didn't update." % (form.cleaned_data['name'], form.cleaned_data['description']))
        return super(CourseUpdateView, self).form_valid(form)


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/edit.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('courses:list')
    context_object_name = 'course'

    def form_valid(self, form):
        try:
            form.save()
            logger.info("Course %s %s was created." % (form.cleaned_data['name'], form.cleaned_data['description']))
        except:
            logger.error("Course %s %s didn't create." % (form.cleaned_data['name'], form.cleaned_data['description']))
        return super(CourseCreateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    template_name = 'courses/remove.html'
    model = Course
    success_url = reverse_lazy('courses:list')

    def delete(self, request, *args, **kwargs):
        course_obj =  self.get_object()
        try:
            course_obj.delete()
            logger.info("Course %s %s was removed." % (course_obj.name, course_obj.description))
        except:
            logger.error("Course %s %s didn't remove." % (course_obj.name, course_obj.description))
        return redirect(self.success_url)


