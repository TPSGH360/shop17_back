from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views
from products.views import ProductViewSet, CustomTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("phones/", views.phones_view, name="phones"),
]
# Add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
