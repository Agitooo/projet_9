from django.conf import settings
from django.db import models


class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')
    objects = models.Manager()

    class Meta:
        unique_together = ('user', 'followed_user')
        verbose_name = "utilisateur suivi"
        verbose_name_plural = "utilisateurs suivis"

    def __str__(self):
        return f"{self.user.username} => {self.followed_user.username}"
