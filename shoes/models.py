from django.db import models


class Shoes(models.Model):

    _id = models.CharField(max_length=15, primary_key=True)
    brand = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    item_url = models.CharField(max_length=150)


class ShoesImage(models.Model):

    _id = models.CharField(max_length=15, primary_key=True)
    img_url = models.CharField(max_length=150)
    img_dir = models.CharField(max_length=150)
    vector = models.BinaryField(max_length=250)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name="images")
