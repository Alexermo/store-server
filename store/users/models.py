from django.db import models

from django.core.mail import send_mail

from django.conf import settings

from django.urls import reverse

from django.utils.timezone import now

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'email verification object for {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={
                       'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учетной записи для {self.user.username}'
        html_message = 'Для подтверждения учетной записи для {} перейдите по <a href="{}">ссылке</a>'.format(
            self.user.email, verification_link)
        message = 'Для подтверждения учетной записи для {} перейдите по ссылке: {}'.format(
            self.user.email, verification_link)

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
            html_message=html_message,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False
