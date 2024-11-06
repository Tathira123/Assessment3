from datetime import datetime
import re

# Function to simulate a successful Dine-In Order
def valid_dine_in():
    try:
        print("Processing Dine-In Order...")
        # Simulating a valid order processing (no errors)
        # Returning True for a successful case
        return True
    except Exception as e:
        print(f"Error in Dine-In order: {e}")
        return False

# Function to simulate a failing Home Delivery Order (Failure case 1)
def failed_home_delivery():
    try:
        print("Processing Home Delivery Order...")
        # Simulating an error in the delivery process, for example, invalid address format
        address = "123, Some Road"  # Incomplete address to trigger failure
        if len(address.split(',')) < 3:
            raise ValueError("Address is incomplete.")  # Raise a custom error
        return True
    except ValueError as e:
        print(f"Error in Home Delivery: {e}")
        return False

# Function to simulate a successful Sign-Up (Successful case 1)
def valid_signup():
    try:
        print("Processing Sign Up...")
        # Assuming user data is valid and sign-up is successful
        return True
    except Exception as e:
        print(f"Error in Sign-Up: {e}")
        return False

# Function to simulate a failing Payment Processing (Failure case 2)
def failed_payment():
    try:
        print("Processing Payment...")
        # Simulating a payment failure due to insufficient funds
        balance = 20  # Assuming insufficient balance for a larger order
        if balance < 50:  # Payment failure condition
            raise ValueError("Insufficient funds for payment.")
        return True
    except ValueError as e:
        print(f"Error in Payment: {e}")
        return False

# Function to simulate a successful Home Delivery (Successful case 2)
def valid_home_delivery():
    try:
        print("Processing Home Delivery Order...")
        # Simulating a successful home delivery order (no errors)
        return True
    except Exception as e:
        print(f"Error in Home Delivery: {e}")
        return False

# Function to simulate a successful Order Completion (Successful case 3)
def valid_order_completion():
    try:
        print("Completing Order...")
        # Simulating a successful order completion (no errors)
        return True
    except Exception as e:
        print(f"Error in Order Completion: {e}")
        return False

# Main function to test all cases
def main():
    print("Testing Functions...\n")

    # Test valid_dine_in
    print("Testing Dine-In Order:")
    result1 = valid_dine_in()
    print(f"Dine-In Result: {result1}\n")

    # Test failed_home_delivery
    print("Testing Home Delivery Order (Expected Failure):")
    result2 = failed_home_delivery()
    print(f"Home Delivery Result: {result2}\n")

    # Test valid_signup
    print("Testing Sign-Up:")
    result3 = valid_signup()
    print(f"Sign-Up Result: {result3}\n")

    # Test failed_payment
    print("Testing Payment Processing (Expected Failure):")
    result4 = failed_payment()
    print(f"Payment Result: {result4}\n")

    # Test valid_home_delivery
    print("Testing Home Delivery Order (Expected Success):")
    result5 = valid_home_delivery()
    print(f"Home Delivery Result: {result5}\n")

    # Test valid_order_completion
    print("Testing Order Completion:")
    result6 = valid_order_completion()
    print(f"Order Completion Result: {result6}\n")

if __name__ == "__main__":
    main()
