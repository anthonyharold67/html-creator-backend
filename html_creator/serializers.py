from rest_framework import serializers
from .models import HtmlCreatorModel

class HtmlCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HtmlCreatorModel
        fields = "__all__"