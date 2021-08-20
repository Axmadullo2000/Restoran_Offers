from django.db import models
from django.db.models import Model


class CarouselContent(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=80)
    image = models.FileField(upload_to='img/upload/', default=None)

    def __str__(self):
        return self.title


class BestBurger(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=80)
    price = models.IntegerField()
    image = models.FileField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title


class PresidentBurger(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=80)
    price = models.IntegerField()
    image = models.FileField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title


class HamburgerClient(models.Model):
    comment = models.CharField(max_length=400)
    image = models.FileField(upload_to='img/upload/', default=None)
    author = models.CharField(max_length=80)
    SCORE_CHOICES = zip(range(1, 6), range(1, 6))
    grade = models.IntegerField(choices=SCORE_CHOICES, blank=True)

    def __str__(self):
        return self.comment


class OurGallery(models.Model):
    title = models.CharField(max_length=60)
    image = models.FileField(upload_to='img/burgers/', default=None)


class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=1200)
    author = models.CharField(max_length=80)
    comments = models.IntegerField(default=0)
    image = models.FileField(upload_to='img/burgers/', default=None)
    day = models.DateField()

    def printDay(self):
        return self.day.strftime('%d')

    def printMonth(self):
        return self.day.strftime('%b')


class SingleBlog(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=400)
    author = models.CharField(max_length=80)
    comments = models.IntegerField(default=0)
    image = models.FileField(upload_to='img/burgers/', default=None)


class GalleryImage(models.Model):
    title = models.CharField(max_length=300)
    image = models.FileField(upload_to='img/burgers/', default=None)


class getInTouch(models.Model):
    message = models.CharField(max_length=512)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=150)
