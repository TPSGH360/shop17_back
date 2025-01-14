from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=False
    )

    class Meta:
        model = Product
        fields = ["id", "name", "price", "image", "type", "manufacturer", "in_stock"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Get the token object
        token = super().get_token(user)

        # Add custom claims to the token payload
        token["username"] = user.username
        token["is_admin"] = (
            user.is_staff
        )  # Assuming 'is_admin' corresponds to `is_staff`

        return token
