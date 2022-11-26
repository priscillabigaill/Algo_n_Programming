from Account import Account
from Customer import Customer
from Bank import Bank

class ATM:

    def __init__(self,data):
        self.__DEBUG = False
        self.__data = data
        # self.__data = [
        #     {
        #         'fname': 'First1',
        #         'lname': 'Last1',
        #         'balance': 100000
        #     },
        #     {
        #         'fname': 'First2',
        #         'lname': 'Last2',
        #         'balance': 200000
        #     },
        #     {
        #         'fname': 'First3',
        #         'lname': 'Last3',
        #         'balance': 300000
        #     }
        # ]
        self.__authenticated_user_idx = None

        self.__bank = Bank("ABI BANK")
        for idx, data in enumerate(self.__data):
            self.__bank.addCustomer(data['fname'], data['lname'])
            self.__bank.getCustomer(idx).setAccount(Account(data['balance']))        

        self.__main_routine()


    def __main_routine(self):

        print(f"""
        #############################
        Welcome to {self.__bank._Bank__bName} ATM!!
        #############################
        """)

        self.__auth_routine()

        while(True):
            self.__main_menu_routine()


    def __auth_routine(self):
        
        prompt_str1 = """
        >> First Name: 
        """

        prompt_str2 = """
        >> Last Name: 
        """

        cred_fname = input(prompt_str1)
        cred_lname = input(prompt_str2)

        while not self.__check_cred_by_names(cred_fname,cred_lname):
            print("""
            Wrong credential! Please enter your credential again.
            """)

            cred_fname = input(prompt_str1)
            cred_lname = input(prompt_str2)

            if(self.__DEBUG):
                print(f"First name: {cred_fname}")
                print(f"Last name: {cred_lname}")

    def __check_cred_by_names(self,fname,lname):

        for idx, data in enumerate(self.__data):
            if fname == data['fname'] and lname == data['lname']:
                self.__authenticated_user_idx = idx
                return True

        return False

    def __main_menu_routine(self):

        main_menu_str = f"""
        What would you like to do? (input number)
        > (1) Check Balance
        > (2) Deposit
        > (3) Withdraw
        > (4) Exit
        """

        opt_number = input(main_menu_str)

        while opt_number not in ["1","2","3","4"]: 
            print("""
            Please try again.
            """)

            opt_number = input(main_menu_str)

        if opt_number == '1':
            print(f"""
            Your balance is: {self.__bank.getCustomer(self.__authenticated_user_idx).getAccount().getBalance()}
            """)

        elif opt_number == "2":
            deposit_amt = input("""
            Amount of deposit: 
            """)
            if self.__bank.getCustomer(self.__authenticated_user_idx).getAccount().deposit(int(deposit_amt)):
                print(f"""
            Your new balance is: {self.__bank.getCustomer(self.__authenticated_user_idx).getAccount().getBalance()}
            """)
            else:
                print("Invalid")
                
        elif opt_number == "3":
            withdrawal_amt = input("""
            Amount of withdrawal: 
            """)
            if self.__bank.getCustomer(self.__authenticated_user_idx).getAccount().withdraw(int(withdrawal_amt)):
                print(f"""
            Your remaining balance is: {self.__bank.getCustomer(self.__authenticated_user_idx).getAccount().getBalance()}
            """)
            else:
                print("Invalid")

        elif opt_number == "4":
            print("Thank you for using our ATM. Come back soon! :)")
            exit()


    def __check_cred_by_names(self,fname,lname):

        for idx, data in enumerate(self.__data):
            if fname == data['fname'] and lname == data['lname']:
                self.__authenticated_user_idx = idx
                return True

        return False


        
