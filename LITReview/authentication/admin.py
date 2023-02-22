from django.contrib import admin
from review.models import Ticket, Review


class TicketAdmin(admin.ModelAdmin):
    list_display = ['auteur', 'titre', 'contenu', 'date_creation']
    list_filter = ['auteur', 'titre', 'date_creation']
    search_fields = ['auteur', 'titre', 'contenu', 'date_creation']
    # fields = ['auteur', 'titre', 'contenu', 'date_creation']
    readonly_fields = ['date_creation']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['auteur', 'titre', 'vote', 'contenu', 'date_creation']
    list_filter = ['auteur', 'titre', 'vote', 'contenu', 'date_creation']
    search_fields = ['auteur', 'titre', 'vote', 'contenu', 'date_creation']
    # fields = ['auteur', 'titre', 'vote', 'contenu', 'date_creation']
    readonly_fields = ['date_creation']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
