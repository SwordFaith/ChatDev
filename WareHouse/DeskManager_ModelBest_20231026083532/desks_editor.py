'''
This file contains the DesksEditor class which provides functionality related to desk management.
'''
import tkinter as tk
class DesksEditor:
    def __init__(self, root):
        self.root = root
        self.desks_canvas = tk.Canvas(self.root)
        self.desks_canvas.pack(fill=tk.BOTH, expand=True)
        self.desks = []
        self.selected_desks = []
        self.groups = []
    def place_desk(self, name, x, y):
        desk = Desk(name, x, y)
        self.desks.append(desk)
        desk.draw(self.desks_canvas)
    def select_desks(self, x1, y1, x2, y2):
        self.selected_desks = []
        for desk in self.desks:
            if x1 <= desk.x <= x2 and y1 <= desk.y <= y2:
                self.selected_desks.append(desk)
    def copy_desks(self):
        self.copied_desks = []
        for desk in self.selected_desks:
            self.copied_desks.append(desk)
    def paste_desks(self, x, y):
        for desk in self.copied_desks:
            new_desk = Desk(desk.name, x + desk.x, y + desk.y)
            self.desks.append(new_desk)
            new_desk.draw(self.desks_canvas)
    def label_desk(self, desk, name):
        desk.name = name
        self.desks_canvas.delete(desk.text_id)
        desk.draw(self.desks_canvas)
    def drag_desk(self, desk, x, y):
        desk.move(x, y)
        self.desks_canvas.delete(desk.shape_id)
        desk.draw(self.desks_canvas)
    def create_group(self, name):
        group = Group(name)
        self.groups.append(group)
    def add_desk_to_group(self, desk, group):
        group.add_desk(desk)
    def remove_desk_from_group(self, desk, group):
        group.remove_desk(desk)
    def draw_groups(self):
        for group in self.groups:
            group.draw(self.desks_canvas)
class Desk:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def move(self, x, y):
        self.x = x
        self.y = y
    def draw(self, canvas):
        self.shape_id = canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill="white")
        self.text_id = canvas.create_text(self.x + 25, self.y + 25, text=self.name)
class Group:
    def __init__(self, name):
        self.name = name
        self.desks = []
    def add_desk(self, desk):
        self.desks.append(desk)
    def remove_desk(self, desk):
        self.desks.remove(desk)
    def draw(self, canvas):
        for desk in self.desks:
            desk.draw(canvas)