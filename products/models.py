from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100) #blank(Used in forms), null(used for ur db)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=45.78)
    sale_price = models.DecimalField(decimal_places=2, max_digits=10, default=28.70)
    slug = models.SlugField(unique=True)  # this is a url..stroes a string value..
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
   # photo = models.ImageField(null=True,default="image.png")
    def __str__(self):
        return f"{self.title}"
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'slug':self.slug})

class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class Framework(models.Model):
    name = models.CharField(max_length=15)
    # if we delete the Language, its going to delete all frameworks..
    language = models.ForeignKey(Language, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Movie(models.Model):
    name = models.CharField(max_length=34)

    def __str__(self):
        return f"{self.name}"
class Character(models.Model):
    name = models.CharField(max_length=25)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f"{self.name}"

class Forum(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=64)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=5)
    check_me_out = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"

class DemoPic(models.Model):
    photo = models.ImageField()

    class Meta:
        verbose_name_plural = "Profile_photo"

    def __str__(self):
        return f"{self.photo.name}"
