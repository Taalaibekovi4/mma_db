from rest_framework import serializers
from .models import Request, Lead, Stage

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    leads = LeadSerializer(many=True, read_only=True)

    class Meta:
        model = Stage
        fields = ['id', 'title', 'order', 'is_final', 'leads']
