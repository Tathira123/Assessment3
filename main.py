# -*- coding: utf-8 -*- 

""" 

Created on Sun Apr 28 14:36:31 2024 

  

@author: tathira 

""" 

from datetime import datetime 

import re 

  

class User: 

    def __init__(self, first_name, last_name, mobile_number, password, dob, address = None): 

        self.first_name = first_name 

        self.last_name = last_name 

        self.mobile_number = mobile_number 

        self.password = password 

        self.dob = dob 

        self.address = address      # address attribute with default value None 

  

    def validate_password(self): 

        if re.match('^[a-zA-Z][a-zA-Z]*[@&#]\d+$', self.password): 

            return True 

        else: 

            return False 

  

    def get_age(self): 

        # Assuming current year is 2024 

        birth_year = int(self.dob.split('/')[2]) 

        return 2024 - birth_year 

  

    def __str__(self): 

        return f"Name: {self.first_name} {self.last_name}, Mobile Number: {self.mobile_number}, DOB: {self.dob}" 

  

class MenuItem: 

    def __init__(self, item_id, name, price): 

        self.item_id = item_id 

        self.name = name 

        self.price = price 

  

class Menu: 

    def __init__(self): 

        self.food_menu = [ 

            MenuItem(1, 'Noodles', 2), 

            MenuItem(2, 'Sandwich', 4), 

            MenuItem(3, 'Dumpling', 6), 

            MenuItem(4, 'Muffins', 8), 

            MenuItem(5, 'Pasta', 10), 

            MenuItem(6, 'Pizza', 20)] 

                             

        self.drink_menu = [ 

            MenuItem(1, 'Coffee', 2), 

            MenuItem(2, 'Colddrink', 4), 

            MenuItem(3, 'Shake', 6)] 

  

    def display_food_menu(self): 

        index = 1 

        for item in self.food_menu: 

            print(f'Enter {index} for {item.name} - Price AUD {item.price}') 

            index += 1 

     

    def display_drink_menu(self): 

        index = 1 

        for item in self.drink_menu: 

            print(f'Enter {index} for {item.name} - Price AUD {item.price}') 

            index += 1 

  

class Order: 

    order_count = 0 

  

    def __init__(self, option): 

        self.option = option 

        Order.order_count += 1 

        self.order_id = 'B00' + str(Order.order_count) 

  

    def checkout_order(self): 

        while True: 

            proceed_payment = input('Please enter Y to proceed to Check out or Enter N to cancel the order: ') 

            if proceed_payment.upper() == 'Y': 

                break 

            elif proceed_payment.upper() == 'N': 

                print('Your order has been cancelled!') 

                return False #return to main menu 

            else: 

                print('Please enter valid option Y or N.') 

        return True      # If the order is not cancelled, continue with the checkout process    

  

class DineIn(Order): 

    def __init__(self): 

        super().__init__('Dine In') 

  

    def calculate_amount(self, selected_food_items, selected_drink_items): 

        food_total_price = sum(item.price for item in selected_food_items) 

        drink_total_price = sum(item.price for item in selected_drink_items) 

        total_price = (food_total_price + drink_total_price)  

        service_charge = total_price * 0.15 

        total_payable_price = total_price + service_charge 

        print('Your Order ID is', self.order_id,'. Your Total Payable Amount is AUD' + str(total_payable_price) + ' inclusing AUD '+str(service_charge) + ' for Service Charges.') 

        return total_payable_price 

  

    def proceed_order(self): 

        print('Dine In Menu: ') 

        menu = Menu() 

        menu.display_food_menu() 

        print('Enter 7 for Food Check out') 

        selected_food_items = [] 

        while True: 

            select = input(': ') 

            if select == '7': 

                break 

            elif select in ['1', '2', '3', '4', '5', '6']: 

                selected_food_items.append(menu.food_menu[int(select) - 1]) 

            else: 

                print('Please enter a valid option.') 

  

        print('Drink Menu: ') 

        menu.display_drink_menu() 

        print('Enter 4 for Drink Check out') 

        selected_drink_items = [] 

        while True: 

            select = input(': ') 

            if select == '4': 

                break 

            elif select in ['1', '2', '3']: 

                selected_drink_items.append(menu.drink_menu[int(select) - 1]) 

            else: 

                print('Please enter a valid option.') 

  

        total_amount = self.calculate_amount(selected_food_items, selected_drink_items) 

        self.checkout_order() 

         

        while True: 

            try: 

                Date = input('Please enter the Date of Booking for Dine in (DD/MM/YYYY): ') 

                date_format = Date.split('/') 

                if len(date_format) != 3: 

                    print('Please enter the date in the correct format (DD/MM/YYYY).') 

                    continue 

                 

                hour_minute = input('Please enter the time of booking (HH:MM): ') 

                hour, minute = [int(part) for part in hour_minute.split(':')] 

                if not (0 <= hour <= 23 and 0 <= minute <= 59): 

                    print('Please enter a valid time.') 

                    continue 

     

                Persons = input('Please enter the Number of Persons: ') 

                print('Thank you for entering details! Your Booking is confirmed. \nYour Order ID:' + str(self.order_id)) 

                break    

            except ValueError: 

                print('Please enter valid format !') 

  

