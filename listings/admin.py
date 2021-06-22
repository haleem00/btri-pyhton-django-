from django.contrib import admin
from .models import Listing

# Register your models here.

class adminArea(admin.ModelAdmin): ## to sort and arange your database tables in admin area
    list_display = ("id", "title", "is_published", "price", "list_date", "realtor" ) # to display these tables outside
    list_display_links = ("id", "title") # to make it clickable
    list_filter = ("realtor",) 
    list_editable = ("is_published",) # you can edit this table
    search_fields = ("title", "discription", "price", "state", "city", )

admin.site.register(Listing, adminArea)
