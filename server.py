import sqlite3



class Database:

    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()


    def user_validation(self, username, password):

        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.cursor.fetchone()
        self.conn.close()


        if user is None:
            # User not found
            return False
        else:
            # User has been found
            return user[1]
        
