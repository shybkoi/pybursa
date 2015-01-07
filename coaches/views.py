from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView, DeleteView)
from django import forms
from coaches.models import Coach
from courses.models import Course

import logging
logger = logging.getLogger(__name__)


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

    def form_valid(self, form):
        try:
            form.save()
            logger.info("Coach %s %s was updated." % (form.cleaned_data['name'], form.cleaned_data['surname']))
        except:
            logger.error("Coach %s %s didn't update." % (form.cleaned_data['name'], form.cleaned_data['surname']))
        return super(CoachUpdateView, self).form_valid(form)


class CoachCreateView(CreateView):
    model = Coach
    template_name = 'coaches/edit.html'
    form_class = CoachModelForm
    success_url = reverse_lazy('coaches:list')
    context_object_name = 'coach'

    def form_valid(self, form):
        try:
            form.save()
            logger.info("Coach %s %s was add." % (form.cleaned_data['name'], form.cleaned_data['surname']))
        except:
            logger.error("Coach %s %s didn't add." % (form.cleaned_data['name'], form.cleaned_data['surname']))
        return super(CoachCreateView, self).form_valid(form)


class CoachDeleteView(DeleteView):
    template_name = 'coaches/remove.html'
    model = Coach
    success_url = reverse_lazy('coaches:list')

    def delete(self, request, *args, **kwargs):
        coach_obj =  self.get_object()
        try:
            coach_obj.delete()
            logger.info("Coach %s %s was removed." % (coach_obj.name, coach_obj.surname))
        except:
            logger.error("Coach %s %s didn't remove." % (coach_obj.name, coach_obj.surname))
        return redirect(self.success_url)
