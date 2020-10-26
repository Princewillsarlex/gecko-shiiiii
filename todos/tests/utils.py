from accounts.tests.mixins import SeleniumScreenShotMixin
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse_lazy, reverse

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



class UserBaseSeleniumTestCase(SeleniumScreenShotMixin, StaticLiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user("todo_man", "todo@man.com", "ThiSk4Zu")
        self.user.is_active = True
        self.user.save()
        self.browser = webdriver.Firefox()
        binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities["marionette"] = False

        driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities, executable_path="/usr/local/bin/geckodriver")
        driver.get("http://google.com/")
        print ("Headless Firefox Initialized")
        self.browser.get(self.live_server_url)

    def login(self):
        self.browser.get('%s%s' % (self.live_server_url, reverse_lazy("accounts:login")))
        self.browser.find_element_by_id("id_username").send_keys("todo_man")
        self.browser.find_element_by_id("id_password").send_keys("ThiSk4Zu")
        self.browser.find_element_by_id("user-login-submit").click()
