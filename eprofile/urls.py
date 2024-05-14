from datetime import datetime

from django.http import HttpResponse
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


def health(request):
    return HttpResponse("test5")


urlpatterns = [
    path('health/', health, name='health'),

    path('api/users/', include('users.urls')),
    path('api/activities/', include('activities.urls')),
    path('api/notifications/', include('notifications.urls')),

    # auth
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
