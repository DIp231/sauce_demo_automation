"""
Configuration settings for Sauce Demo automation tests
"""

# Application URLs
BASE_URL = "https://www.saucedemo.com/"
LOGIN_PAGE_URL = "https://www.saucedemo.com/"
INVENTORY_PAGE_URL = "https://www.saucedemo.com/inventory.html"

# Browser Configuration
BROWSER_NAME = "chrome"
HEADLESS_MODE = False
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15

# User Credentials
TEST_USERS = {
    "standard_user": {
        "username": "standard_user",
        "password": "secret_sauce"
    },
    "locked_out_user": {
        "username": "locked_out_user",
        "password": "secret_sauce"
    },
    "problem_user": {
        "username": "problem_user",
        "password": "secret_sauce"
    },
    "performance_glitch_user": {
        "username": "performance_glitch_user",
        "password": "secret_sauce"
    },
    "error_user": {
        "username": "error_user",
        "password": "secret_sauce"
    },
    "visual_user": {
        "username": "visual_user",
        "password": "secret_sauce"
    }
}

# Test Data
BANNED_USER_ERROR_MESSAGE = "Sorry, this user has been locked out."

# Report Settings
REPORT_FOLDER = "reports"
SCREENSHOTS_FOLDER = "screenshots"
EXTRACTED_DATA_FOLDER = "extracted_data"

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
