from django.test import LiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path='/Users/chengkrilo/projects/selenium_py36/geckodriver')

    def tearDown(self) -> None:
        # pass
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     f"New to-do item did not appear in table. Contents were:\n{table.text}"
        # )  ## 留意一下 any 函數，它是 Python 中的原生函數，卻鮮為人知。
        self.assertIn(row_text, [row.text for row in rows])



    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000/lists/')
        self.assertIn('To-Do', self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', head_text)

        # 應用邀請她輸入一個待辦事項
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertIn(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一個文本框中輸入了“Buy peacock feathers”（購買孔雀羽毛）
        # 伊迪絲的愛好是使用假蠅做餌釣魚
        inputbox.send_keys('1: Buy peacock feathers')

        # 她按回return後，頁面更新了
        # 待辦事項表格中顯示了“1: Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        # self.assertIn(
        #     '2: Use peacock feathers to make a fly',
        #     [row.text for row in rows]
        # )
        # 頁面中又顯示了一個文本框，可以輸入其他的待辦事項
        # 她輸入了“Use peacock feathers to make a fly”（使用孔雀羽毛做假蠅）
        # 伊迪絲做事很有條理
        self.fail('Finish the test!')

        # 頁面再次更新，她的清單中顯示了這兩個待辦事項

        # 伊迪絲想知道這個網站是否會記住她的清單
        # 她看到網站為她生成了一個唯一的URL
        # 而且頁面中有一些文字解說這個功能

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# browser = webdriver.Firefox(executable_path='/Users/chengkrilo/projects/selenium_py36/geckodriver')
# browser.maximize_window()
#
#
# try:
#     assert 'To-Do' in browser.title



# 她訪問那個URL，發現她的待辦事項列表還在

# 她很滿意，去睡覺了
# finally:
#     browser.quit()