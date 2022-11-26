from Account import Account
from Customer import Customer
from Bank import Bank

class Admin:

    def __init__(self):
        
        self.data = []

        self.__main_routine()

    def __main_routine(self):

        print(f"""
        #############
        Welcome to Admin Page!
        #############
        """)

        self.__auth_routine()

        is_not_exit = True

        while(is_not_exit):
            is_not_exit = self.__main_menu_routine()
        
    def __auth_routine(self):
        
        pin_input = """
        >> PIN """

        pin = input(pin_input)

        while not self.__check_cred_by_pin(pin):
            print("""
            Wrong pin number! Please enter pin again.
            """)

            pin = input(pin_input)

    def __check_cred_by_pin(self,pin):

        if pin == "21M517008":
            return True

        return False

    def __main_menu_routine(self):

        main_menu_str = f"""
        What would you like to do? (input number)
        > (1) Add customer
        > (2) Delete customer
        > (3) Edit customer
        > (4) Search customer
        > (5) Exit
        """

        opt_number = input(main_menu_str)

        while opt_number not in ["1","2","3","4","5"]: 
            print("""
            Please try again.
            """)

            opt_number = input(main_menu_str)

        if opt_number == '1': #add cust
            
            fname = input("""
            Customer details:
            >> First Name:
            """)
            lname = input("""
            >> Last Name:
            """)
            balance = input("""
            >> Balance:
            """)

            self.data.append(
                {
                    'fname': fname,
                    'lname': lname,
                    'balance': int(balance)
                },
            )

            return True


        elif opt_number == "2": #delete cust
            deleted = input("""
            Which customer do you want to delete?: 
            """)

            del self.data[int(deleted)]

            return True
                
        elif opt_number == "3": #edit cust
            edited = input("""
            Which customer do you want to edit?: 
            """)
            
            if int(edited) > len(self.data)-1:
                print(f"""
                    There are only {len(self.data)} customers in our database.
                    Please enter a proper value!
                """)
            else: 

                fname = input("""
                New customer details:
                >> First Name:
                """)
                lname = input("""
                >> Last Name:
                """)
                balance = input("""
                >> Balance:
                """)

                self.data[int(edited)] = {
                        'fname': fname,
                        'lname': lname,
                        'balance': int(balance)
                    }

            return True
    

        elif opt_number == "4": #search cust
            for idx, data in enumerate(self.data):
                print(f"""
                    Customer ID-{idx}:
                        > First Name: {data['fname']}
                        > Last Name: {data['lname']}
                        > Balance: {data['balance']}
                """)
            return True

        elif opt_number == "5":
            print("""
            Thank you for your hard work! :)
            """)
            return False
        




