from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from fedsearch.pkgsearch.tests.utils import create_pkgs
from fedsearch.pkgsearch.models import Package


class PackageSearchViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        create_pkgs()

    def test_search_package_name(self):
        url = reverse("search")
        response = self.client.get(url, {"q": "gnome-terminal", "unittest": True})
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["name"] == "gnome-terminal"

    def test_search_package_summary(self):
        url = reverse("search")
        response = self.client.get(url, {"q": "terminal", "unittest": True})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3
        assert response.data["results"][0]["name"] == "mate-terminal"
        assert response.data["results"][1]["name"] == "gnome-terminal"
        assert response.data["results"][2]["name"] == "tmux"


class PackageViewTests(APITestCase):
    def test_package_view(self):
        package = Package.objects.create(name="foo", point_of_contact="bar")
        url = reverse("package-detail", kwargs={"pk": package.pk})
        response = self.client.get(url)
        assert response.data["name"] == "foo"
