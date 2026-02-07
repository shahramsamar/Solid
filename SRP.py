# without solid -SRP

class UserHandler:
    def __init__(self):
        self.users = []

    def register_user(self, name, age, email):
        user = {"name": name, "age": age, "email": email}
        self.users.append(user)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for user in self.users:
                f.write(f"{user['name']},{user['age']},{user['email']}\n")

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            self.users = [self._parse_line(line) for line in f.readlines()]

    def _parse_line(self, line):
        name, age, email = line.strip().split(',')
        return {"name": name, "age": age, "email": email}

    def display_users(self):
        for user in self.users:
            print(f"Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")


# solid - SRP

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self, name, age, email):
        user = User(name, age, email)
        self.users.append(user)

    def display_users(self):
        for user in self.users:
            print(f"Name: {user.name}, Age: {user.age}, Email: {user.email}")

class UserFileHandler:
    @staticmethod
    def save_to_file(users, filename):
        with open(filename, 'w') as f:
            for user in users:
                f.write(f"{user.name},{user.age},{user.email}\n")

    @staticmethod
    def read_from_file(filename):
        users = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                name, age, email = line.strip().split(',')
                users.append(User(name, age, email))
        return users

