#from lib.py import *
from tkinter import *
import json
import os

root = Tk();

class App:
    def __init__(self, root):
        self.root = root

        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)

        self.root.geometry("500x600")

        self.root.title("Kalkulačka")

        self.root.minsize(250, 300)
        # self.root.maxsize(750, 900)

        self.buttons = []

        self.frame = Frame(self.root, bg="#fefefe")
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)

        self.frameGrid()

        self.inputValue = StringVar()
        self.input = Entry(self.frame, bg="#efbfef", textvariable=self.inputValue, justify='right')
        self.input.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=4)

        self.buttonsFrame = Frame(self.frame, bg="#fff")

        self.buttonsFrame.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5, rowspan=5, columnspan=4)

        self.createButtons()
        self.buttonsGrid()

    def frameGrid(self):
        for x in range(4):
            Grid.columnconfigure(self.frame, x, weight=1)
        for y in range(6):
            Grid.rowconfigure(self.frame, y, weight=1)

    def buttonsGrid(self):
        for x in range(4):
            Grid.columnconfigure(self.buttonsFrame, x, weight=1)
        for y in range(6):
            Grid.rowconfigure(self.buttonsFrame, y, weight=1)

    def createButtons(self):
        # otevření json souboru s tlačítky
        try:
            buttonsJSON = open("buttons.json", "r")
        except:
            print("[ERROR] Nebyl nalezen soubor s tlačítky - buttons.json.\nUkončuji program.")
            exit()

        buttonsData = json.load(buttonsJSON)
        for button in buttonsData:
            data = buttonsData[button]
            self.buttons.append(Button(self.buttonsFrame, text=data["symbol"], font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1").grid(row=data["row"], column=data["column"], sticky=N+S+E+W))

if __name__ == '__main__':
    calculator = App(root)
    root.mainloop()
