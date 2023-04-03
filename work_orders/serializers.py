from rest_framework import serializers
from .models import WorkOrder
from users.serializers import UserSerializer

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'


class WorkOrderListSerializer(serializers.ModelSerializer):

    assigned_to = UserSerializer()
    
    class Meta:
        model = WorkOrder
        fields = ['id', 'site', 'status', 'arrival', 'est_completion', 'assigned_to']
