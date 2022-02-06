
from django.test import Client


class TestProfiles:
    def test_profiles_index_view(self):
        client = Client()

        response = client.get("/main/")
        assert response.status_code == 200

        response = client.get("/register/")
        assert response.status_code == 200