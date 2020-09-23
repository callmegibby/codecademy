import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.yo = tk.Button(self, text="yo", command=self.sayyo)
        self.yo.pack(side="bottom")

        self.quit = tk.Button(self,
                              text="QUIT",
                              fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def sayyo(self):
        print("yo")
        self.age = tk.Button(self, text="age", command=self.age)
        self.age.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        # do something

    def age(self):
        master = tk.Tk()
        tk.Label(master, text="What is your age?").grid(row=0)
        entry1 = tk.Entry(master)
        entry1.grid(row=0, column=1)
        age = entry1
        self.submit = tk.Button(self, text="Submit", command=self.play)

    def play(self):
        master = tk.Tk()
        tk.Label(master, text="Do you want to play").grid(row=0)
        entry1 = tk.Entry(master)
        entry1.grid(row=0, column=1)
        age = entry1
        self.yo = tk.Button(self, text="Close", command=self.play)
        self.yo.pack(side="bottom")


root = tk.Tk()
app = Application(master=root)
app.mainloop()