class OrderOnline(Order): 

    def __init__(self): 

        super().__init__('OrderOnline') 

  

    def calculate_amount(self, selected_items): 

        total_price = sum(item.price for item in selected_items) 

        return total_price 

  

    def proceed_order(self): 

        print('Select your preferred option: \n1. Self-Pickup \n2. Home Delivery \n3. Go to Previous Menu') 

        while True: 

            option = input('Your Choice: ') 

            if option == '1': 

                self.self_pickup() 

                break 

            elif option == '2': 

                self.home_delivery() 

                break 

            elif option == '3': 

                print('Going back to the previous menu...') 

                return 

            else: 

                print('Invalid choice. Please enter 1, 2, or 3.') 

  

    def self_pickup(self): 

        print('Food Menu: ')  # Added food menu display 

        menu = Menu() 

        menu.display_food_menu() 

        print('Enter 7 for Food Check out') 

        selected_food_items = [] 

        while True: 

            select = input(': ') 

            if select == '7':  # Assuming '7' is the option to exit food selection 

                total_amount = self.calculate_amount(selected_food_items) 

                print('Your Order ID is', self.order_id + '. Your total payable amount is AUD' +str(total_amount) + '. No Additional Charges Applied.') 

                 

                break 

            elif select in ['1', '2', '3', '4', '5', '6']: 

                selected_food_items.append(menu.food_menu[int(select) - 1]) 

            else: 

                print('Please enter a valid option.') 

                self.checkout_order() 

                 

        while True: 

            try: 

                Date = input('Please enter the Date of Booking for Pick up (DD/MM/YYYY): ') 

                check = Date.split('/') 

                if len(check) != 3: 

                    print('Please enter the date in the correct format (DD/MM/YYYY).') 

                    continue 

                else: 

                    Time = input('Please enter the Time of Booking for Pick up (HH:MM): ') 

                    Persons = input('Please enter the Name of the Person: ') 

                break 

            except ValueError: 

                print('Please enter valid format!') 

        print('Thank you for entering detail! Your Booking is confirmed. Your Order ID is' + self.order_id) 

         

    def calculate_delivery_charge(self, distance): 

        if 0 <= distance <= 4: 

            delivery_charge = 3 

        elif 4 < distance <= 8: 

            delivery_charge = 6 

        elif 8 < distance <= 12: 

            delivery_charge = 10 

        else: 

            delivery_charge = None  # No delivery possible for distances over 12 KM 

        return delivery_charge  

  

    def home_delivery(self): 

        user = User('', '', '', '', '')  # Creating a dummy user object 

        if user.address is None or user.address == "": 

            print('You have not mentioned your address while signing up.') 

            proceed_address = input('Please enter Y if you would like to enter your address, or N to select another mode of order: ') 

  

            if proceed_address.upper() == 'Y': 

                address = input('Please enter your address: ') 

                user.address = address 

                print('Your Address has been added successfully.') 

            elif proceed_address.upper() == 'N': 

                self.proceed_order() 

                return 

            else: 

                print("Invalid input. Please enter valid command.") 

                return 

             

        print('Food Menu: ') 

        menu = Menu() 

        menu.display_food_menu() 

        print('Enter 7 for Food Check out') 

        selected_food_items = [] 

        while True: 

            select = input(': ') 

            if select == '7': 

                print('Your Order ID is', self.order_id + '.Thank you for selecting your foods.') 

                break 

            elif select in ['1', '2', '3', '4', '5', '6']: 

                selected_food_items.append(menu.food_menu[int(select) - 1]) 

            else: 

                print('Please enter a valid option.') 

                break 

         

        delivery_date = input('Please enter the Date of Delivery (DD/MM/YYYY): ') 

        delivery_time = input('Please enter the Time of Delivery (HH:MM): ') 

        distance = float(input('Please enter the distance from the restaurant (KM): ')) 

  

        if not self.validate_date(delivery_date): 

            print('Please enter a valid future date.') 

            return 

  

        if distance > 12: 

            print('Sorry, no delivery can be done for distances more than 12 KMs.') 

            pick_up_option = input('Would you like to change to pick up this order? (yes/no): ') 

            if pick_up_option.lower() == 'yes': 

                self.self_pickup() 

            elif pick_up_option.lower() == 'no': 

                print('Order has been cancelled !') 

            else: 

                print('Invalid input. Please enter yes or no.') 

        else: 

            # Calculate delivery charge 

            delivery_charge = self.calculate_delivery_charge(distance) 

            if delivery_charge is not None: 

                total_amount = self.calculate_amount(selected_food_items) + delivery_charge 

                print('Your Order ha been confirmed. Your Order ID is', self.order_id + '. Your total payable amount is AUD' +str(total_amount) + '. Including delivery charge of AUD ' + str(delivery_charge) +'.') 

                self.checkout_order() 

            else: 

                print('No delivery possible for distances over 12 KM.') 

  

    def validate_date(self, date_string): 

        try: 

            delivery_date = datetime.strptime(date_string, '%d/%m/%Y') 

            current_date = datetime.now() 

            return delivery_date >= current_date 

        except ValueError: 

            return False 

  

    def order_online(self): 

        while True: 

            option = input("Please select the order type:\n1 Self-Pickup\n2 Home Delivery\n3 Go to Previous Menu\nYour Choice: ") 

            if option == '1': 

                Order_Online_order = OrderOnline() 

                Order_Online_order.proceed_order() 

                break 

            elif option == '2': 

                OrderOnline().home_delivery() 

                break 

            elif option == '3': 

                self.login() 

                return 

            else: 

                print('Invalid choice. Please enter 1, 2, or 3.') 

  

