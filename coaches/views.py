from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView, DeleteView)
from django import forms
from coaches.models import Coach
from courses.models import Course


class CoachModelForm(forms.ModelForm):
    class Meta:
        model = Coach


class CoachListView(ListView):
    model = Coach
    template_name = 'coaches/list.html'
    context_object_name = 'coaches'


class CoachDetailView(DetailView):
    model = Coach
    template_name = 'coaches/item.html'
    context_object_name = 'coach'

    def get_context_data(self, **kwargs):
        context = super(CoachDetailView, self).get_context_data(**kwargs)
        try:
            course = Course.objects.get(teacher=int(kwargs['object'].id))
        except:
            course = None
        context['course'] = course
        return context


class CoachUpdateView(UpdateView):
    model = Coach
    template_name = 'coaches/edit.html'
    success_url = reverse_lazy('coaches:list')
    context_object_name = 'coach'


class CoachCreateView(CreateView):
    model = Coach
    template_name = 'coaches/edit.html'
    form_class = CoachModelForm
    success_url = reverse_lazy('coaches:list')
    context_object_name = 'coach'


class CoachDeleteView(DeleteView):
    template_name = 'coaches/remove.html'
    model = Coach
    success_url = reverse_lazy('coaches:list')
