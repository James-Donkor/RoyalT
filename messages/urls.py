from django.urls import path
from .views import messages_dashboard, thread_detail



urlpatterns = [
    path('', messages_dashboard, name='messages-dashboard'),
    path('thread/<int:thread_id>/', thread_detail, name='thread-detail'),
]
#URLS.PY IN MESSAGES