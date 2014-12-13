from django.contrib import admin
from coaches.models import Coach


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    radio_fields = {'position': admin.HORIZONTAL}
    #list view
    list_display = ['name', 'surname', 'position']
    list_display_links = ['name', 'surname', 'position']
    ordering = ['name', 'surname', 'position']
    list_per_page = 20
    list_filter = ['name', 'surname', 'position', 'user__username']
    search_fields = ['name', 'surname', 'position', 'email']
