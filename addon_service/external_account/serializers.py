from addon_service.models import OSFUser
from rest_framework_json_api import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSFUser
        fields = "__all__"
