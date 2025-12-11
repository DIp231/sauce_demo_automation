"""
Inventory Page Object
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object for Inventory Page"""
    
    # Locators
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    INVENTORY_ITEM_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    LOGOUT_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    
    def is_inventory_page_loaded(self):
        """
        Check if inventory page is loaded
        
        Returns:
            bool: True if inventory page is loaded
        """
        is_loaded = self.is_element_visible(self.APP_LOGO)
        self.logger.info(f"Inventory page loaded: {is_loaded}")
        return is_loaded
    
    def is_app_logo_visible(self):
        """
        Verify if app logo exists
        
        Returns:
            bool: True if app logo is visible
        """
        return self.is_element_visible(self.APP_LOGO)
    
    def get_all_products(self):
        """
        Get all products from inventory
        
        Returns:
            list: List of product information dictionaries
        """
        products = []
        
        try:
            items = self.find_elements(self.INVENTORY_ITEMS)
            self.logger.info(f"Found {len(items)} products in inventory")
            
            for item in items:
                product_data = {}
                
                # Extract product name
                try:
                    name_element = item.find_element(*self.INVENTORY_ITEM_NAME)
                    product_data['name'] = name_element.text
                except:
                    product_data['name'] = "N/A"
                
                # Extract product description
                try:
                    desc_element = item.find_element(*self.INVENTORY_ITEM_DESCRIPTION)
                    product_data['description'] = desc_element.text
                except:
                    product_data['description'] = "N/A"
                
                # Extract product price
                try:
                    price_element = item.find_element(*self.INVENTORY_ITEM_PRICE)
                    product_data['price'] = price_element.text
                except:
                    product_data['price'] = "N/A"
                
                products.append(product_data)
            
            self.logger.info(f"Extracted data for {len(products)} products")
            
        except Exception as e:
            self.logger.error(f"Failed to get products: {str(e)}")
            raise
        
        return products
    
    def logout(self):
        """Logout from the application"""
        try:
            # Click menu button
            self.click_element(self.MENU_BUTTON)
            self.logger.info("Clicked menu button")
            
            # Wait for logout link to be visible
            import time
            time.sleep(1)  # Wait for menu to open
            
            # Scroll into view and click logout link
            logout_element = self.find_element(self.LOGOUT_LINK)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_element)
            time.sleep(0.5)
            self.driver.execute_script("arguments[0].click();", logout_element)
            self.logger.info("Clicked logout button")
            
        except Exception as e:
            self.logger.error(f"Failed to logout: {str(e)}")
            raise
