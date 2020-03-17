from django.db import models 
from django.urls import reverse
from .patron import Patron
from .pub import Pub


class PatronPub (models.Model):    
    patron = models.ForeignKey(Patron, on_delete=models.DO_NOTHING)
    pub = models.ForeignKey(Pub, on_delete=models.DO_NOTHING)
    is_wished = models.BooleanField(default=False)
    is_visited = models.BooleanField(default=False)
    has_experience = models.BooleanField(default=False)
    beers_tried = models.CharField(max_length=55)
    food_ate = models.CharField(max_length=85)
    experience = models.CharField(max_length=3000)


    # librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("patron_pub")
        verbose_name_plural = ("patron_pubs")

    def __str__(self):
        return self.Pub.name
        # if I wanted to return the pub name that was a Patron's pub, does that make sense and if so is this close to how one would do that?

    def get_absolute_url(self):
        return reverse("PatronPub_detail", kwargs={"pk": self.pk})

        # what exactly is this doing? "absolute_url"






