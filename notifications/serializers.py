from rest_framework import serializers


class NotificationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    receiver = serializers.IntegerField()
