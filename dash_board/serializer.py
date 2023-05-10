from rest_framework import serializers
from .models import Dashboard


class DashboardGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ('id', 'title', 'image', 'text')


class DashboardPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ('id', 'title', 'image', 'text')
