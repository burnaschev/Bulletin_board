from django.urls import path

from bulletin.views import AdListAPIView, AdCreateAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView

urlpatterns = [
    path('', AdListAPIView.as_view(), name='ad-list'),
    path('create/', AdCreateAPIView.as_view(), name='ad-create'),
    path('view/<int:pk>', AdRetrieveAPIView.as_view(), name='ad-view'),
    path('update/<int:pk>', AdUpdateAPIView.as_view(), name='ad-update'),
    path('delete/<int:pk>', AdDestroyAPIView.as_view(), name='ad-delete'),
]
