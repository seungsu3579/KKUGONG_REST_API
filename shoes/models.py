from django.db import models
from users.models import User


class Shoes(models.Model):

    id = models.CharField(max_length=15, primary_key=True)
    brand = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    item_url = models.CharField(max_length=150)


class UserShoes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="userShoes", null=True
    )
    vector = models.BinaryField(max_length=250, null=True)
    img = models.ImageField(upload_to="userShoes")
    meta_shoes = models.ForeignKey(
        Shoes, on_delete=models.SET_NULL, related_name="similarThings", null=True,
    )


class ShoesImage(models.Model):

    id = models.CharField(max_length=15, primary_key=True)
    img_url = models.CharField(max_length=150)
    img = models.ImageField(upload_to="shoes")
    vector = models.BinaryField(max_length=250)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name="images")
