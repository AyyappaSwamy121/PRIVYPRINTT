from django.urls import include, path
from django.views.generic import View
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class HealthCheckView(View):
    def get(self, _request, *args, **kwargs):
        return JsonResponse({"status": "ok", "service": "privy-backend"})


urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health-check"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/", include("apps.auth_app.urls")),
]
