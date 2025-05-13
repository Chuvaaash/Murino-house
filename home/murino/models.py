from django.db import models


class Hobby(models.Model):
    name = models.CharField(max_length=127, default=None)
    description = models.TextField(default=None, null=True)

    def __str__(self):
        return self.name


class Occupant(models.Model):
    name = models.CharField(max_length=127)
    nickname = models.CharField(max_length=127, default=None)
    page_name = models.CharField(max_length=64, unique=True)
    age = models.IntegerField(default=None)
    date_of_birth = models.DateField(default=None)
    avatar_file = models.FileField(upload_to='files/', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, default=None, null=True)
    hobbies = models.ManyToManyField(Hobby, related_name='hobbies')

    def interact(self):
        introduction = ""
        if self.page_name == "Kapibara" or self.page_name == "kapibara":
            age = self.age
            introduction = "Hi! My name is Andriyake a I am " + str(self.age) + " years old\nА ты шо тут делаешь? о_О"
        else:
            introduction = "Данный персонаж еще не умеет взаимодействовать"
        return introduction

    def __str__(self):
        return self.page_name


class KissTransaction(models.Model):
    REQUESTED = "REQD"
    APPROVED = "APPD"
    DECLINED = "DCLD"
    KISS_TRANSACTION_STATUSES = [
        (REQUESTED, "Requested"),
        (APPROVED, "Approved"),
        (DECLINED, "Declined")
    ]
    requested_by = models.ForeignKey(Occupant, null=True, on_delete=models.SET_NULL)
    number_of_kisses = models.IntegerField()
    request_date = models.DateField()
    kiss_transaction_status = models.CharField(
        max_length=4,
        choices=KISS_TRANSACTION_STATUSES,
        default=DECLINED
    )


"""
    KISS_TRANSACTION_STATUSES = {
        "Requested",
        "Approved",
        "Declined",
    }
"""

"""
class Toy(models.Model):
    name = models.CharField(max_length=127)
    color = models.CharField(max_length=127)


class Items(models.Model):
    name = models.CharField(max_length=127)
"""