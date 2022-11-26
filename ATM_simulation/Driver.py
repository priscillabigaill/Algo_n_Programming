from Account import Account
from Customer import Customer
from Bank import Bank

def main():
    b1 = Bank("BCA")
    
    #adding a customer to the bank
    b1.addCustomer("Laplace", "AnyLastName")
    b1.addCustomer("Andrew", "Tanenbaum")
    b1.addCustomer("Vania", "Vanilla")
    
    #getting the total number of customers
    print(b1.getNumOfCust())
    
    #accessing info of a customer
    print(b1.getCustomer(2).getFirstName())
    print(b1.getCustomer(2).getLastName())
    
    #deposit
    b1.getCustomer(2).setAccount(Account(500000))
    
    print(b1.getCustomer(2).getAccount().getBalance())
    
    if b1.getCustomer(2).getAccount().deposit(1000000):
        print(b1.getCustomer(2).getAccount().getBalance())
    else:
        print("Invalid")

    #withdraw
    b1.getCustomer(2).setAccount(Account(500000))
    
    print(b1.getCustomer(2).getAccount().getBalance())
    
    if b1.getCustomer(2).getAccount().withdraw(1000000):
        print(b1.getCustomer(2).getAccount().getBalance())
    else:
        print("Invalid")
    
        


    
    
    
if __name__ == "__main__":
    main()
    