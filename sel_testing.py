import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

tic = int(round(time.time() * 1000))

browser = webdriver.Chrome()
browser.get('http://192.168.3.191:8080/login')

user_field = browser.find_element_by_name('uname')
pass_field = browser.find_element_by_name('pw')

user_field.send_keys('abc')
pass_field.send_keys('xyz')

pass_field.send_keys(Keys.RETURN)

try:
    assert 'log' in browser.title
    print('Test case Success')
except AssertionError:
    print('Assertion Error')
finally:
    toc = int(round(time.time() * 1000))
    time.sleep(2)
    browser.close()

import unittest


class MyTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        print('In Setup..')

    def test_testcase1(self):
        browser = self.browser
        browser.get('http://192.168.3.191:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')

        user_field.send_keys('abc')
        pass_field.send_keys('xyz')

        pass_field.send_keys(Keys.RETURN)

        assert 'Log' in browser.title
        print('Testcase 1 Pass')

    def test_testcase2(self):
        browser = self.browser
        browser.get('http://192.168.3.191:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')

        user_field.send_keys('abc')
        pass_field.send_keys('xyz')

        pass_field.send_keys(Keys.RETURN)

        assert 'Log' in browser.title
        print('Testcase 2 Pass')

    def tearDown(self):
        print('In tearDown')
        time.sleep(2)
        self.browser.close()


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()

print((toc - tic) / 1000)
