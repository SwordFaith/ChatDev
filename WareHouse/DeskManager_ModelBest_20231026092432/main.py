'''
This is the main file of the Work Desks Management System.
'''
from tkinter import Tk, Canvas, messagebox
class Desk:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
class User:
    def __init__(self, name):
        self.name = name
        self.desk = None
class Group:
    def __init__(self, name):
        self.name = name
        self.desks = []
class WorkDesksManagementSystem:
    def __init__(self):
        self.desks = []
        self.users = []
        self.groups = []
    def add_desk(self, name, x, y):
        desk = Desk(name, x, y)
        self.desks.append(desk)
    def add_user(self, name):
        user = User(name)
        self.users.append(user)
    def add_group(self, name):
        group = Group(name)
        self.groups.append(group)
    def assign_desk_to_user(self, desk_name, user_name):
        desk = next((desk for desk in self.desks if desk.name == desk_name), None)
        user = next((user for user in self.users if user.name == user_name), None)
        if desk and user:
            user.desk = desk
            messagebox.showinfo("Success", f"Desk '{desk_name}' assigned to user '{user_name}'")
        else:
            messagebox.showerror("Error", "Invalid desk or user name")
    def assign_desks_to_group(self, desk_names, group_name):
        group = next((group for group in self.groups if group.name == group_name), None)
        if group:
            desks = [desk for desk in self.desks if desk.name in desk_names]
            if len(desks) == len(desk_names):
                group.desks.extend(desks)
                messagebox.showinfo("Success", f"Desks assigned to group '{group_name}'")
            else:
                messagebox.showerror("Error", "Invalid desk name(s)")
        else:
            messagebox.showerror("Error", "Invalid group name")
    def visualize_desks(self):
        root = Tk()
        root.title("Work Desks Management System")
        canvas = Canvas(root, width=800, height=600)
        canvas.pack()
        def create_desk(desk):
            canvas.create_rectangle(desk.x, desk.y, desk.x + 50, desk.y + 50, fill="white")
            canvas.create_text(desk.x + 25, desk.y + 25, text=desk.name)
        for desk in self.desks:
            create_desk(desk)
        root.mainloop()
    def copy_desks(self, desk_names):
        desks_to_copy = [desk for desk in self.desks if desk.name in desk_names]
        for desk in desks_to_copy:
            self.add_desk(desk.name, desk.x, desk.y)
    def paste_desks(self, copied_desks):
        for desk in copied_desks:
            self.add_desk(desk.name, desk.x + 50, desk.y + 50)
    def run(self):
        self.visualize_desks()
if __name__ == "__main__":
    system = WorkDesksManagementSystem()
    system.add_desk("Desk 1", 100, 100)
    system.add_desk("Desk 2", 200, 200)
    system.add_user("User 1")
    system.add_user("User 2")
    system.add_group("Group 1")
    system.assign_desk_to_user("Desk 1", "User 1")
    system.assign_desks_to_group(["Desk 1", "Desk 2"], "Group 1")
    system.run()