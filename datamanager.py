# data_manager.py
import shelve
from user import User
from post import Post

class DataManager:
    def __init__(self, filename="social_media_data"):
        self.filename = filename

    def save_data(self, users):
        with shelve.open(self.filename) as db:
            for user in users:
                db[user.username] = user

    def load_data(self):
        users = []
        with shelve.open(self.filename) as db:
            for username in db:
                users.append(db[username])
        return users

    def clear_data(self):
        with shelve.open(self.filename) as db:
            db.clear()