class TransactionHistory: 

    def __init__(self): 

        self.transactions = [] 

  

    def add_transaction(self, transaction): 

        self.transactions.append(transaction) 

  

    def total_amount_spent(self, user_mobile_number=None): 

        total_spent = sum(transaction.amount_paid for transaction in self.transactions if user_mobile_number is None or transaction.mobile_number == user_mobile_number) 

        print(f"Total Amount Spent: ${total_spent:.2f}") 

  

    def view_transactions(self, user_mobile_number=None, order_type=None): 

        print("Transaction History:") 

        print("1. All Dine In Orders") 

        print("2. All Pickup Orders") 

        print("3. All Deliveries") 

        print("4. All Orders in Ascending Order (based on amount)") 

        print("5. Total Amount Spent (All Types of Orders)") 

        print("6. Go to Previous Menu") 

        option = input("Enter your choice: ") 

        if option == '1': 

            self.display_transactions(order_type="Dine In", user_mobile_number=user_mobile_number) 

            return 

        elif option == '2': 

            self.display_transactions(order_type="Pickup", user_mobile_number=user_mobile_number) 

            return 

        elif option == '3': 

            self.display_transactions(order_type="Delivery", user_mobile_number=user_mobile_number) 

            return 

        elif option == '4': 

            self.display_transactions(ascending=True, user_mobile_number=user_mobile_number) 

            return 

        elif option == '5': 

            self.total_amount_spent(user_mobile_number=user_mobile_number) 

            return 

        elif option == '6': 

            return 

        else: 

            print("Invalid choice. Please try again") 

  

    def display_transactions(self, order_type=None, user_mobile_number=None, ascending=False): 

        filtered_transactions = [transaction for transaction in self.transactions 

                                 if (order_type is None or transaction.order_type == order_type) 

                                 and (user_mobile_number is None or transaction.user_mobile_number == user_mobile_number)] 

        sorted_transactions = sorted(filtered_transactions, key=lambda x: x.amount_paid, reverse=not ascending) 

        print("Order ID\tDate\t\tTotal Amount Paid\tType of Order") 

        for transaction in sorted_transactions: 

            print(f"{transaction.order_id}\t\t{transaction.date}\t${transaction.amount_paid:.2f}\t\t{transaction.order_type}") 

  

             

