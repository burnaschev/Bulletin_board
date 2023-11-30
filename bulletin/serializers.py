from rest_framework import serializers

from bulletin.models import Ad


class AdSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'
