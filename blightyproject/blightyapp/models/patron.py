from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#  Note how this is different from the original Libray app Librarian Model. No post_save stuff going on. Since we want to use some of the form data to create a Librarian when a new user registers, we will handle making a librarian in the register view.

class Patron (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Patron")
        verbose_name_plural = ("Patrons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Patron _detail", kwargs={"pk": self.pk})



# # These receiver hooks allow you to continue to
# # work with the `User` class in your Python code.


# # Every time a `User` is created, a matching `Librarian`
# # object will be created and attached as a one-to-one
# # property
# @receiver(post_save, sender=User)
# def create_patron(sender, instance, created, **kwargs):
#     if created:
#         Patron.objects.create(user=instance)

# # Every time a `User` is saved, its matching `Librarian`
# # object will be saved.
# @receiver(post_save, sender=User)
# def save_patron(sender, instance, **kwargs):
#     instance.patron.save()