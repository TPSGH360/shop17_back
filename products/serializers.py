from rest_framework import serializers
from .models import Product, Cart
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username  # Add username
        token["email"] = user.email  # Add email if needed

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username  # Include username in response
        return data


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=False
    )

    class Meta:
        model = Product
        fields = ["id", "name", "price", "image", "type", "manufacturer", "in_stock"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "items"]
        read_only_fields = ["user"]

    def validate_items(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Items must be a list.")
        for item in value:
            required_keys = ["id", "name", "price", "quantity", "image"]
            if not all(key in item for key in required_keys):
                raise serializers.ValidationError(
                    f"Each item must include {', '.join(required_keys)}."
                )
        return value

    def update(self, instance, validated_data):

        instance.items = validated_data.get("items", [])
        instance.save()
        return instance
