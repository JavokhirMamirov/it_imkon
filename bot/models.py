from django.db import models


# Create your models here.

class Viloyat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tuman(models.Model):
    name = models.CharField(max_length=255)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mahalla(models.Model):
    name = models.CharField(max_length=255)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="game/", null=True, blank=True)
    description = models.TextField()
    file = models.FileField(upload_to="game/", null=True, blank=True)

    def __str__(self):
        return self.name


class Yetakchi(models.Model):
    name = models.CharField(max_length=255)
    chat_id = models.IntegerField(default=0)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    username = models.CharField(max_length=4, null=True)
    password = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    CHOICES = (
        (0, "game"),
        (1, "name"),
        (2, "phone"),
        (3, "mahalla"),
        (4, "uy"),
        (5, "done"),
    )
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=35, null=True)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, null=True)
    uy = models.CharField(max_length=225, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    chat_id = models.IntegerField(default=0)
    status = models.IntegerField(default=0, choices=CHOICES)

    def __str__(self):
        return self.name


