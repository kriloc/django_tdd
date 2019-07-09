from selenium import webdriver

browser = webdriver.Firefox(executable_path='/Users/chengkrilo/projects/selenium_py36/geckodriver')
browser.maximize_window()
browser.get('http://localhost:8000')

assert 'To-Do in browser.title'

# 應用邀請她輸入一個待辦事項

# 她在一個文本框中輸入了“Buy peacock feathers”（購買孔雀羽毛）
# 伊迪絲的愛好是使用假蠅做餌釣魚

# 她按回return後，頁面更新了
# 待辦事項表格中顯示了“1: Buy peacock feathers”

# 頁面中又顯示了一個文本框，可以輸入其他的待辦事項
# 她輸入了“Use peacock feathers to make a fly”（使用孔雀羽毛做假蠅）
# 伊迪絲做事很有條理

# 頁面再次更新，她的清單中顯示了這兩個待辦事項

# 伊迪絲想知道這個網站是否會記住她的清單
# 她看到網站為她生成了一個唯一的URL
# 而且頁面中有一些文字解說這個功能

# 她訪問那個URL，發現她的待辦事項列表還在

# 她很滿意，去睡覺了

# browser.quit()