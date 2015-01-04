from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django import forms
from django.contrib import messages
from courses.models import Course
from coaches.models import Coach
from students.models import Student
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _



class ComplaintForm(forms.Form):
    theme = forms.CharField(label=_("Theme"), max_length=255)
    coach = forms.ModelChoiceField(label=_("Coach"), queryset=Coach.objects.all(),)
    student = forms.ModelChoiceField(label=_("Guilty"), queryset=Student.objects.all(),)
    body = forms.CharField(label=_("Complaint text"), widget=forms.Textarea)
    email = forms.EmailField()


class ComplaintView(FormView):
    template_name = 'complaint.html'
    form_class = ComplaintForm
    success_url = reverse_lazy('complaint')

    def form_valid(self, form):
        print dir(self)
        theme = form.cleaned_data['theme']
        coach = form.cleaned_data['coach']
        student = form.cleaned_data['student']
        course = student.course.name
        print course
        body = form.cleaned_data['body']
        email = form.cleaned_data['email']
        rendered = render_to_string('complaint_body.html',
         {'coach_name': coach.name, 'coach_surname': coach.surname,
          'student_surname': student.surname, 'course': course,
          'body_complaint': body})
        try:
            send_mail(theme, rendered, email, ['heap_@bla.com'])
            messages.success(self.request, _("Complaint was sent."))
        except:
            messages.error(self.request, _("Connection error. Try later."))
        return redirect(self.get_success_url())

