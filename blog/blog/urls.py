"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from comments.views import delete_comment
from posts.views import main, post_view, delete_post
from django.conf import settings
from blog.views import register, authorization, logout_view
from shop.views import product_list, product_details_view

urlpatterns = [
    path("admin/django-rq/", include("django_rq.urls")),
    # ПРОФИЛЬ
    path("admin/", admin.site.urls),
    path("", authorization, name="login"),  # АВТОРИЗАЦИЯ
    path("register/", register, name="register"),  # РЕГИСТРАЦИЯ
    path("logouthtml/", logout_view, name="logout"),  # ВЫХОД ИЗ ПРОФИЛЯ
    path("main/", main, name="home"),  # ДОМАШНЯЯ СТРАНИЦА
    # ПОСТЫ
    path("post/<str:slug>/", post_view, name="post_view"),  # ПРОСМОТР ОТДЕЛЬНОГО ПОСТА
    path("delete/<int:post_id>/", delete_post, name="delete_post"),  # УДАЛЕНИЕ ПОСТА
    # КОММЕНТЫ
    path(
        "delete/<int:comment_id>/", delete_comment, name="delete_comment"
    ),  # УДАЛЕНИЕ КОММЕНТА
    # ПРОДУКТЫ
    path("products/", product_list, name="product_list"),
    path(
        "product/<int:product_id>/", product_details_view, name="product_details_view"
    ),
    # API
    path("api/", include("api.urls", namespace="api")),  # АПИ
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
