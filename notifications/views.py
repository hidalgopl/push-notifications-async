from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import NotificationSerializer
from .services import send_push_notification

User = get_user_model()


class TestPushView(CreateAPIView):
    serializer_class = NotificationSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_push_notification(serializer.data)
        return Response(serializer.data)
