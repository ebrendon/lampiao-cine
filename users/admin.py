from django.contrib import admin
from .models import User
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastName')
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('name', 'lastName', 'birthDate',)
        }),
        ('Contato', {
            'fields': ('phone',)
        }) ,
        ('Localização', {
            'fields': ('city', 'country',)
        }) 
    )

admin.site.register(Profile, ProfileAdmin)
