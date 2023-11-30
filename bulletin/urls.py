from django.urls import path

from bulletin.apps import BulletinConfig
from bulletin.views import AdListAPIView, AdCreateAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView

app_name = BulletinConfig.name

urlpatterns = [
    path('', AdListAPIView.as_view(), name='ad-list'),
    path('create/', AdCreateAPIView.as_view(), name='ad-create'),
    path('view/<int:pk>', AdRetrieveAPIView.as_view(), name='ad-view'),
    path('update/<int:pk>', AdUpdateAPIView.as_view(), name='ad-update'),
    path('delete/<int:pk>', AdDestroyAPIView.as_view(), name='ad-delete'),
]
