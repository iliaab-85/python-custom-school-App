from pl.form import School

from tkinter import *

if __name__ == "__main__":
    screen = Tk()
    screen.geometry("%dx%d+%d+%d" % (800, 600, 400, 100))
    screen.title("مدرسه")
    screen.iconbitmap("icon.ico")
    screen.resizable(False, False)
    PageMe = School.App(screen)
    screen.mainloop()