from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_indexpage_is_avaliable(self):
        respone = self.client.get(reverse("webapp:index"))
        self.assertEqual(respone.status_code, 200)
