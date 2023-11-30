from rest_framework import serializers

from bulletin.models import Ad


class AdSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ad
        field = '__all__'
