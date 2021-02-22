from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from User.models import User


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=User.Role)
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
            ),
        ],
    )
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
            ),
        ],
    )

    class Meta:
        model = User

        fields = (
            'id', 'username', 'email', 'bio', 'first_name', 'last_name', 'role'
        )


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class SentJWTTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)
