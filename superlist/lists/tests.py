from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import home_page
from .models import Item

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
        # response = home_page(request)
        response = self.client.get('/lists/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

        self.assertTemplateUsed(response, 'Lists/home.html')


    def test_only_saves_items_when_necessary(self):
        self.client.get('/lists/')
        self.assertEqual(Item.objects.count(), 0)


    def test_can_seve_a_POST_request(self):
        self.client.post('/lists/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)  ## 響應是 HTTP 重定向，狀態碼是 302，讓瀏覽器指向一個新地址。
        self.assertEqual(response['location'], '/lists/')

        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'Lists/home.html')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get('/lists/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):
    def test_save_and_retriving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')