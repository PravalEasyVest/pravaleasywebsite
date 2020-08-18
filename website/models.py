from django.db import models
from django.utils import timezone
from django.conf import settings


class SignUp(models.Model):
    email = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    contact_no = models.CharField(max_length=200,null=True)
    drop_us_a_line = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name