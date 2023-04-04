from rest_framework import serializers
from .models import WorkOrder
from users.serializers import UserSerializer

class WorkOrderSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer()
    
    class Meta:
        model = WorkOrder
        fields = ['id', 'site','date', 'status', 'arrival', 'est_completion', 'assigned_to', 'description', 'parts_used', 'work_completed', 'work_to_be_completed','work_time_start','work_time_end']


class WorkOrderListSerializer(serializers.ModelSerializer):

    assigned_to = UserSerializer()

    class Meta:
        model = WorkOrder
        fields = ['id', 'site', 'status', 'arrival', 'est_completion', 'assigned_to']
