from rest_framework import serializers

from bulletin.models import Ad, Feedback


class AdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
