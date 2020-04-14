#from lib.py import *
from tkinter import *

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

        self.frame = Frame(self.root, bg="#fefefe")
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)

        self.frameGrid()

        self.inputValue = StringVar()
        self.input = Entry(self.frame, bg="#efbfef", textvariable=self.inputValue, justify='right')
        self.input.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=4)

        self.buttonsFrame = Frame(self.frame, bg="#fff")

        self.buttonsFrame.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5, rowspan=5, columnspan=4)

        buttonModulo = Button(self.buttonsFrame, text="%", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonModulo.grid(row=0, column=0, sticky=N+S+E+W)

        buttonNthRoot = Button(self.buttonsFrame, text="√", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonNthRoot.grid(row=0, column=1, sticky=N+S+E+W)

        buttonPower = Button(self.buttonsFrame, text="x^2", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonPower.grid(row=0, column=2, sticky=N+S+E+W)

        buttonInversion = Button(self.buttonsFrame, text="1/x", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonInversion.grid(row=0, column=3, sticky=N+S+E+W)

        buttonCE = Button(self.buttonsFrame, text="CE", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonCE.grid(row=1, column=0, sticky=N+S+E+W)

        buttonC = Button(self.buttonsFrame, text="C", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonC.grid(row=1, column=1, sticky=N+S+E+W)

        buttonDelete = Button(self.buttonsFrame, text="<-", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonDelete.grid(row=1, column=2, sticky=N+S+E+W)

        buttonDivide = Button(self.buttonsFrame, text="/", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonDivide.grid(row=1, column=3, sticky=N+S+E+W)

        buttonMultiply = Button(self.buttonsFrame, text="*", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonMultiply.grid(row=2, column=3, sticky=N+S+E+W)

        buttonMinus = Button(self.buttonsFrame, text="-", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonMinus.grid(row=3, column=3, sticky=N+S+E+W)

        buttonPlus = Button(self.buttonsFrame, text="+", font=("Arial", 14, "bold"), cursor="hand2", bd=0, bg="#4a69bd", activebackground="#82ccdd", fg="#ecf0f1") # command=
        buttonPlus.grid(row=4, column=3, sticky=N+S+E+W)

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
    # def createButton:
    #

if __name__ == '__main__':
    calculator = App(root)
    root.mainloop()
