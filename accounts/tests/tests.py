from accounts.tests.mixins import SeleniumScreenShotMixin
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class UserRegistrationSeleniumTestCase(SeleniumScreenShotMixin, StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities["marionette"] = False

        driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities, executable_path="/usr/local/bin/geckodriver")
        driver.get("http://google.com/")
        print ("Headless Firefox Initialized")
        self.browser.get(self.live_server_url)

    def test_user_registration(self):
        self.browser.find_element_by_id("id-register").click()

        username = "newuser"
        self.browser.find_element_by_id("id_username").send_keys(username)
        self.browser.find_element_by_id("id_email").send_keys("newuser@email.com")
        self.browser.find_element_by_id("id_password1").send_keys("Psiph5sK")
        self.browser.find_element_by_id("id_password2").send_keys("Psiph5sK")

        self.browser.find_element_by_id("user-registration-submit").click()
        self.assertEqual(username, self.browser.find_element_by_id("username-text").text)


class UserLoginSeleniumTestCase(SeleniumScreenShotMixin, StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities["marionette"] = False

        driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities, executable_path="/usr/local/bin/geckodriver")
        driver.get("http://google.com/")
        print ("Headless Firefox Initialized")
        self.browser.get(self.live_server_url)
        self.user = User.objects.create_user(username="newuser", password="NiGiw3Ch", email="todo@todoapp.com")

    def tearDown(self):
        self.browser.quit()

    def test_user_login(self):
        self.browser.find_element_by_id("id-login").click()
        self.browser.find_element_by_id("id_username").send_keys("newuser")
        self.browser.find_element_by_id("id_password").send_keys("NiGiw3Ch")
        self.browser.find_element_by_id("user-login-submit").click()
        self.assertEqual(self.user.username, self.browser.find_element_by_id("username-text").text)
