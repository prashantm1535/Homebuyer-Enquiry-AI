from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','city','age','income','booked','interested','created_at')
    list_filter = ('city','property_type','booked','interested')
    search_fields = ('name','city')
