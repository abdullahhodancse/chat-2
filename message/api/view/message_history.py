from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from message.models import Message
from message.api.serializer.message_history import MessageSerializer

class ChatHistoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, room_name):

        messages = Message.objects.filter(room=room_name).order_by('timestamp')

        serializer = MessageSerializer(messages, many=True)

        return Response(serializer.data)