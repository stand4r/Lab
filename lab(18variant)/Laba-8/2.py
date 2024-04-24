# Вариант 3
import tkinter as tk
import threading
import random
import time
from queue import Queue, Empty

class AuctionSimulation:
    def __init__(self, event_queue, root):
        self.event_queue = event_queue
        self.root = root

    def start_sim(self):
        for i in range(3):  
            threading.Thread(target=self.start_auc, args=(f"Аукцион {i+1}",)).start()

    def start_auc(self, auction_id):
        start_time = time.time()
        while time.time() - start_time < 15:
            event_type = random.choice(['старт', 'лот', 'ставка', 'продажа'])
            timestamp = time.time()  
            if event_type == 'старт':
                self.event_queue.put((timestamp, 'старт', auction_id, None, None, None))
            elif event_type == 'лот':
                lot_id = random.randint(1, 5)
                self.event_queue.put((timestamp, 'лот', auction_id, lot_id, None, None))
            elif event_type == 'ставка':
                lot_id = random.randint(1, 5)
                participant_id = random.randint(1, 10)
                bid = random.randint(50, 500)
                self.event_queue.put((timestamp, 'ставка', auction_id, lot_id, participant_id, bid))
            elif event_type == 'продажа':
                lot_id = random.randint(1, 5)
                participant_id = random.randint(1, 10)
                self.event_queue.put((timestamp, 'продажа', auction_id, lot_id, participant_id, None))
            time.sleep(random.uniform(0.1, 0.5))

def update_gui():
    while True:
        try:
            event = event_queue.get_nowait()
            update_event_display(event)
            event_queue.task_done()
        except Empty:
            break
    root.after(1000, update_gui)

def update_event_display(event):
    auction_id = event[2]
    timestamp = f"{event[0]:.2f}"
    event_type = event[1]
    lot_id = event[3] if event[3] is not None else "-"
    participant_id = event[4] if event[4] is not None else "-"
    bid = event[5] if event[5] is not None else "-"

    text = f"{timestamp:<10} {event_type:<10} {auction_id:<15} {lot_id:<10} {participant_id:<15} {bid:<10}\n"
    if auction_id in auction_frames:
        auction_text_widgets[auction_id].delete(1.0, tk.END)
        auction_text_widgets[auction_id].insert(tk.END, text)

root = tk.Tk()
root.title("Аукцион")

auction_frames = {}
auction_text_widgets = {}
for auction_id in ['Аукцион 1', 'Аукцион 2', 'Аукцион 3']:
    frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
    frame.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.BOTH)
    tk.Label(frame, text=f"{auction_id} События").pack()
    text_widget = tk.Text(frame, wrap=tk.WORD, height=20, width=50)
    text_widget.pack(fill=tk.BOTH, expand=True)
    auction_frames[auction_id] = frame
    auction_text_widgets[auction_id] = text_widget

event_queue = Queue()
auction_simulation = AuctionSimulation(event_queue, root)
auction_simulation.start_sim()

update_gui()

root.mainloop()
