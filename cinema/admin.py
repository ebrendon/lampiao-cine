from django.contrib import admin
from .models import Cinema, Movie, Ticket
# Register your models here.

admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Ticket)
