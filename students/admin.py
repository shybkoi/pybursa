from django.contrib import admin
from students.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    #item view
    radio_fields = {'package': admin.HORIZONTAL}
    #list view
    list_display = ['name', 'surname', 'package']
    date_hierarchy = 'date_of_birth'
    list_display_links = ['name', 'surname', 'package']
    ordering = ['name', 'surname', 'package']
    list_per_page = 20
    list_filter = ['name', 'surname', 'package', 'course__technology']
    search_fields = ['name', 'surname', 'package', 'email',
                     'course__technology']
