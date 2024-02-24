from rest_framework.decorators import api_view 
from rest_framework.response import Response
from basicapp.models import Room
from .serializers import RoomSerial

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms', 
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serial = RoomSerial(rooms, many = True)
    return Response(serial.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id = pk)
    serial = RoomSerial(room, many = False)
    return Response(serial.data)