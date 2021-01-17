import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class AmazonTestCase(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.get('http://www.amazon.in')
		self.addCleanup(self.browser.quit)

	def testPageTitle(self):
		self.assertIn('Amazon', self.browser.title)

	def testlogin(self):
		elem = self.browser.find_element_by_id('nav-link-accountList-nav-line-1').click()
		elem = self.browser.find_element_by_id('ap_email').send_keys('gupta.aaryan8@gmail.com')
		elem = self.browser.find_element_by_id('continue').click()
		elem = self.browser.find_element_by_id('ap_password').send_keys('HACKworld13')
		elem = self.browser.find_element_by_id('auth-signin-button').click()
		self.browser.implicitly_wait(2)
		self.assertIn('Verification', self.browser.title)
	
	def testsearch(self):
		elem = self.browser.find_element_by_id('twotabsearchtextbox').send_keys('phone')
		elem = self.browser.find_element_by_id('nav-search-submit-button').click()
		res = self.browser.find_elements_by_class_name('s-result-item')
		elem = self.browser.find_element_by_xpath("//*[text()='Previous']")
		self.browser.implicitly_wait(2)
		self.browser.execute_script("arguments[0].scrollIntoView();", elem)
		self.browser.implicitly_wait(2)
		self.assertTrue(len(res)>10)

	def testaddtocart(self):
		elem = self.browser.find_element_by_class_name('feed-carousel-card')
		self.browser.execute_script("arguments[0].scrollIntoView();", elem)
		self.browser.implicitly_wait(2)
		elem.click()
		self.browser.implicitly_wait(2)
		elem = self.browser.find_element_by_class_name('octopus-dlp-image-section').click()
		self.browser.implicitly_wait(2)
		elem = self.browser.find_element_by_id('add-to-cart-button').click()
		self.browser.implicitly_wait(2)
		self.assertIn('Shopping Cart', self.browser.title)

	def teardown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2)