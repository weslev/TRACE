from rest_framework import serializers
from kickstarterAPI.models import Kickstarter

class KickstarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kickstarter
        fields = ['id', 'backers_count', 'name']