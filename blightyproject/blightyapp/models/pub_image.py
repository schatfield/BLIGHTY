from django.db import models
from .pub import Pub

class PubImage (models.Model):

    pub = models.ForeignKey(Pub, on_delete=models.DO_NOTHING)
    image_path = models.CharField(max_length=255)

    class Meta:
        verbose_name = ("PubImage")
        verbose_name_plural = ("PubImages")

    def __str__(self):
        return self.pub

    def get_absolute_url(self):
        return reverse("PubImage _detail", kwargs={"pk": self.pk})
