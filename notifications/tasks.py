from __future__ import absolute_import, unicode_literals

from django.contrib.auth import get_user_model

from celery.utils.log import get_task_logger
from push_notifications.models import APNSDevice, APNSDeviceQuerySet, GCMDevice, GCMDeviceQuerySet

from settings.celery import app

logger = get_task_logger(__name__)
User = get_user_model()


def get_user_devices(user):
    """
    Function used to fetch receiver's iOS and Android devices.
    :param user:
    :return:
    """
    if isinstance(user, int):
        apns_devices = APNSDevice.objects.filter(user_id=user)
        fcm_devices = GCMDevice.objects.filter(user_id=user)
        return apns_devices, fcm_devices
    else:
        raise TypeError('Function argument is not a User instance!')


@app.task
def push_to_all_devices(message, user_id, extra_dict={}):
    """
    Function used to push notifications to receiver's devices.
    :param message: Push title.
    :param user_id: self-explanatory.
    :param extra_dict: this dict will be send as JSON data.
    :return:
    """
    apns_device, fcm_device = get_user_devices(user_id)
    # Note: send_message function works both on device instance and device queryset
    if apns_device is not None and (isinstance(apns_device, APNSDevice) or isinstance(apns_device, APNSDeviceQuerySet)):
        apns_device.send_message(message, extra=extra_dict)
    if fcm_device is not None and (isinstance(fcm_device, GCMDevice) or isinstance(fcm_device, GCMDeviceQuerySet)):
        fcm_device.send_message(message, extra=extra_dict)
    if len(apns_device) + len(fcm_device) > 0:
        logger.info('Push notification sent: {}, \n extra_data: {} \n receiver: {}'.format(message, extra_dict, user_id))
    else:
        logger.info('There are no registered devices for given receiver.')
