from rest_framework import serializers

from api_users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'username', 'email', 'bio', 'first_name', 'last_name',
            'role', 'is_staff'
        )
        model = User
