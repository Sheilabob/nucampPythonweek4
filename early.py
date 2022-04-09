class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print(self.name, "has an account balance of:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(self.name, "has an account balance of:", self.balance)

    def transfer_money(self, amount, target):
        print("\nYou are transferring $", amount, "to", target.name)
        print("Authentication required")

        access_pin = input("Enter your PIN:\t")
        if access_pin == self.pin:
            print("Tranfer authorized")
            print("Transferring $", amount, "to", target.name)
            self.balance -= amount
            target.balance += amount
        else:
            print("Invalid PIN. Transaction canceled.")
            print(self.name, "has a balance of:", self.balance)
            print(target.name, "has a balance of:", target.balance)
            return False
        print(self.name, "has a balance of:", self.balance)
        print(target.name, "has a balance of:", target.balance)
        return True

    def request_money(self, amount, target):
        print(f"\nYou are requesting ${amount} from", target.name)
        print("User authentication is required . . .")

        request_pin = input(f"Enter {target.name}'s PIN:\t")
        if request_pin == target.pin:
            access_password = input("Enter your password:\t")
            if access_password == self.password:
                print("Request authorized")
                print(target.name, "sent $", amount)
                self.balance += amount
                target.balance -= amount
            else:
                print("Invalid password. Transaction canceled.")
                print(self.name, "has a balance of:", self.balance)
                print(target.name, "has a balance of:", target.balance)
                return False
        else:
            print("Invalid PIN. Transaction canceled.")
            print(self.name, "has a balance of:", self.balance)
            print(target.name, "has a balance of:", target.balance)
            return False
        print(self.name, "has a balance of:", self.balance)
        print(target.name, "has a balance of:", target.balance)
        return True

# Driver Code for Task 1
# user1 = User("Bob", "1234", "password")
# print(user1.name, user1.pin, user1.password)

# Driver Code for Task 2
# user1 = User("Bob", "1234", "password")
# print(user1.name, user1.pin, user1.password)
# user1.change_name("Bobby")
# user1.change_pin("4321")
# user1.change_password("newpassword")
# print(user1.name, user1.pin, user1.password)

# Driver Code for Task 3
# bankuser1 = BankUser("Bob", "1234", "password")
# print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)

# Driver Code for Task 4
# bankuser1 = BankUser("Bob", "1234", "password")
# bankuser1.show_balance()
# bankuser1.deposit(1000)
# bankuser1.withdraw(500)


# Driver Code for Task 5
user1 = BankUser("Bob", "1234", "password")
user2 = BankUser("Alice", "5678", "apassword")
user2.deposit(5000)
user1.show_balance()
if user2.transfer_money(500, user1) == True:
    user2.request_money(250, user1)
