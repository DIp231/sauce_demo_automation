"""
Test Scenario 2: Failed Login
Given I am on the Demo Login Page
When I fill the account information for account LockedOutUser into the Username field and the Password field
And I click the Login Button
Then I verify the Error Message contains the text "Sorry, this user has been banned."
"""

import pytest
import logging
from pages.login_page import LoginPage
from config.settings import TEST_USERS, BANNED_USER_ERROR_MESSAGE

logger = logging.getLogger(__name__)


class TestScenario2:
    """Test class for Scenario 2: Failed Login (Locked Out User)"""
    
    @pytest.mark.scenario2
    @pytest.mark.login
    def test_failed_login_locked_out_user(self, driver):
        """
        Test failed login with locked out user credentials
        
        This test verifies:
        1. User can navigate to login page
        2. User enters locked_out_user credentials
        3. Login fails with appropriate error message
        4. Error message contains "Sorry, this user has been banned."
        """
        logger.info("Starting test: Failed Login - Locked Out User")
        
        # Step 1: Navigate to Login Page
        login_page = LoginPage(driver)
        login_page.load()
        assert login_page.is_login_page_loaded(), "Failed to load login page"
        logger.info("✓ Successfully loaded login page")
        
        # Step 2: Verify we are on the Demo Login Page
        current_url = login_page.get_current_url()
        assert "saucedemo.com" in current_url, "Not on the correct login page"
        logger.info(f"✓ Verified on correct page: {current_url}")
        
        # Step 3: Fill in locked_out_user credentials and attempt login
        locked_out_user = TEST_USERS['locked_out_user']
        login_page.login_user(locked_out_user['username'], locked_out_user['password'])
        logger.info(f"✓ Attempted login with user: {locked_out_user['username']}")
        
        # Step 4: Wait for error message to appear
        import time
        time.sleep(1)
        
        # Step 5: Verify error message is present
        assert login_page.is_error_message_present(), "Error message is not displayed"
        logger.info("✓ Error message is displayed")
        
        # Step 6: Get error message text and verify it contains expected text
        error_message = login_page.get_error_message()
        assert BANNED_USER_ERROR_MESSAGE in error_message, \
            f"Expected error message to contain: '{BANNED_USER_ERROR_MESSAGE}', but got: '{error_message}'"
        logger.info(f"✓ Error message verified: {error_message}")
        
        # Step 7: Verify we are still on login page (not redirected)
        current_url = login_page.get_current_url()
        assert "inventory" not in current_url, "User should not be redirected to inventory page"
        logger.info("✓ User remained on login page (not redirected)")
        
        logger.info("✓✓✓ Test Scenario 2 PASSED ✓✓✓")
