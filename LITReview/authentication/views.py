from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate  # import des fonctions login et authenticate
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import IntegrityError
from .models import UserFollows

from . import forms


class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})


def signup_page(request):
    form = forms.ReviewUserCreationForm()
    if request.method == 'POST':
        form = forms.ReviewUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})


@login_required
# def follow_user(request, user_id):
def follow_user(request):
    # On récupère l'utilisateur saisi
    # user_to_follow = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user_to_follow = get_object_or_404(User, username=request.POST['user_to_follow'])
        if user_to_follow != request.user:
            try:
                UserFollows.objects.create(user=request.user, followed_user=user_to_follow)
                messages.success(request, f"Vous suivez maintenant {request.POST['user_to_follow']}")
            except IntegrityError:
                # On vérifie qu'il ne suit pas déjà le user saisi
                messages.error(request, f"Vous suivez déjà {request.POST['user_to_follow']}")
        else:
            # L'utilisateur ne peut pas se suivre lui meme
            messages.error(request, f"Vous ne pouvez pas vous suivre")

    # On récupère la liste des utilisateurs suivis du user connecté
    followed_user_list = request.user.following.all()
    followed_by_user_list = request.user.followed_by.all()

    context = {
        'followed_user_list': followed_user_list,
        'followed_by_user_list': followed_by_user_list
    }
    return render(request, 'authentication/manage_follow.html', context)


@login_required
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = get_object_or_404(User, id=user_id)
        # if user_to_unfollow != request.user:
        try:
            user_follow = get_object_or_404(UserFollows, user=request.user, followed_user=user_to_unfollow)
            user_follow.delete()
            messages.success(request, f"Vous ne suivez plus {user_to_unfollow.username}")
        except IntegrityError:
            # On vérifie qu'il ne suit pas déjà le user saisi
            messages.error(request, f"Utilisateur introuvable dans la liste des utilisateurs suivi")
    except User.DoesNotExist:
        # Pas de correspondance entre la saisie et un utilisateur connu
        messages.error(request, f"L'utilisateur {user_id} est introuvable")
    return redirect('follow_user')
