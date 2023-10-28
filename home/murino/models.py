from django.db import models


class Occupant(models.Model):
    name = models.CharField(max_length=127)
    nickname = models.CharField(max_length=127, default=None)
    page_name = models.CharField(max_length=64, unique=True)
    age = models.IntegerField(default=None)
    date_of_birth = models.DateField(default=None)
    avatar_file = models.FileField(upload_to='files/', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, default=None, null=True)

    def __str__(self):
        return self.page_name


class Hobby(models.Model):
    owner = models.ManyToManyField(Occupant)
    description = models.TextField


class Toy(models.Model):
    name = models.CharField(max_length=127)
    color = models.CharField(max_length=127)


class Items(models.Model):
    name = models.CharField(max_length=127)
