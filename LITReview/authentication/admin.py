from django.contrib import admin
from django.contrib.admin import register

from review.models import Ticket, Review


@register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
#     list_display = ['user', 'titre', 'contenu', 'date_creation']
#     list_filter = ['user', 'titre', 'date_creation']
#     search_fields = ['user', 'titre', 'contenu', 'date_creation']
#     # fields = ['auteur', 'titre', 'contenu', 'date_creation']
#     readonly_fields = ['date_creation']


@register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
    # list_display = ['auteur', 'titre', 'vote', 'contenu', 'date_creation']
    # list_filter = ['auteur', 'titre', 'vote', 'contenu', 'date_creation']
    # search_fields = ['auteur', 'titre', 'vote', 'contenu', 'date_creation']
    # # fields = ['auteur', 'titre', 'vote', 'contenu', 'date_creation']
    # readonly_fields = ['date_creation']


# admin.site.register(Ticket, TicketAdmin)
# admin.site.register(Review, ReviewAdmin)
