from django.conf.urls import url

from .views import TestPushView

urlpatterns = [
    url(r'^test/$', TestPushView.as_view(), name='test-push'),
]
