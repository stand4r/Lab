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

class Unit(Object):
    def __init__(self, name, hp, attack, defense, range_, cost):
        super().__init__(name, hp, attack, defense, range_, cost)

class TrollAxethrower(Unit):
    def __init__(self):
        super().__init__("TrollAxethrower", 250, "25-30", 10, 2, 300)

class TrollBerserker(Unit):
    def __init__(self):
        super().__init__("TrollBerserker", 400, "30-35", 15, 1, 500)

class Dragon(Unit):
    def __init__(self):
        super().__init__("Dragon", 1000, "50-60", 20, 3, 1500)

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

    def add_unit_to_table(self, unit):
        self.tree.insert("", "end", text="Unit", values=(unit.name, unit.hp, unit.attack, unit.defense, unit.range, unit.cost, "-"))

    def add_hierarchy_to_table(self):
        object_id = self.tree.insert("", "end", text="Object")
        unit_id = self.tree.insert("", "end", text="Unit", values=("", "", "", "", "", "", ""))
        
        troll_axethrower = TrollAxethrower()
        troll_berserker = TrollBerserker()
        dragon = Dragon()
        
        self.add_unit_to_table(troll_axethrower)
        self.add_unit_to_table(troll_berserker)
        self.add_unit_to_table(dragon)


app = GameApp()
app.mainloop()
