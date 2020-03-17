from django.db import models
from .region import Region

class Pub (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    address = models.CharField(max_length=300)
    website = models.CharField(max_length=200)
    image_path = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Pub")
        verbose_name_plural = ("Pubs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Pub _detail", kwargs={"pk": self.pk})
