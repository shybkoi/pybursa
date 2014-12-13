from django.contrib import admin
from courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    #item view
    radio_fields = {'technology': admin.HORIZONTAL}
    prepopulated_fields = {"slug": ("name",)}
    #list view
    list_display = ['name', 'technology', 'teacher', 'start_date', 'finish_date']
    date_hierarchy = 'start_date'
    list_display_links = ['technology', 'teacher', 'start_date', 'finish_date']
    ordering = ['name', 'technology', 'start_date', 'finish_date']
    list_per_page = 20
    list_filter = ['technology', 'teacher', 'start_date', 'finish_date']
    search_fields = ['name', 'technology', 'teacher__surname']
    list_editable = ['name']
