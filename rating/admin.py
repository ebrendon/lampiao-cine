from django.contrib import admin
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ('review', 'score')
    
    fieldsets = (
        ('Review', {
            'fields': ('review',)
        }),
        ('Rating', {
            'fields': ('score',)
        }) 
    )   

admin.site.register(Rating, RatingAdmin)
