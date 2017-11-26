# Push notifications boilerplate.
This is minimalistic setup for sending asynchronous push notifications in django using django-rest-framework.
Components used:
- [celery](https://github.com/celery/celery)
- [django](https://github.com/django/django)
- [django-push-notifications](https://github.com/django-push-notifications/django-push-notifications)
- [django-rest-framework](https://github.com/encode/django-rest-framework)
- [docker-compose](https://docs.docker.com/compose/)
- [redis](https://redis.io/)

## How to run
If you have docker and docker-compose installed, simply go to the project main directory and type `docker-compose up -d`.
Project is now running on port 400 on your localhost. Go to the http://localhost:4000/notifications/test/ to send test push.


## Usage
Main advantage of this setup is sending push notifications to all user's devices asynchronously.
First, read the docs of django-push-notifications package to know how to register user's device. 
Then you can use `push_to_all_devices` task to push notification to all user's devices.

Example:
`views.py`
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

from notifications.tasks import push_to_all_devices


@api_view(['POST'])
def send_test_push(request):
    receiver_id = request.POST.data['receiver_id']
    message = request.POST.data['message']
    push_to_all_devices.delay(message, receiver_id)
    return Response(data={'info': 'Push notification sent.'})

```
```python
from django.conf.urls import include, url
from django.contrib import admin

from .views import send_test_push

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notifications/', send_test_push, name='test-push'),
]

```
