
class UsersRepository:
    def __init__(self):
        self.users_db = {}

    def get_user_by_email(self, email: str):
        return self.users_db.get(email)

    def create_user(self, email: str, full_name: str, password: str):
        if email in self.users_db:
            raise ValueError(f"User with email {email} already exists.")
        self.users_db[email] = {"full_name": full_name, "password": password}
        return self.users_db[email]


