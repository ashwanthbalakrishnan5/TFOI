from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import BoothData2019, BoothData2014


class SuperAdminUserCreateSerializer(UserCreateSerializer):
    # class Meta(UserCreateSerializer.Meta):
    #     model = get_user_model()
    #     fields = ('id', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        request = self.context.get("request")
        if not request.user.is_superuser:
            raise serializers.ValidationError("Only superadmins can create users.")

        return super().create(validated_data)


class BoothData2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = BoothData2019
        fields = "__all__"


class BoothData2014Serializer(serializers.ModelSerializer):
    class Meta:
        model = BoothData2014
        fields = "__all__"
