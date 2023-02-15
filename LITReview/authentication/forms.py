from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from django import forms
from django.contrib.auth.models import User


class ReviewUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password = forms.CharField(
        label='Mot de passe',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    confirm_password = forms.CharField(
        label='Confirmer Mot de passe',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model = User
        fields = ("username",)
        # field_classes = {"username": UsernameField}
        help_texts = {"username": None}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("confirm_password")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("confirm_password", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


# class SignupForm(forms.ModelForm):
#     username = forms.CharField(max_length=63, label='Nom d’utilisateur')
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
#     confirm_password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Confirmer Mot de passe')
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'confirm_password')
#
#     def clean(self):
#         cleaned_data = super(SignupForm, self).clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if password != confirm_password:
#             raise forms.ValidationError(
#                 "Les mots de passe saisis sont différents"
#             )
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user
