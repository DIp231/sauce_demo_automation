"""
Test Scenario 3: Extract Data from Inventory
Given I am logged in
When I am on the inventory page
Then I extract content from the web page
And Save it to a file
Then I log out
And I verify I am on the Login page again
"""

import pytest
import logging
import json
import csv
import os
from datetime import datetime
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import TEST_USERS, EXTRACTED_DATA_FOLDER

logger = logging.getLogger(__name__)


class TestScenario3:
    """Test class for Scenario 3: Extract Data from Inventory"""
    
    @pytest.mark.scenario3
    def test_extract_and_save_inventory_data(self, driver):
        """
        Test extracting inventory data and saving to files
        
        This test verifies:
        1. User can login successfully
        2. User is on inventory page
        3. User can extract product data
        4. Data is saved in multiple formats (JSON, CSV, and TXT)
        5. User can logout
        6. User is redirected back to login page
        """
        logger.info("Starting test: Extract and Save Inventory Data")
        
        # Step 1: Navigate to Login Page and login
        login_page = LoginPage(driver)
        login_page.load()
        logger.info("✓ Loaded login page")
        
        standard_user = TEST_USERS['standard_user']
        login_page.login_user(standard_user['username'], standard_user['password'])
        logger.info(f"✓ Logged in with user: {standard_user['username']}")
        
        # Step 2: Wait and verify inventory page is loaded
        import time
        time.sleep(2)
        
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_page_loaded(), "Failed to load inventory page"
        logger.info("✓ Successfully on inventory page")
        
        # Step 3: Extract product data
        products = inventory_page.get_all_products()
        assert len(products) > 0, "No products found in inventory"
        logger.info(f"✓ Extracted data for {len(products)} products")
        
        # Step 4: Save data to files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create extracted_data directory if it doesn't exist
        os.makedirs(EXTRACTED_DATA_FOLDER, exist_ok=True)
        
        # Save as JSON
        json_file = os.path.join(EXTRACTED_DATA_FOLDER, f"inventory_data_{timestamp}.json")
        with open(json_file, 'w') as f:
            json.dump(products, f, indent=4)
        logger.info(f"✓ Saved product data to JSON: {json_file}")
        
        # Save as CSV
        csv_file = os.path.join(EXTRACTED_DATA_FOLDER, f"inventory_data_{timestamp}.csv")
        if products:
            with open(csv_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=products[0].keys())
                writer.writeheader()
                writer.writerows(products)
            logger.info(f"✓ Saved product data to CSV: {csv_file}")
        
        # Save as TXT (formatted)
        txt_file = os.path.join(EXTRACTED_DATA_FOLDER, f"inventory_data_{timestamp}.txt")
        with open(txt_file, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("SAUCE DEMO - INVENTORY DATA EXTRACTION\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Extraction Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Products: {len(products)}\n")
            f.write("=" * 80 + "\n\n")
            
            for idx, product in enumerate(products, 1):
                f.write(f"Product {idx}:\n")
                f.write(f"  Name: {product.get('name', 'N/A')}\n")
                f.write(f"  Price: {product.get('price', 'N/A')}\n")
                f.write(f"  Description: {product.get('description', 'N/A')}\n")
                f.write("-" * 80 + "\n\n")
        logger.info(f"✓ Saved product data to TXT: {txt_file}")
        
        # Step 5: Logout
        inventory_page.logout()
        time.sleep(2)
        logger.info("✓ Successfully logged out")
        
        # Step 6: Verify we are back on login page
        login_page_after_logout = LoginPage(driver)
        assert login_page_after_logout.is_login_page_loaded(), "Not back on login page after logout"
        logger.info("✓ Verified we are on the login page")
        
        current_url = login_page_after_logout.get_current_url()
        assert "inventory" not in current_url, "Still on inventory page after logout"
        logger.info(f"✓ Verified logout URL: {current_url}")
        
        logger.info("✓✓✓ Test Scenario 3 PASSED ✓✓✓")
        logger.info(f"✓ Extracted data saved to:\n  - JSON: {json_file}\n  - CSV: {csv_file}\n  - TXT: {txt_file}")
