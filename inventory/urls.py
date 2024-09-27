from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ItemCreateView, ItemDetailView, UserRegistrationView

urlpatterns = [
    path("items/", ItemCreateView.as_view(), name="create_item"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
]
urlpatterns += [
    path("register/", UserRegistrationView.as_view(), name="user-register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
