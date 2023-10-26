'''
This is the main file of the Work Desks Management System.
'''
import tkinter as tk
from tkinter import messagebox
from desks_editor import DesksEditor
from users_editor import UsersEditor
class WorkDesksManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Work Desks Management System")
        self.root.geometry("800x600")
        self.desks_editor = DesksEditor(self.root)
        self.users_editor = UsersEditor(self.root)
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.exit_application)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)
    def run(self):
        self.root.mainloop()
    def exit_application(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()
if __name__ == "__main__":
    app = WorkDesksManagementSystem()
    app.run()