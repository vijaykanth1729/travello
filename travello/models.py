from django.db import models

class Tourisam(models.Model):
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    city_pic = models.ImageField(default="")

    def __str__(self):
        return f"mycity, {self.city}"
