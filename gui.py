#tkinter boilerplate code
import tkinter as tk
import Api.food as api
window = tk.Tk()
window.geometry("800x600")
window.title("Nosalty API")

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
        self.fetch = tk.Label(self.master, text=str(api.Nosalty().fetchFood(self.food.get())))
        self.fetch.pack()
    def run(self):
        self.master.mainloop()
        
app = App(window)
app.run()
