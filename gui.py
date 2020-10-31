import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import ImageTk
from logic import ParseUrl
import webbrowser


# Search for the reddit post
def web_lookup(url):
    webbrowser.open_new(url)


# Initialise the frame widget and create new vars
class Gui:
    def __init__(self, **kw):
        self.titles = ParseUrl("http://reddit.com/r/news").titles
        self.root = tk.Tk()
        self.font = Font(family="helvetica", size=9, weight="bold")
        self.root.resizable(False, False)
        self.root.configure(background="#555")
        self.root.title("Reddit Top News Posts")
        self.frame = tk.Frame(master=self.root, bg="#555")
        self.frame.pack()
        self.panel = tk.PanedWindow()
        self.frame.place(relx=.5, rely=.6, anchor="c")
        self.canvas = tk.Canvas(self.root, width=800, height=100, bg="#000")
        self.canvas.pack()
        self.image = ImageTk.PhotoImage(file="banner.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)

    def position_root(self):
        w = 500  # width for the Tk root
        h = 400  # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Create the title and link button for all of the reddit posts
    # ________________ SIDE NOTE, USING A LOOP DID NOT WORK HERE: HENCE THE JANKY CODE __________________#
    def create_titles(self):
        if len(self.titles) == 0:
            tk.Label(self.frame, text="There were no posts associated with that search.").pack()
        else:
            tk.Label(self.frame, font=self.font, text=list(self.titles.keys())[0] + "\n", bg="#555", fg="#DDD",
                     wraplength=500).pack()
            tk.Button(self.frame, font=self.font, pady=0, text="Click To Find Out More", bg="#400", fg="#DDD",
                      command=lambda: web_lookup(list(self.titles.values())[0])).pack()
            tk.Label(self.frame, font=self.font, text=list(self.titles.keys())[1] + "\n", bg="#555", fg="#DDD",
                     wraplength=500).pack()
            tk.Button(self.frame, font=self.font, pady=0, text="Click To Find Out More", bg="#400", fg="#DDD",
                      command=lambda: web_lookup(list(self.titles.values())[1])).pack()
            tk.Label(self.frame, font=self.font, text=list(self.titles.keys())[2] + "\n", bg="#555", fg="#DDD",
                     wraplength=500).pack()
            tk.Button(self.frame, font=self.font, pady=0, text="Click To Find Out More", bg="#400", fg="#DDD",
                      command=lambda: web_lookup(list(self.titles.values())[2])).pack()

    # Search for new reddit posts, link to the logic and update the dictionary, also refresh current screen
    def search(self, url):
        self.titles = ParseUrl("http://reddit.com/r/" + url).titles
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.root.title("Reddit Top {} Posts".format(url))
        self.create_titles()
        self.search_for_more()

    # Add a search button to go on a different reddit page
    def search_for_more(self):
        new_search = tk.StringVar()
        tk.Label(self.frame, bg="#555", fg="#DDD", pady=4, text="Search for a different subreddit?", font=self.font).pack()
        ttk.Entry(self.frame, width=50, textvariable=new_search).pack()
        tk.Button(self.frame, bg="#555", fg="#DDD", font=self.font, text="search", padx=131, pady=5,
                  command=lambda: self.search(str(new_search.get()))).pack()

    # Create the GUI
    def create_gui(self):
        self.position_root()
        self.create_titles()
        self.search_for_more()
        self.root.mainloop()
        self.root.quit()