def signup(): 

    while True: 

        print('Please enter your details to sign up:') 

        first_name = input('Enter your First Name: ').capitalize() 

        last_name = input('Enter your Last Name: ').capitalize() 

         

        mobile_attempts = 0 

        while mobile_attempts < 3: 

            mobile_number = input('Enter your 10 digit Mobile Number starting with 0: ') 

            if re.match('^0[1-9]\d{8}$', mobile_number): 

                break 

            print('Invalid Mobile Number. Please try again.') 

            mobile_attempts += 1 

        else: 

            print('You have reached maximum number of attempts for entering the mobile number. Please try again.') 

            continue 

         

        password_attempts = 0 

        while password_attempts < 3: 

            password = input('Enter your Password: ') 

            if re.match('^[a-zA-Z][a-zA-Z]*[@&#]\d+$', password): 

                password_confirmation = input('Confirm your Password: ') 

                if password_confirmation == password: 

                    break 

                else: 

                    print('Password confirmation does not match. Please try again.') 

            else: 

                print('Invalid password format. Please try again.') 

            password_attempts += 1 

        else: 

            print('You have reached maximum number of attempts for entering the password.') 

            continue 

         

        dob_attempts = 0  

        while dob_attempts < 3: 

            dob = input('Enter your Date of Birth (DD/MM/YYYY): ') 

            if len(dob) == 10 and dob[2] == '/' and dob[5] == '/': 

                day_str, month_str, year_str = dob.split('/') 

                day, month, year = int(day_str), int(month_str), int(year_str)   

             

                if not (1 <= day <= 31 and 1 <= month <= 12): 

                    print('Invalid Date of Birth. Please enter a valid Date of Birth. You have '  

                          + str(3 - dob_attempts -1) + ' attempts left.') 

                elif not (1900 <= int(year) <= 2024): 

                    print('Invalid year. Year must be between 1900 and 2024. You have '  

                          + str(3 - dob_attempts -1) + ' attempts left.') 

                else: 

                    break 

            else: 

                print('Invalid Date of Birth format. Please enter in DD/MM/YYYY format. You have '  

                      + str(3 - dob_attempts - 1) + ' attempts left.') 

            dob_attempts += 1 

        else: 

            print('You have reached maximum number of attempts for entering the date of birth. Try again.') 

            continue 

     

        # Calculate Age 

        age = User(first_name, last_name, mobile_number, password, dob).get_age() 

        if age < 21: 

            print('Your current age is', age,'years old. You must be at least 21 years old to sign up.', 

                  ' Sorry! You are not eligible for sign up.') 

            continue  # Restart the sign-up process if the user is not eligible 

  

        user_data = User(first_name, last_name, mobile_number, password, dob) 

        user_data_list.append(user_data) 

        print('Welcome' + first_name, last_name+'! You have Successfully Signed Up.') 

        break 

  

def login(): 

    while True: 

        mobile_number = input('Please enter your Username (Mobile Number): ') 

        password = input('Please enter your Password: ') 

  

        for user_data in user_data_list: 

            if user_data.mobile_number == mobile_number and user_data.password == password: 

                print('You have Successfully Signed In.') 

                while True: 

                    print('Please enter: \n2.1 to start ordering. \n2.2 to print statistics. \n2.3 for logout') 

                    option = input('Your Choice: ') 

                    if option == '2.1': 

                        print('Please Enter 1 for Dine in.\nPlease Enter 2 for Order Online.\nPlease enter 3 to go to Login Page.\n') 

                        order_type = input('Your Choice: ') 

                        if order_type == '1': 

                            dine_in_order = DineIn() 

                            if not dine_in_order.proceed_order(): 

                                break # Return to the main menu 

                            break 

                        elif order_type == '2': 

                            Order_Online_order = OrderOnline() 

                            if not Order_Online_order.proceed_order(): 

                                break  # Return to the main menu 

                            break 

                        elif order_type == '3': 

                            break 

                        else: 

                            print('Invalid Choice.') 

                    elif option == '2.2': 

                        transaction_history = TransactionHistory() 

                        transaction_history.view_transactions(order_type="All", user_mobile_number=mobile_number)  # Display transaction history for the user 

                        break 

                    elif option == '2.3': 

                        print('You have Successfully Signed Out.') 

                        return 

                    else: 

                        print('Invalid Choice. Please enter 2.1, 2.2, or 2.3.') 

  

                break 

        else: 

            print('Incorrect Username or Password. Please try again.') 

  

def main(): 

    while True: 

        print('Welcome to Restuarant App! \nPlease select the option:\n1 for Sign up \n2 for Sign in \n3 for Quit') 

  

        choice = input('Your Choice: ') 

  

        if choice == '1': 

            signup() 

        elif choice == '2': 

            login() 

        elif choice == '3': 

            print('Thank you for using the Application.') 

            break 

        else: 

            print('Invalid choice. Please enter a valid option 1, 2, or 3.') 

  

if __name__ == "__main__": 

    user_data_list = []  # List to store user data 

    transaction_history = TransactionHistory()  # Creating an instance of TransactionHistory 

    main()           