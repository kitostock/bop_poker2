from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'customer_id', 'current_period_end')
        # extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user

