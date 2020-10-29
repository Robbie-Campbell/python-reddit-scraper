from gui import Gui, ParseUrl

# Execute the parse url function
if __name__ == '__main__':
    get_titles = ParseUrl("http://reddit.com/r/news/")
    gui = Gui()
    gui.create_gui()

