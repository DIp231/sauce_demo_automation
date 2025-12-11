"""
Test Scenario 1: Successful Login
Given I am on the Demo Login Page
When I fill the account information for account StandardUser into the Username field and the Password field
And I click the Login Button
Then I am redirected to the Demo Main Page
And I verify the App Logo exists
"""

import pytest
import logging
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import TEST_USERS

logger = logging.getLogger(__name__)


class TestScenario1:
    """Test class for Scenario 1: Successful Login"""
    
    @pytest.mark.scenario1
    @pytest.mark.login
    def test_successful_login(self, driver):
        """
        Test successful login with standard user credentials
        
        This test verifies:
        1. User can navigate to login page
        2. User can enter valid credentials
        3. User is redirected to inventory page
        4. App logo is visible on inventory page
        """
        logger.info("Starting test: Successful Login")
        
        # Step 1: Navigate to Login Page
        login_page = LoginPage(driver)
        login_page.load()
        assert login_page.is_login_page_loaded(), "Failed to load login page"
        logger.info("✓ Successfully loaded login page")
        
        # Step 2: Verify we are on the Demo Login Page
        current_url = login_page.get_current_url()
        assert "saucedemo.com" in current_url, "Not on the correct login page"
        logger.info(f"✓ Verified on correct page: {current_url}")
        
        # Step 3: Fill in credentials and login
        standard_user = TEST_USERS['standard_user']
        login_page.login_user(standard_user['username'], standard_user['password'])
        logger.info(f"✓ Logged in with user: {standard_user['username']}")
        
        # Step 4: Verify redirect to inventory page
        import time
        time.sleep(2)  # Wait for page load
        
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_page_loaded(), "Failed to load inventory page"
        logger.info("✓ Successfully redirected to inventory page")
        
        # Step 5: Verify App Logo exists
        assert inventory_page.is_app_logo_visible(), "App logo is not visible"
        logger.info("✓ App logo is visible on the page")
        
        # Step 6: Verify page URL
        inventory_url = inventory_page.get_current_url()
        assert "inventory" in inventory_url, "Not on inventory page"
        logger.info(f"✓ Verified on inventory page: {inventory_url}")
        
        logger.info("✓✓✓ Test Scenario 1 PASSED ✓✓✓")
