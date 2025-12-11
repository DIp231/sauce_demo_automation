"""
Base Page Object class for all page objects
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import EXPLICIT_WAIT
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        """
        Initialize base page
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
        self.logger = logger
    
    def navigate_to(self, url):
        """
        Navigate to a URL
        
        Args:
            url: URL to navigate to
        """
        self.driver.get(url)
        self.logger.info(f"Navigated to: {url}")
    
    def find_element(self, locator):
        """
        Find element using the locator
        
        Args:
            locator: Tuple containing locator strategy and value (e.g., (By.ID, "element_id"))
            
        Returns:
            WebElement: The found element
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.debug(f"Found element: {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Failed to find element: {locator}. Error: {str(e)}")
            raise
    
    def find_elements(self, locator):
        """
        Find multiple elements using the locator
        
        Args:
            locator: Tuple containing locator strategy and value
            
        Returns:
            List[WebElement]: List of found elements
        """
        try:
            elements = self.driver.find_elements(*locator)
            self.logger.debug(f"Found {len(elements)} elements: {locator}")
            return elements
        except Exception as e:
            self.logger.error(f"Failed to find elements: {locator}. Error: {str(e)}")
            raise
    
    def click_element(self, locator):
        """
        Click on an element
        
        Args:
            locator: Tuple containing locator strategy and value
        """
        try:
            element = self.find_element(locator)
            element.click()
            self.logger.info(f"Clicked on element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element: {locator}. Error: {str(e)}")
            raise
    
    def send_keys(self, locator, keys):
        """
        Send keys to an element
        
        Args:
            locator: Tuple containing locator strategy and value
            keys: Keys to send
        """
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(keys)
            self.logger.info(f"Sent keys to element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to send keys to element: {locator}. Error: {str(e)}")
            raise
    
    def get_text(self, locator):
        """
        Get text from an element
        
        Args:
            locator: Tuple containing locator strategy and value
            
        Returns:
            str: Text content of the element
        """
        try:
            element = self.find_element(locator)
            text = element.text
            self.logger.debug(f"Retrieved text from element: {locator}")
            return text
        except Exception as e:
            self.logger.error(f"Failed to get text from element: {locator}. Error: {str(e)}")
            raise
    
    def is_element_visible(self, locator):
        """
        Check if an element is visible
        
        Args:
            locator: Tuple containing locator strategy and value
            
        Returns:
            bool: True if element is visible, False otherwise
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.debug(f"Element is visible: {locator}")
            return True
        except:
            self.logger.debug(f"Element is not visible: {locator}")
            return False
    
    def is_element_present(self, locator):
        """
        Check if an element is present in DOM
        
        Args:
            locator: Tuple containing locator strategy and value
            
        Returns:
            bool: True if element is present, False otherwise
        """
        try:
            element = self.find_element(locator)
            self.logger.debug(f"Element is present: {locator}")
            return True
        except:
            self.logger.debug(f"Element is not present: {locator}")
            return False
    
    def get_current_url(self):
        """
        Get current URL
        
        Returns:
            str: Current URL
        """
        url = self.driver.current_url
        self.logger.debug(f"Current URL: {url}")
        return url
