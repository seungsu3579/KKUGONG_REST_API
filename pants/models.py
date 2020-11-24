from django.db import models
from users.models import User


class Pants(models.Model):

    id = models.CharField(max_length=15, primary_key=True)
    brand = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    item_url = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)


class UserPants(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50, default=f"pants")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="userPants", null=True
    )
    vector = models.BinaryField(max_length=250, null=True)
    img = models.ImageField(upload_to="userPants")
    meta_pants = models.ForeignKey(
        Pants, on_delete=models.SET_NULL, related_name="similarThings", null=True,
    )
    jjim = models.BooleanField(default=False)


class PantsImage(models.Model):

    id = models.CharField(max_length=15, primary_key=True)
    img_url = models.CharField(max_length=150)
    img = models.ImageField(upload_to="pants")
    vector = models.BinaryField(max_length=250)
    pants = models.ForeignKey(Pants, on_delete=models.CASCADE, related_name="images")
