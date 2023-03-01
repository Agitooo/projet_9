from django import forms
from .models import Ticket, Review


VOTE_LIST = [('1', '1 étoile'), ('2', '2 étoiles'), ('3', '3 étoiles'), ('4', '4 étoiles'), ('5', '5 étoiles')]


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):

    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=VOTE_LIST, label='Vote')

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
