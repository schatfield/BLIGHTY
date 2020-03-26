from django.db import models

class Region (models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    image_path = models.CharField(max_length=255)
    

    class Meta:
        verbose_name = ("Region")
        verbose_name_plural = ("Regions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Region _detail", kwargs={"pk": self.pk})
