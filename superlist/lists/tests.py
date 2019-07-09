from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import home_page

# Create your tests here.
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(2+1, 3)

class HomePageTest(TestCase):
    def test_root_url(self):
        found = resolve('/lists/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))