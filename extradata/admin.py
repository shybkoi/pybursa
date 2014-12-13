from django.contrib import admin
from extradata.models import Address, Dossier


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    #list view
    list_display = ['country', 'zip_code', 'city', 'street', 'building']
    list_display_links = ['country', 'city', 'street']
    ordering = ['country', 'city', 'street']
    list_per_page = 20
    list_filter = ['country', 'zip_code', 'city', 'street', 'building']
    search_fields = ['country', 'zip_code', 'city', 'street', 'building']


@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    #item view
    filter_horizontal = ['unliked_courses']
    #list view
    list_display = ['adress', 'favorite_color']
    list_display_links = ['adress', 'favorite_color']
    ordering = ['adress', 'favorite_color']
    list_per_page = 20
    list_filter = ['adress__country', 'adress__city', 'adress__street',
                   'unliked_courses__technology', 'favorite_color']
    search_fields = ['adress__country', 'adress__city', 'adress__street',
                     'unliked_courses__technology', 'favorite_color']
