from django.urls import path, include
from rest_framework import routers
from .views import UserProfileViewSet, OfferViewSet, MessageViewSet
from . import views
from .views import thread_detail

router = routers.DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),  # API endpoints
]
#urls.py in api