from rest_framework import generics, viewsets
from bulletin.models import Ad, Feedback
from bulletin.paginators import AdPaginator
from bulletin.permission import IsUser, IsAdmin
from bulletin.serializers import AdSerializers, FeedbackSerializers
from django_filters.rest_framework import DjangoFilterBackend


class AdListAPIView(generics.ListAPIView):
    """ Getting list fo ads """

    serializer_class = AdSerializers
    queryset = Ad.objects.all()
    pagination_class = AdPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('title',)
    permission_classes = [IsUser]


class AdCreateAPIView(generics.CreateAPIView):
    """ Create ads """

    serializer_class = AdSerializers
    permission_classes = [IsUser | IsAdmin]

    def perform_create(self, serializer):
        """ User's Announcement """

        new_ad = serializer.save(author=self.request.user)
        new_ad.author = self.request.user
        new_ad.save()


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """ View ads """

    serializer_class = AdSerializers
    queryset = Ad.objects.all()
    permission_classes = [IsUser | IsAdmin]


class AdDestroyAPIView(generics.DestroyAPIView):
    """ Delete ads """

    serializer_class = AdSerializers
    queryset = Ad.objects.all()
    permission_classes = [IsUser | IsAdmin]


class AdUpdateAPIView(generics.UpdateAPIView):
    """ Update ads """

    serializer_class = AdSerializers
    queryset = Ad.objects.all()
    permission_classes = [IsUser | IsAdmin]


class FeedbackViewSet(viewsets.ModelViewSet):
    """ Managing comments """

    serializer_class = FeedbackSerializers
    queryset = Feedback.objects.all()
    permission_classes = [IsUser | IsAdmin]

    def perform_create(self, serializer):
        """ User's feedback """

        new_feedback = serializer.save(author=self.request.user)
        new_feedback.author = self.request.user
        new_feedback.save()
