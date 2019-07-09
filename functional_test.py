from selenium import webdriver

browser = webdriver.Firefox(executable_path='/Users/chengkrilo/projects/selenium_py36/geckodriver')
browser.maximize_window()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
