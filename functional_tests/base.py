from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model
from selenium.webdriver.common.by import By
from utils import get_browser


class LavavaFunctionalTests(LiveServerTestCase):

    fixtures = ["gamedata_fixtures.json"]

    @classmethod
    def setUpClass(cls):

        user_model = get_user_model()

        cls.player = user_model.objects.create_superuser(
            username="testuser",
            email="teste@teste.com",
            password="testpassword",
            is_staff=True,
        )

        return super().setUpClass()

    def setUp(self):
        self.browser = get_browser()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def responsive_helper(self, width, callback):
        """Helper function to test responsiveness of the welcome title"""
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(width, 1024)
        welcome_title = self.browser.find_element(
            By.XPATH, "/html/body/main/section[1]/div/div/div[2]"
        )
        welcome_title_position = welcome_title.value_of_css_property("position")
        return callback(welcome_title_position)

    def login_user(self, email, password):
        login_url = self.live_server_url + "/accounts/login/"
        self.browser.get(login_url)

        email_input = self.browser.find_element(By.XPATH, "//*[@id='id_login']")
        email_input.send_keys(email)

        password_input = self.browser.find_element(By.XPATH, "//*[@id='id_password']")
        password_input.send_keys(password)

        login_button = self.browser.find_element(
            By.XPATH, "/html/body/main/div/div/form/div/div/button"
        )
        login_button.click()
