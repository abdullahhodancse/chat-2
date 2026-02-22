from rest_framework import serializers
from message.models import Message

class MessageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='sender.email')

    class Meta:
        model = Message
        fields = ['id','username','content','timestamp']