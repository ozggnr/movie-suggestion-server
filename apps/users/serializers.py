from apps.users.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # metadata describing the model
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_active')
