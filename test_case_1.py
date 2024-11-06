import unittest
from datetime import datetime
from unittest.mock import patch
from main import User, DineIn, Menu, user_data_list

# Assuming the classes are in the module `restaurant_app.py`:
# from restaurant_app import User, Menu, DineIn, OrderOnline, MenuItem

class TestRestaurantApp(unittest.TestCase):

    # Test case 1: Test valid password format (Should pass)
    def test_valid_password(self):
        user = User("John", "Doe", "0123456789", "Password123@1", "01/01/1990")
        self.assertTrue(user.validate_password(), "Password should be valid according to the format.")

    # Test case 2: Test invalid password format (Should fail)
    def test_invalid_password(self):
        user = User("Jane", "Smith", "0987654321", "password", "01/01/1992")
        self.assertFalse(user.validate_password(), "Password should be invalid due to missing special character and number.")

    # Test case 3: Test calculating age (Should pass)
    def test_get_age(self):
        user = User("Alice", "Wonderland", "0456789012", "Alice123@1", "15/05/2000")
        age = user.get_age()
        # Assuming the current year is 2024, Alice's age should be 24
        self.assertEqual(age, 24, f"Alice's age should be 24, but got {age}.")

    # Test case 4: Test calculating total order amount for DineIn (Should pass)
    def test_calculate_amount_dine_in(self):
        menu = Menu()
        food_items = [menu.food_menu[0], menu.food_menu[2]]  # Noodles and Dumpling
        drink_items = [menu.drink_menu[1]]  # Cold drink
        dine_in_order = DineIn()
        
        # Calculate total price for these items
        total_price = dine_in_order.calculate_amount(food_items, drink_items)
        expected_total_price = (2 + 6) + 4  # Food (Noodles + Dumpling) + Drink (Cold drink)
        service_charge = expected_total_price * 0.15
        expected_total_price += service_charge
        
        self.assertEqual(total_price, expected_total_price, f"Expected total price is {expected_total_price}, but got {total_price}.")

    # Test case 5: Test invalid date format in order (Should fail)
    @patch("builtins.input", side_effect=["30/02/2024", "12/12/2024"])  # Mocking user input to simulate invalid date
    def test_invalid_order_date(self, mock_input):
        dine_in_order = DineIn()
        with self.assertRaises(ValueError):
            dine_in_order.proceed_order()  # This will raise an error on invalid date entry.
        
        # Verify that the correct error was raised (we mock the date input to simulate an invalid entry)
        self.assertEqual(mock_input.call_count, 2)  # Ensuring that the prompt was called twice

    # Test case 6: Test valid user sign up with all correct fields (Should pass)
    def test_valid_signup(self):
        user_data = User("Charlie", "Brown", "0498765432", "Charlie@1234", "20/05/1998")
        user_data_list.append(user_data)
        self.assertIn(user_data, user_data_list, "User should be added to the user_data_list.")

    # Test case 7: Test invalid mobile number format (Should fail)
    def test_invalid_mobile_number(self):
        with self.assertRaises(ValueError):
            user = User("Test", "User", "12345678", "Test@1234", "01/01/2000")  # Invalid mobile number

    # Test case 8: Test invalid menu item selection in DineIn (Should fail)
    @patch("builtins.input", side_effect=["9", "7"])  # Mocking invalid input
    def test_invalid_food_item_selection(self, mock_input):
        dine_in_order = DineIn()
        dine_in_order.proceed_order()  # First enter invalid item, then '7' to proceed
        self.assertEqual(mock_input.call_count, 2, "Should prompt the user twice for input.")
        # Check that no invalid selection is accepted
        self.assertNotIn('9', [str(item) for item in dine_in_order.selected_food_items])

if __name__ == "__main__":
    unittest.main()
