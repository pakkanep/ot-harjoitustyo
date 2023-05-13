from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Instance search")
    window.geometry("1000x1000")

    userinterface= UI(window)
    userinterface.start()

    window.mainloop()


if __name__ == "__main__":
    main()
