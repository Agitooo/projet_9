from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titre', 'contenu', 'photo']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        contenu = forms.CharField(widget=forms.Textarea)
        vote_list = [('1', '1 étoile'), ('2', '2 étoiles'), ('3', '3 étoiles'), ('4', '4 étoiles'), ('5', '5 étoiles')]
        vote = forms.ChoiceField(widget=forms.RadioSelect(choices=vote_list))
        fields = ['titre', 'vote', 'contenu']
