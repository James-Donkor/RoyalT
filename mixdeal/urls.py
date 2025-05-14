from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from mixdeal.views import CustomLoginView
from mixdeal.views_contracts import contracts_view
from mixdeal.views_statistics import statistics_view
from sptracker_mixdeal_test_2025.views import get_song_by_isrc as get_spotify_data
from api.views import post_login_redirect, select_role
from mixdeal.views import browse_view


 # ✅ Import from new file

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

    # ✅ Contracts route now works
    path('contracts/', contracts_view, name='contracts'),
    path('stats/', statistics_view, name='statistics_view'), 

    # ✅ Other app routes
    path('messages/', include('messages.urls')),
    path('api/', include('api.urls')),

    path('spotify/', include('sptracker_mixdeal_test_2025.urls')),
    path('spotify/data/', get_spotify_data, name='spotify_data'),

    path('redirect/', post_login_redirect, name='post_login_redirect'),
    path('select-role/', select_role, name='select_role'),

    path('browse/', browse_view, name='browse'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
