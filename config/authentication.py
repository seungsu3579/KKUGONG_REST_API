import jwt
from rest_framework import authentication
from django.conf import settings
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                return None
            else:
                version, jwt_token = token.split(" ")
                decoded_token = jwt.decode(
                    jwt_token, settings.SECRET_KEY, algorithms=["HS256"]
                )
                pk = decoded_token.get("pk")
                user = User.objects.get(pk=pk)
                return (user, None)

        except (ValueError, jwt.exceptions.DecodeError, User.DoesNotExist):
            return None
