#tkinter boilerplate code
import tkinter as tk
from tkinter import ttk
from Api.food import Nosalty
window = tk.Tk()
window.geometry("300x200")
window.title("Nosalty API")
api = Nosalty()

class App:
    def __init__(self, master):
        self.master = master

        self.label = tk.Label(master, text="Nosalty API",font=("Arial", 25))
        self.label.pack()
        self.button = tk.Button(master, text="Quit", command=master.quit)
        self.button.pack()
        self.food = tk.Entry(master)
        self.food.pack()
        self.fetch = tk.Button(master, text="Fetch", command=self.fetchData)
        self.fetch.pack()
        
    def fetchData(self):
        
        table_window = tk.Tk()
        self.fetch = ttk.Treeview(table_window)
        self.fetch["columns"] = ("Title", "Url")
        self.fetch.heading("Title", text="Title")
        self.fetch.heading("Url", text="Url")
        
        self.fetch.column("Title", width=500, minwidth=200, stretch=tk.NO)
        self.fetch.column("Url", width=500, minwidth=200, stretch=tk.NO)
        

 
            
        self.fetch.pack()
        
    def run(self):
        self.master.mainloop()
        
app = App(window)
app.run()
