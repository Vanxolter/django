from django.test import Client
import pytest

from django.contrib.auth.models import User
from shop.models import Purchase, Product


@pytest.mark.django_db
class TestPurchase:
    def test_purchase(self):
        client = Client()

        user = User.objects.create(username="test", email="test@test.com", password="test")
        client.force_login(user)
        product = Product.objects.create(title="Test", cost=100)
        Purchase.objects.create(user=user, product=product, count=3)

        response = client.get("/purchase/")
        assert response.status_code == 200