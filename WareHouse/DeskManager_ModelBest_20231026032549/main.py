'''
This is the main file of the Work Desks Management System.
'''
from tkinter import Tk, Canvas, Button, Label, Entry, messagebox
from desks import DesksEditor
from users import UsersEditor
class WorkDesksManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Work Desks Management System")
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.desks_editor = DesksEditor(self.canvas)
        self.users_editor = UsersEditor(self.canvas)
        self.create_buttons()
    def create_buttons(self):
        self.place_desk_button = Button(self.root, text="Place Desk", command=self.desks_editor.place_desk)
        self.place_desk_button.pack(side="left")
        self.copy_button = Button(self.root, text="Copy", command=self.desks_editor.copy)
        self.copy_button.pack(side="left")
        self.paste_button = Button(self.root, text="Paste", command=self.desks_editor.paste)
        self.paste_button.pack(side="left")
        self.label_button = Button(self.root, text="Label", command=self.desks_editor.label)
        self.label_button.pack(side="left")
        self.assign_desk_button = Button(self.root, text="Assign Desk", command=self.users_editor.assign_desk)
        self.assign_desk_button.pack(side="left")
        self.import_button = Button(self.root, text="Import", command=self.users_editor.import_users)
        self.import_button.pack(side="left")
root = Tk()
app = WorkDesksManagementSystem(root)
root.mainloop()