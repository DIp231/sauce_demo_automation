"""
WebDriver Factory for creating browser instances
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import BROWSER_NAME, HEADLESS_MODE, IMPLICIT_WAIT
import logging

logger = logging.getLogger(__name__)


class DriverFactory:
    """Factory class for creating and managing WebDriver instances"""
    
    @staticmethod
    def create_driver(browser_name=BROWSER_NAME):
        """
        Create and return a WebDriver instance
        
        Args:
            browser_name: Name of the browser to instantiate
            
        Returns:
            WebDriver: Browser driver instance
        """
        if browser_name.lower() == "chrome":
            return DriverFactory._create_chrome_driver()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
    
    @staticmethod
    def _create_chrome_driver():
        """
        Create and configure Chrome WebDriver
        
        Returns:
            WebDriver: Chrome driver instance
        """
        options = Options()
        
        if HEADLESS_MODE:
            options.add_argument("--headless")
        
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(IMPLICIT_WAIT)
        
        logger.info(f"Chrome WebDriver initialized with implicit wait: {IMPLICIT_WAIT}s")
        return driver
    
    @staticmethod
    def quit_driver(driver):
        """
        Close the WebDriver instance
        
        Args:
            driver: WebDriver instance to close
        """
        if driver:
            driver.quit()
            logger.info("WebDriver closed")
