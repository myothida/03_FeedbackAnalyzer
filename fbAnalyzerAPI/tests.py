from django.test import TestCase

class MyTestCase(TestCase):
    def test_my_view(self):
        response = self.client.get('/http://127.0.0.1:8000//')  # Replace with your URL
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Expected content")

