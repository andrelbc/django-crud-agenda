from django.test import TestCase

# Create your tests here.
class URLTest(TestCase):
    def test_agenda_page_url(self):
        response = self.client.get('/agenda/')
        self.assertEqual(response.status_code, 200)