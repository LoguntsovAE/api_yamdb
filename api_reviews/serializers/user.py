from rest_framework import serializers

from User.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = User
