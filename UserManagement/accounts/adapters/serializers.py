from rest_framework import serializers
from ..domain.models import UserProfile, InstructorRate


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'identity_id', 'email', 'full_name', 'date_of_birth', 'is_active']
        extra_kwargs = {
            'identity_id': {'read_only': True},  # Make 'identity_id' read-only after creation
        }


class InstructorRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorRate
        fields = '__all__'
        extra_kwargs = {
            'rate_date_created': {'read_only': True},  # Make 'email' read-only after creation
        }

