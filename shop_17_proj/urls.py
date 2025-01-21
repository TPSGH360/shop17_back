from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views
from products.views import (
    CartView,
    CustomTokenObtainPairView,
    GetCSRFToken,
    LoginView,
    ProductViewSet,
)
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("csrf/", GetCSRFToken.as_view(), name="csrf"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("cart/", CartView.as_view(), name="cart"),
    path("", include(router.urls)),
    path("phones/", views.phones_view, name="phones"),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
# Add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
