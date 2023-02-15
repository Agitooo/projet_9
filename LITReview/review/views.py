from django.shortcuts import redirect, render, get_object_or_404
from . import forms
from . import models


def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'review/home.html', context={'tickets': tickets})


def create_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.auteur = request.user
            ticket.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
    }
    return render(request, 'review/create_ticket.html', context=context)


def update_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect('home')
    else:
        ticket_form = forms.TicketForm(instance=ticket)
    return render(request, 'review/update_ticket.html', context={'ticket_form': ticket_form})


def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    print(ticket)
    return render(request, 'review/view_ticket.html', {'ticket': ticket})
