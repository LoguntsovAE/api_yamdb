from rest_framework import serializers

from User.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email', 'bio', 'first_name', 'last_name')
        model = User
