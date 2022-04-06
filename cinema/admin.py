from django.contrib import admin
from .models import Cinema, Movie, Ticket

class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('name',)
        }), 
        ('Localização', {
            'fields': ('city', 'street', 'location_number',)
        }), 
        ('Filmes', {
            'fields': ('movies',)
        }) 
    ) 

admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Movie)
admin.site.register(Ticket)
