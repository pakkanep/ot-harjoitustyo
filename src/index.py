from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Job application search")
    window.geometry("600x600")

    userinterface= UI(window)
    userinterface.start()

    window.mainloop()


if __name__ == "__main__":
    main()
