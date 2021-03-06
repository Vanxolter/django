from django.urls import include, path
from rest_framework import routers

from api.comments.views import CommentsViewSet
from api.posts.views import PostViewSet
from api.shop.views import PurchaseCreateView, ProductViewSet

from api.users.views import UserViewSet, UserCreateView, UserLoginView, UserLogoutView

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"products", ProductViewSet, basename="products")
router.register(r"users", UserViewSet, basename="users")
router.register(r"comments", CommentsViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserCreateView.as_view(), name="reg"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("products/<int:product_id>/purchase/", PurchaseCreateView.as_view(), name="purchase",),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]