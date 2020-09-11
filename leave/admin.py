from django.contrib import admin
from .models import Profile, Leave
from import_export.admin import ImportExportModelAdmin

#Customizing Contact Model in Admin Site
class LeaveAdmin(ImportExportModelAdmin):
    list_display = ('full_name', 'leaves_avai', 'start_date', 'end_date', 'total')
    list_display_links = ('full_name',)
    #list_editable = ('info',)
    list_per_page = 10
    search_fields = ('full_name',)
    list_filter = ('approval',)
# Register your models here.
admin.site.register(Profile)
admin.site.register(Leave, LeaveAdmin)