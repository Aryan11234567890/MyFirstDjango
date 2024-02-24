from rest_framework.serializers import ModelSerializer 
from basicapp.models import Room

class RoomSerial(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'