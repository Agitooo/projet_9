from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Value, CharField
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review
from itertools import chain


@login_required
def home(request):
    # tickets = Ticket.objects.all()
    tickets = Ticket.objects.filter(user__pk__in=[u.followed_user.pk for u in request.user.following.all()])
    tickets = tickets.annotate(content_type=Value('Ticket', CharField()))

    my_tickets = Ticket.objects.filter(user=request.user)
    my_tickets = my_tickets.annotate(content_type=Value('Ticket', CharField()))

    # reviews = Review.objects.all()
    reviews = Review.objects.filter(user__in=[u.pk for u in request.user.following.all()])
    reviews = reviews.annotate(content_type=Value('Review', CharField()))

    my_reviews = Review.objects.filter(user=request.user)
    my_reviews = my_reviews.annotate(content_type=Value('Review', CharField()))

    liste_postes = sorted(
        chain(reviews, tickets, my_reviews, my_tickets),
        key=lambda
        poste: poste.time_created,
        reverse=True
    )

    postes = None
    if liste_postes:
        paginator = Paginator(liste_postes, 20)
        page = request.GET.get('page')
        postes = paginator.get_page(page)

    context = {
        'tickets': tickets,
        'reviews': reviews,
        'postes': postes,
    }

    return render(request, 'review/home.html', context)


@login_required
def create_ticket(request):
    ticket_form = TicketForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'review/create_ticket.html', context={'ticket_form': ticket_form})


@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES, instance=ticket)
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect('home')
    else:
        ticket_form = TicketForm(instance=ticket)
    return render(request, 'review/update_ticket.html', context={'ticket_form': ticket_form})


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'review/view_ticket.html', {'ticket': ticket})


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket.user == request.user:
        ticket.delete()
        messages.success(request, "Votre ticket a été supprimé")
    else:
        messages.error(request, "Vous ne pouvez pas supprimer ce ticket")
        return render(request, 'review/view_ticket.html', {'ticket': ticket})
    return redirect('home')


@login_required
def create_review(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid() and ticket_form.is_valid():
            # On enregistre le ticket, car il en faut un pour faire une critique
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            # Puis on save la critique en ajoutant el ticket
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'review/create_review.html', context)


@login_required
def create_review_from_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(request, 'review/create_review_from_ticket.html', context)


@login_required
def view_review(request, ticket_id, review_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    review = get_object_or_404(Review, id=review_id)
    context = {
        'ticket': ticket,
        'review': review,
    }
    return render(request, 'review/view_review.html', context)


@login_required
def update_review(request, ticket_id, review_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('home')
    else:
        review_form = ReviewForm(instance=review)

    context = {
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(request, 'review/update_review.html', context)


@login_required
def delete_review(request, ticket_id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user == request.user:
        review.delete()
        messages.success(request, "Votre Critique a été supprimé")
    else:
        messages.error(request, "Vous ne pouvez pas supprimer cette critique")
    return redirect('home')
