'''
This file contains the UsersEditor class for managing users.
'''
import csv
class UsersEditor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.users = []
        self.groups = []
    def assign_desk(self):
        # Code to assign a desk to a user or desks to a group of users
        pass
    def import_users(self):
        # Code to import users from excel/csv
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.users.append(row)