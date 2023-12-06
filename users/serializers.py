from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'telegram_id', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            phone=validated_data['phone'],
            telegram_id=validated_data['telegram_id'],
        )
        # шифрование пароля
        user.set_password(validated_data['password'])
        user.save()
        return user