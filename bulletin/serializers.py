from rest_framework import serializers

from bulletin.models import Ad, Feedback


class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class AdSerializers(serializers.ModelSerializer):
    feedbacks = FeedbackSerializers(source='feedback', many=True, read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
