import tkinter as tk
import webbrowser


def web_lookup(url):
    webbrowser.open_new(url)


class Gui:
    def __init__(self, titles, **kw):
        self.titles = titles
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.configure(background="#555")
        self.root.title("R/News")
        self.root.frame = tk.Frame(master=self.root, bg="#555")
        self.panel = tk.PanedWindow()
        self.root.frame.place(relx=.5, rely=.5, anchor="c")

    def position_root(self):
        w = 800  # width for the Tk root
        h = 600  # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def create_titles(self):
        for key in self.titles:
            tk.Label(self.root.frame, text=key + "\n", bg="#555", fg="#DDD").pack()
            tk.Button(self.root.frame, text="Click To Find Out More", bg="#400", fg="#DDD", command=lambda: web_lookup(self.titles[key])).pack()
            print(self.titles[key])

    def create_gui(self):
        self.position_root()
        self.create_titles()
        self.root.mainloop()
        self.root.quit()

