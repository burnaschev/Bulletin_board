from django.urls import path
from rest_framework.routers import DefaultRouter
from bulletin.apps import BulletinConfig
from bulletin.views import AdListAPIView, AdCreateAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView, \
    FeedbackViewSet

app_name = BulletinConfig.name

router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('ads/', AdListAPIView.as_view(), name='ad-list'),
    path('ads/create/', AdCreateAPIView.as_view(), name='ad-create'),
    path('ads/<int:pk>', AdRetrieveAPIView.as_view(), name='ad-view'),
    path('ads/update/<int:pk>', AdUpdateAPIView.as_view(), name='ad-update'),
    path('ads/delete/<int:pk>', AdDestroyAPIView.as_view(), name='ad-delete'),

]
urlpatterns += router.urls
