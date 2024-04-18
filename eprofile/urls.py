from django.urls import path, include
from datetime import datetime
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def health(request):
    return HttpResponse(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


urlpatterns = [
    path('api/users/', include('users.urls')),
    path('health/', health, name='health'),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
