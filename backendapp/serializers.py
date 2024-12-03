from rest_framework import serializers
from .models import Businessregister

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businessregister
        fields = ['business_name', 'phone', 'address', 'workspace_name']
