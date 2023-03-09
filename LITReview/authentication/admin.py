from django.contrib import admin, messages
from django.contrib.admin import register, display, action

from review.models import Ticket, Review
from authentication.models import UserFollows


@register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    pass


@register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'time_created', 'ticket_str']
    list_filter = ['user', 'title', 'time_created']
    search_fields = ['user', 'title', 'description', 'time_created']
    fields = ['user', 'title', 'description', 'time_created']
    readonly_fields = ['time_created']
    actions = ['test_action']

    @display(description="Ticket")
    def ticket_str(self, obj):
        return str(obj)

    @action(description="Tester une action")
    def test_action(self, request, queryset):
        if not queryset:
            self.message_user(request, "Veuillez sélectionner un élément", level=messages.ERROR)
        else:
            self.message_user(request, f"Vous avez sélectionné {queryset.count()}", level=messages.SUCCESS)


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
