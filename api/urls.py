from django.urls import path, include
from rest_framework import routers
from .views import UserProfileViewSet, OfferViewSet, MessageViewSet
from . import views
from .views import thread_detail
from django.urls import path
from api import views
from .views import thread_detail, select_role, post_login_redirect



router = routers.DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),  # API endpoints
    path('select-role/', views.select_role, name='select_role'),
    path('redirect/', views.post_login_redirect, name='post_login_redirect'),
    # other URLs
]
#urls.py in api