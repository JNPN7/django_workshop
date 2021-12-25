from itertools import count
# We will be assigning a number as account number. It will be incremental.

accounts = {}

class Account:

    count = count(start=1) # [1,2,3,4,5,6........]
    
    def __init__(self, name, balance, pin):
        ac_n = next(self.count)
        self.ac_n = ac_n
        self.name = name
        self.balance = balance
        self.pin = pin

        # stores objects in dictonary
        accounts[ac_n] = self # x get/change => x.property_name 

        print(f"Congrats {name}, your account has been opened. Your account number is {ac_n} and your pin is {pin}")

    def change_pin(self, old_pin ,new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
        else:
            print("Your old pin is invalid")

    def __str__(self):
        return f"Account No: {self.ac_n}. Name: {self.name}"

    def transfer(self, pin, receiver_name, reciever_ac_no , amount):
        if pin == self.pin:
            if accounts.get(reciever_ac_no):
                receiver = accounts.get(reciever_ac_no)
                if self.balance >= amount:
                    if (receiver_name == receiver.name):
                        if (self.ac_n != reciever_ac_no):
                            self.balance -= amount
                            receiver.balance += amount
                            print(f"Your transfer has been successful. Your new balance is Rs {self.balance}.")
                        else:
                            print("You can't transfer money to your own account")
                    else:
                        print("Receiver name isn't correct")
                else:
                    print("Your balance isn't enough")
            else:
                print("Receiver account doesn't exits")
        else:
            print("Pin in invalid")

my = Account(name='Aashish', balance=1500, pin=123)
your = Account(name='Abisam', balance=2000, pin=362)


my.transfer(pin=123, receiver_name="Abisam", reciever_ac_no=2, amount=1200)

print("My balance= ", my.balance)
print("Your balance= ", your.balance)

# check if pin is correct
# check if reciever exists
# check if enough balance
# check if reciever's account number and name match


# Assignment: Put a validation to check own account and print("You can't transfer to self.")