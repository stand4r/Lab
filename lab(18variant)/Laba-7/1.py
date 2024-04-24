# Вариант 6
import tkinter as tk
from tkinter import ttk

class Object:
    def __init__(self, name, hp, attack, defense, range_, cost):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.range = range_
        self.cost = cost

class Building(Object):
    def __init__(self, name, hp, attack, defense, range_, cost):
        super().__init__(name, hp, attack, defense, range_, cost)

class WatchTower(Building):
    def __init__(self):
        super().__init__("WatchTower", 800, "15-20", 5, 1, 600)

class GuardTower(WatchTower):
    def __init__(self):
        super().__init__()
        self.name = "GuardTower"

class CannonTower(WatchTower):
    def __init__(self):
        super().__init__()
        self.name = "CannonTower"

class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Units and Buildings")
        self.geometry("800x600")

        self.data_frame = ttk.Frame(self)
        self.data_frame.pack(fill=tk.BOTH, expand=True)

        self.create_data_table()
        self.add_hierarchy_to_table()

    def create_data_table(self):
        self.tree = ttk.Treeview(self.data_frame, columns=("Name", "HP", "Attack", "Defense", "Range", "Cost", "Mana"))
        self.tree.heading("#0", text="Type")
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="HP")
        self.tree.heading("#3", text="Attack")
        self.tree.heading("#4", text="Defense")
        self.tree.heading("#5", text="Range")
        self.tree.heading("#6", text="Cost")
        self.tree.heading("#7", text="Mana")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def add_building_to_table(self, building):
        self.tree.insert("", "end", text="Building", values=(building.name, building.hp, building.attack, building.defense, building.range, building.cost, "-"))

    def add_hierarchy_to_table(self):
        object_id = self.tree.insert("", "end", text="Object")
        building_id = self.tree.insert("", "end", text="Building", values=("", "", "", "", "", "", ""))
        self.tree.insert(object_id, "end", text="WatchTower", values=("WatchTower", 800, "15-20", 5, 1, 600, "-"))
        self.tree.insert(building_id, "end", text="GuardTower", values=("GuardTower", 800, "15-20", 5, 1, 600, "-"))
        self.tree.insert(building_id, "end", text="CannonTower", values=("CannonTower", 800, "15-20", 5, 1, 600, "-"))

app = GameApp()
app.mainloop()
