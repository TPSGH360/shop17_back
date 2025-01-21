from django.urls import path
from .views import GetCSRFToken, LoginView, CartView

urlpatterns = [
    path("csrf/", GetCSRFToken.as_view(), name="csrf"),
    path("login/", LoginView.as_view(), name="login"),
    path("cart/", CartView.as_view(), name="cart"),
]
