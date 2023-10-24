import json
from api.tests.factories import UserFactory
from django.test import TestCase
from api.osf_user.serializers import UserSerializer
from api.osf_user.models import OSFUser

from rest_framework import viewsets
from rest_framework_json_api.renderers import JSONRenderer


class TestViewSet(viewsets.ModelViewSet):
    queryset = OSFUser.objects.all()
    serializer_class = UserSerializer


def render_test_data(instance):
    serializer = UserSerializer(instance=instance)
    renderer = JSONRenderer()
    renderer_context = {"view": TestViewSet()}
    data = renderer.render(serializer.data, renderer_context=renderer_context)
    return json.loads(data)


class TestBaseSerializer(TestCase):
    """Simple base test to test serializer models"""

    def test_serializer(self):
        user = UserFactory(user_guid="hurts1")
        data = render_test_data(user)
        assert data["data"]["attributes"]["user_guid"] == "hurts1"
