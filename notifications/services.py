from .tasks import push_to_all_devices


def send_push_notification(data):
    receiver = data.get('receiver', None)
    message = data.get('title', None)
    if receiver:
        push_to_all_devices.delay(message, receiver)
