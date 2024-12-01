# Function to simulate a successfully processed Home Delivery Order 

def valid_home_delivery(): 

    try: 

        print("Processing Home Delivery Order...") 

        address = "123, Some Road, City, Country"  # Providing a complete address 

        if len(address.split(',')) < 4:  # Check for a valid address format 

            raise ValueError("Address is incomplete.") 

        return True 

    except ValueError as e: 

        print(f"Error in Home Delivery: {e}") 

        return False 

  

# Function to simulate a successful Payment Processing 

def valid_payment(): 

    try: 

        print("Processing Payment...") 

        balance = 100  # Sufficient balance 

        if balance < 50:  # Payment condition 

            raise ValueError("Insufficient funds for payment.") 

        return True 

    except ValueError as e: 

        print(f"Error in Payment: {e}") 

        return False 
commit done
 
