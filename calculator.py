from lib import *
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

        # https://stackoverflow.com/a/4140988
        inputValidate = self.root.register(self.onValidate)
        self.input = Entry(self.frame, bg="#8395a7", textvariable=self.inputValue, validate="key", justify='right', validatecommand=(inputValidate, "%P"))
        self.input.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=4)

        self.buttonsFrame = Frame(self.frame, bg="#fff")

        self.buttonsFrame.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5, rowspan=5, columnspan=4)

        self.createButtons()
        self.buttonsGrid()

    def onValidate(self, value):
        if re.search("[^\^0-9,/*%+\-√()]+", value):
            return(False)
        else:
            return(True)

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

    def getButton(self, symbol, row, column, name):
        functionCall = eval("CommandList."+name)
        button = Button(self.buttonsFrame, text=symbol, font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1", command= lambda: functionCall(self.inputValue)).grid(row=row, column=column, sticky=N+S+E+W)
        return(button)

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
            self.buttons.append(self.getButton(data["symbol"], data["row"], data["column"], button))

if __name__ == '__main__':
    calculator = App(root)
    root.mainloop()
