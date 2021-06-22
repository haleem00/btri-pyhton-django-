from django.contrib import admin
from .models import Contact

# Register your models here.

class contactAdmin (admin.ModelAdmin):
    list_display = ('listing_id',"name",'listing','contact_date','email', )
    list_display_links= ('listing_id','name')
    search_fields = ('name','listing','email')
    list_per_page= 25



admin.site.register(Contact,contactAdmin)


