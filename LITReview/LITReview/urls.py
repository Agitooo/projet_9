"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path

import authentication.views
import review.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        '',
        LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', review.views.home, name='home'),
    path('ticket/add/', review.views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/', review.views.view_ticket, name='view_ticket'),
    path('ticket/<int:ticket_id>/change/', review.views.update_ticket, name='update_ticket'),
    path('ticket/review/add/', review.views.create_review, name='create_review'),
    path('ticket/review/add/<int:ticket_id>', review.views.create_review_from_ticket, name='create_review_from_ticket'),
    path('ticket/<int:ticket_id>/review/<int:review_id>/', review.views.view_review, name='view_review'),
    path('ticket/<int:ticket_id>/review/<int:review_id>/change/', review.views.update_review, name='update_review'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )