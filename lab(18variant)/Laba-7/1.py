# Вариант 6
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog

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
        self.geometry("1600x600")

        self.data_frame = ttk.Frame(self)
        self.data_frame.pack(fill=tk.BOTH, expand=True)

        self.create_data_table()
        self.add_hierarchy_to_table()

        self.tree.bind("<Double-1>", self.on_item_double_click)

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

    def on_item_double_click(self, event):
        selected_items = self.tree.selection()
        if not selected_items:
            return
        
        item_id = selected_items[0]
        item_values = self.tree.item(item_id, "values")
        
        if item_values:
            edit_dialog = EditDialog(self, item_values)

            if edit_dialog.updated_values:
                self.tree.item(item_id, values=edit_dialog.updated_values)

class EditDialog(Dialog):
    def __init__(self, parent, item_values):
        self.item_values = item_values
        self.updated_values = None
        super().__init__(parent, "Edit Item")

    def body(self, master):
        ttk.Label(master, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(master, text="HP:").grid(row=1, column=0, padx=10, pady=5)
        ttk.Label(master, text="Attack:").grid(row=2, column=0, padx=10, pady=5)
        ttk.Label(master, text="Defense:").grid(row=3, column=0, padx=10, pady=5)
        ttk.Label(master, text="Range:").grid(row=4, column=0, padx=10, pady=5)
        ttk.Label(master, text="Cost:").grid(row=5, column=0, padx=10, pady=5)
        ttk.Label(master, text="Mana:").grid(row=6, column=0, padx=10, pady=5)

        self.name_entry = ttk.Entry(master)
        self.hp_entry = ttk.Entry(master)
        self.attack_entry = ttk.Entry(master)
        self.defense_entry = ttk.Entry(master)
        self.range_entry = ttk.Entry(master)
        self.cost_entry = ttk.Entry(master)
        self.mana_entry = ttk.Entry(master)

        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.hp_entry.grid(row=1, column=1, padx=10, pady=5)
        self.attack_entry.grid(row=2, column=1, padx=10, pady=5)
        self.defense_entry.grid(row=3, column=1, padx=10, pady=5)
        self.range_entry.grid(row=4, column=1, padx=10, pady=5)
        self.cost_entry.grid(row=5, column=1, padx=10, pady=5)
        self.mana_entry.grid(row=6, column=1, padx=10, pady=5)

        self.name_entry.insert(0, self.item_values[0])
        self.hp_entry.insert(0, self.item_values[1])
        self.attack_entry.insert(0, self.item_values[2])
        self.defense_entry.insert(0, self.item_values[3])
        self.range_entry.insert(0, self.item_values[4])
        self.cost_entry.insert(0, self.item_values[5])
        self.mana_entry.insert(0, self.item_values[6])

    def apply(self):
        self.updated_values = (
            self.name_entry.get(),
            self.hp_entry.get(),
            self.attack_entry.get(),
            self.defense_entry.get(),
            self.range_entry.get(),
            self.cost_entry.get(),
            self.mana_entry.get()
        )

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
