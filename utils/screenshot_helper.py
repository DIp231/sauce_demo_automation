"""
Screenshot helper utility
"""
import os
from datetime import datetime
from config.settings import SCREENSHOTS_FOLDER


class ScreenshotHelper:
    """Helper class for taking screenshots"""
    
    @staticmethod
    def take_screenshot(driver, test_name):
        """
        Take a screenshot and save it
        
        Args:
            driver: WebDriver instance
            test_name: Name of the test for the screenshot filename
            
        Returns:
            str: Path to the saved screenshot
        """
        # Create screenshots directory if it doesn't exist
        os.makedirs(SCREENSHOTS_FOLDER, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join(SCREENSHOTS_FOLDER, screenshot_name)
        
        # Take screenshot
        driver.save_screenshot(screenshot_path)
        
        return screenshot_path
