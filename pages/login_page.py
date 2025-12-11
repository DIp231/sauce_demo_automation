"""
Login Page Object
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import LOGIN_PAGE_URL


class LoginPage(BasePage):
    """Page Object for Login Page"""
    
    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")
    
    def load(self):
        """Navigate to Login Page"""
        self.navigate_to(LOGIN_PAGE_URL)
        self.logger.info("Login page loaded")
    
    def enter_username(self, username):
        """
        Enter username in the username field
        
        Args:
            username: Username to enter
        """
        self.send_keys(self.USERNAME_FIELD, username)
        self.logger.info(f"Entered username: {username}")
    
    def enter_password(self, password):
        """
        Enter password in the password field
        
        Args:
            password: Password to enter
        """
        self.send_keys(self.PASSWORD_FIELD, password)
        self.logger.info(f"Entered password")
    
    def click_login_button(self):
        """Click the login button"""
        self.click_element(self.LOGIN_BUTTON)
        self.logger.info("Clicked login button")
    
    def get_error_message(self):
        """
        Get error message text
        
        Returns:
            str: Error message text
        """
        error_text = self.get_text(self.ERROR_MESSAGE)
        self.logger.info(f"Error message: {error_text}")
        return error_text
    
    def is_error_message_present(self):
        """
        Check if error message is present
        
        Returns:
            bool: True if error message is present
        """
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    def is_login_page_loaded(self):
        """
        Check if login page is loaded
        
        Returns:
            bool: True if login page is loaded
        """
        return self.is_element_visible(self.LOGIN_LOGO)
    
    def login_user(self, username, password):
        """
        Perform login with username and password
        
        Args:
            username: Username to login
            password: Password to login
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.logger.info(f"Logged in with user: {username}")
