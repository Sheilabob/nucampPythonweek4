class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        if len(new_name) < 2 or len(new_name) > 10:
            print(
                "User name was not changed: all user names must be between 2 and 10 characters.")
        else:
            self.name = new_name

    def change_pin(self, new_pin):
        if len(str(new_pin)) != 4:
            print(
                "Pin was not changed: all pins must be 4 numbers in length.")
        elif new_pin == self.pin:
            print("Error: you cannot reuse a PIN.")
            return
        else:
            self.pin = new_pin

    def change_password(self, new_password):
        if len(new_password) < 5 or ' ' in new_password:
            print(
                "Password was not changed: all passwords must be greater than 5 characters and cannot contain spaces.")
        elif new_password == self.password:
            print("Error: you cannot reuse a password.")
            return
        else:
            self.password = new_password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def toggle_hold(self):
        self.on_hold = not self.on_hold

    def show_balance(self):
        formatted_balance = "{:.2f}".format(self.balance)
        print(f"{self.name}'s balance is: ${formatted_balance}")

    def withdraw(self, amount):
        if self.on_hold == True:
            print(
                "Sorry: this transaction cannot be completed at this time.  Please try again later.")
            return False

        if type(amount) != int and type(amount) != float or amount <= 0:
            print(f"Please enter a valid amount greater than zero.")
        elif amount > self.balance:
            print(f"Please enter an amount less than your account balance.")
        else:
            self.balance -= amount

    def deposit(self, amount):
        if self.on_hold == True:
            print(
                "Sorry: this transaction cannot be completed at this time.  Please try again later.")
            return False

        if type(amount) != int and type(amount) != float or amount <= 0:
            print("Please enter a valid amount greater than zero.")
        else:
            self.balance += amount

    def transfer_money(self, amount, target):
        formatted_amount = "{:.2f}".format(amount)

        if self.on_hold == True or target.on_hold == True:
            print(
                "Sorry: this transaction cannot be completed at this time.  Please try again later.")
            return False

        if type(amount) != int and type(amount) != float or amount <= 0:
            print(f"Please enter a valid transfer amount greater than zero.")
        elif amount > self.balance:
            print(f"Please enter an amount less than your account balance.")
        else:
            print("\nYou are transferring $",
                  formatted_amount, "to", target.name)
            print("Authentication required")

            access_pin = input("Enter your PIN:\t")
            if access_pin == self.pin:
                print("Tranfer authorized")
                print("Transferring $", formatted_amount, "to", target.name)
                self.withdraw(amount)
                target.deposit(amount)
            else:
                print("Invalid PIN. Transaction canceled.")
                self.show_balance()
                target.show_balance()
                return False
            self.show_balance()
            target.show_balance()
            return True

    def request_money(self, amount, origin):
        formatted_amount = "{:.2f}".format(amount)

        if self.on_hold == True or origin.on_hold == True:
            print(
                "Sorry: this transaction cannot be completed at this time.  Please try again later.")
            return False

        if type(amount) != int and type(amount) != float or amount <= 0:
            print("Please enter a valid request amount greater than zero.")
        elif amount > origin.balance:
            print(f"Please enter an amount less than {origin.name}'s balance.")
        else:

            print(
                f"\nYou are requesting ${formatted_amount} from", origin.name)
            print("User authentication is required . . .")

            request_pin = input(f"Enter {origin.name}'s PIN:\t")
            if request_pin == origin.pin:
                access_password = input("Enter your password:\t")
                if access_password == self.password:
                    print("Request authorized")
                    print(origin.name, "sent $", formatted_amount)
                    self.deposit(amount)
                    origin.withdraw(amount)
                else:
                    print("Invalid password. Transaction canceled.")
                    self.show_balance()
                    origin.show_balance()
                    return False
            else:
                print("Invalid PIN. Transaction canceled.")
                self.show_balance()
                origin.show_balance()
                return False
            self.show_balance()
            origin.show_balance()
            return True


# Driver Code for Task 1
# user = User("Bob", 1234, "password")
# print(f"{user.name} {user.pin} {user.password}")


# Driver Code for Task 2
# user = User("Bob", 1234, "password")
# print(f"{user.name} {user.pin} {user.password}")
# user.change_name("Bobby")
# user.change_pin(4321)
# user.change_password("newpassword")
# print(f"{user.name} {user.pin} {user.password}")

# Driver Code for Task 3
# bank_user = BankUser("Bob", 1234, "password")
# print(f"{bank_user.name} {bank_user.pin} {bank_user.password} {bank_user.balance}")

# Driver Code for Task 4
# bank_user = BankUser("Bob", 1234, "password")
# # print(f"{bank_user.name} {bank_user.pin} {bank_user.password} {bank_user.balance}")
# bank_user.show_balance()
# bank_user.deposit(1000)
# bank_user.show_balance()
# bank_user.withdraw(500)
# bank_user.show_balance()

# Driver Code for Task 5
# user1 = BankUser("Bob", "1234", "password")
# user2 = BankUser("Alice", "5678", "apassword")
# user2.deposit(5000)
# user1.show_balance()
# user2.show_balance()
# transfer = user2.transfer_money(500, user1)
# user2.toggle_hold()
# if transfer == True:
#     user2.request_money(250, user1)
