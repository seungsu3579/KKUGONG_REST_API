from rest_framework import serializers
from .models import Tops, TopsImage, UserTops


class TopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopsImage
        fields = (
            "id",
            "img_url",
            "img",
            "top",
        )

        read_only_fields = (
            "id",
            "img_url",
            "img",
            "top",
        )


class TopsSerializer(serializers.ModelSerializer):
    images = TopImageSerializer(many=True, read_only=True)

    class Meta:
        model = Tops
        fields = (
            "id",
            "brand",
            "product",
            "item_url",
            "images",
        )

        read_only_fields = (
            "id",
            "brand",
            "product",
            "item_url",
            "images",
        )


class UserTopsSerializer(serializers.ModelSerializer):
    meta_top = TopsSerializer(read_only=True)

    class Meta:
        model = UserTops
        fields = (
            "id",
            "nickname",
            "user",
            "img",
            "meta_top",
            "jjim",
        )

        read_only_fields = (
            "id",
            "nickname",
            "user",
            "img",
            "meta_top",
            "jjim",
        )


class UserTopsImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTops
        fields = (
            "id",
            "img",
        )

        read_only_fields = (
            "id",
            "img",
        )

