from django.contrib import admin
from review.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ['auteur', 'titre', 'contenu', 'date_creation']
    list_filter = ['auteur', 'titre', 'date_creation']
    search_fields = ['auteur', 'titre', 'contenu', 'date_creation']


admin.site.register(Ticket, TicketAdmin)
